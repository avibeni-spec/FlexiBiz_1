from engineering.process_model import run_process_model
from simulation.chem_model import metals_db


def main():
    for metal_name in metals_db:
        result = run_process_model(metal_name)
        print(f"{metal_name}: {result}")


if __name__ == "__main__":
    main()
