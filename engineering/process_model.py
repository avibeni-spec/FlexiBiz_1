from simulation.chem_model import metals_db, simulate_chemical_process


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
