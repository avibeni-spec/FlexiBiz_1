from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

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

    return design_process(
        sim_results, request.target_lifetime_years, request.max_cost
    )


def start_server(host="127.0.0.1", port=8000):
    import uvicorn

    uvicorn.run(app, host=host, port=port)
