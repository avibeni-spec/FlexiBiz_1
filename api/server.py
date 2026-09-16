from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from data.models import CoatingRun, SessionLocal, save_run
from engineering.process_model import design_process
from simulation.chem_model import simulate_coating

app = FastAPI()


class CoatingProcessRequest(BaseModel):
    metal_type: str
    coating_type: str
    environment: str
    target_lifetime_years: float
    max_cost: float


@app.post("/design-coating-process")
def design_coating_process(request: CoatingProcessRequest):
    try:
        sim_results = simulate_coating(
            request.metal_type, request.coating_type, request.environment
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    process_results = design_process(
        sim_results, request.target_lifetime_years, request.max_cost
    )

    save_run({
        "metal_type": request.metal_type,
        "coating_type": request.coating_type,
        "environment": request.environment,
        **sim_results,
        **process_results,
    })

    return process_results


@app.get("/coating-runs")
def get_coating_runs():
    session = SessionLocal()
    try:
        runs = session.query(CoatingRun).all()
        return [
            {
                "id": run.id,
                "metal_type": run.metal_type,
                "coating_type": run.coating_type,
                "environment": run.environment,
                "binding_energy": run.binding_energy,
                "corrosion_index": run.corrosion_index,
                "thermal_stability": run.thermal_stability,
                "layer_thickness": run.layer_thickness,
                "process_time": run.process_time,
                "material_usage": run.material_usage,
                "estimated_cost": run.estimated_cost,
            }
            for run in runs
        ]
    finally:
        session.close()


def start_server(host="127.0.0.1", port=8000):
    import uvicorn

    uvicorn.run(app, host=host, port=port)
