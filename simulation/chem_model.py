import logging

logger = logging.getLogger(__name__)

metals_db = {
    "aluminum": {"reactivity": 0.7, "corrosion_resistance": 0.5, "hardness": 0.3},
    "steel": {"reactivity": 0.4, "corrosion_resistance": 0.3, "hardness": 0.8},
    "stainless_steel": {"reactivity": 0.2, "corrosion_resistance": 0.9, "hardness": 0.7},
    "titanium": {"reactivity": 0.1, "corrosion_resistance": 0.95, "hardness": 0.9},
    "magnesium": {"reactivity": 0.9, "corrosion_resistance": 0.2, "hardness": 0.2},
    "copper": {"reactivity": 0.6, "corrosion_resistance": 0.4, "hardness": 0.5}
}

environments_db = {
    "marine": {"salt_factor": 1.2, "temp_factor": 0.9},
    "industrial": {"salt_factor": 1.0, "temp_factor": 1.1},
    "desert": {"salt_factor": 0.6, "temp_factor": 1.3},
    "lab": {"salt_factor": 0.3, "temp_factor": 0.8}
}


def simulate_chemical_process(metal_name, exposure_time=1.0, environment_factor=1.0):
    logger.info(
        "Starting simulate_chemical_process: metal_name=%s exposure_time=%s environment_factor=%s",
        metal_name, exposure_time, environment_factor,
    )

    metal = metals_db.get(metal_name)
    if metal is None:
        raise ValueError(f"Unknown metal: {metal_name}")

    corrosion_level = (
        metal["reactivity"]
        * (1 - metal["corrosion_resistance"])
        * exposure_time
        * environment_factor
    )
    degradation = corrosion_level * (1 - metal["hardness"] * 0.3)

    result = {
        "metal": metal_name,
        "corrosion_level": round(corrosion_level, 4),
        "degradation": round(degradation, 4),
    }

    logger.info("Finished simulate_chemical_process: result=%s", result)
    return result


def simulate_coating(metal_type: str, coating_type: str, environment: str) -> dict:
    logger.info(
        "Starting simulate_coating: metal_type=%s coating_type=%s environment=%s",
        metal_type, coating_type, environment,
    )

    data = metals_db.get(metal_type.lower())
    if not data:
        raise ValueError("Metal type not supported")

    env_data = environments_db.get(environment.lower())
    if not env_data:
        raise ValueError("Environment not supported")

    salt_factor = env_data["salt_factor"]
    temp_factor = env_data["temp_factor"]

    binding_energy = (data["hardness"] * 0.6) + (data["corrosion_resistance"] * 0.4)
    corrosion_index = (data["reactivity"] * 0.7) - (data["corrosion_resistance"] * 0.3)
    thermal_stability = (data["hardness"] + data["corrosion_resistance"]) / 2

    binding_energy *= temp_factor
    corrosion_index *= salt_factor
    thermal_stability *= (temp_factor + salt_factor) / 2

    result = {
        "binding_energy": binding_energy,
        "corrosion_index": corrosion_index,
        "thermal_stability": thermal_stability
    }

    logger.info("Finished simulate_coating: result=%s", result)
    return result
