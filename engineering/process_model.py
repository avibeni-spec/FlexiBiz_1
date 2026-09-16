import logging

from simulation.chem_model import metals_db, simulate_chemical_process

logger = logging.getLogger(__name__)


def run_process_model(metal_name, exposure_time=1.0, environment_factor=1.0, max_degradation=0.5):
    metal = metals_db.get(metal_name)
    if metal is None:
        raise ValueError(f"Unknown metal: {metal_name}")

    simulation = simulate_chemical_process(metal_name, exposure_time, environment_factor)
    suitable = simulation["degradation"] <= max_degradation

    return {
        "metal": metal_name,
        "hardness": metal["hardness"],
        "degradation": simulation["degradation"],
        "suitable_for_process": suitable,
    }


def design_process(sim_results: dict, target_lifetime_years: float, max_cost: float) -> dict:
    logger.info(
        "Starting design_process: sim_results=%s target_lifetime_years=%s max_cost=%s",
        sim_results, target_lifetime_years, max_cost,
    )

    layer_thickness = sim_results["binding_energy"] * 10
    process_time = sim_results["thermal_stability"] * 5
    material_usage = layer_thickness * 0.8
    estimated_cost = material_usage * 3

    result = {
        "layer_thickness": layer_thickness,
        "process_time": process_time,
        "material_usage": material_usage,
        "estimated_cost": estimated_cost
    }

    logger.info("Finished design_process: result=%s", result)
    return result
