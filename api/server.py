import logging

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from data.models import CoatingRun, SessionLocal, save_run
from engineering.process_model import design_process
from simulation.chem_model import coatings_db, environments_db, metals_db, simulate_coating

logger = logging.getLogger(__name__)

app = FastAPI()


class CoatingProcessRequest(BaseModel):
    metal_type: str
    coating_type: str
    environment: str
    target_lifetime_years: float
    max_cost: float


@app.post("/design-coating-process")
def design_coating_process(request: CoatingProcessRequest):
    logger.info("Received request: POST /design-coating-process %s", request.model_dump())

    if request.metal_type.lower() not in metals_db:
        raise HTTPException(status_code=400, detail=f"Invalid metal_type: {request.metal_type}")
    if request.coating_type.lower() not in coatings_db:
        raise HTTPException(status_code=400, detail=f"Invalid coating_type: {request.coating_type}")
    if request.environment.lower() not in environments_db:
        raise HTTPException(status_code=400, detail=f"Invalid environment: {request.environment}")
    if request.target_lifetime_years <= 0:
        raise HTTPException(status_code=400, detail="target_lifetime_years must be greater than 0")
    if request.max_cost <= 0:
        raise HTTPException(status_code=400, detail="max_cost must be greater than 0")

    sim_results = simulate_coating(
        request.metal_type, request.coating_type, request.environment
    )

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

    logger.info("Sending response: POST /design-coating-process %s", process_results)
    return process_results


@app.get("/available-metals")
def get_available_metals():
    logger.info("Received request: GET /available-metals")

    result = list(metals_db.keys())

    logger.info("Sending response: GET /available-metals %s", result)
    return result


@app.get("/available-environments")
def get_available_environments():
    logger.info("Received request: GET /available-environments")

    result = list(environments_db.keys())

    logger.info("Sending response: GET /available-environments %s", result)
    return result


@app.get("/coating-runs")
def get_coating_runs():
    logger.info("Received request: GET /coating-runs")

    session = SessionLocal()
    try:
        runs = session.query(CoatingRun).all()
        result = [
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

    logger.info("Sending response: GET /coating-runs (%d runs)", len(result))
    return result


def start_server(host="127.0.0.1", port=8000):
    import uvicorn

    uvicorn.run(app, host=host, port=port)
