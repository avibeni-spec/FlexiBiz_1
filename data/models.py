from dataclasses import dataclass

from sqlalchemy import Column, Float, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from simulation.chem_model import metals_db

engine = create_engine("sqlite:///coating_runs.db")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class CoatingRun(Base):
    __tablename__ = "coating_runs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    metal_type = Column(String, nullable=False)
    coating_type = Column(String, nullable=False)
    environment = Column(String, nullable=False)
    binding_energy = Column(Float)
    corrosion_index = Column(Float)
    thermal_stability = Column(Float)
    layer_thickness = Column(Float)
    process_time = Column(Float)
    material_usage = Column(Float)
    estimated_cost = Column(Float)


Base.metadata.create_all(engine)


def save_run(results_dict):
    session = SessionLocal()
    try:
        run = CoatingRun(**results_dict)
        session.add(run)
        session.commit()
        session.refresh(run)
        return run.id
    finally:
        session.close()


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
