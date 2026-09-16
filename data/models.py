from dataclasses import dataclass

from simulation.chem_model import metals_db


@dataclass
class MetalModel:
    name: str
    reactivity: float
    corrosion_resistance: float
    hardness: float


def define_models():
    return {
        name: MetalModel(
            name=name,
            reactivity=props["reactivity"],
            corrosion_resistance=props["corrosion_resistance"],
            hardness=props["hardness"],
        )
        for name, props in metals_db.items()
    }
