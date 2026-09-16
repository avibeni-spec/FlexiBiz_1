from engineering.process_model import design_process
from simulation.chem_model import simulate_coating


def test_design_process_returns_expected_fields():
    sim_results = simulate_coating("titanium", "anodizing", "marine")
    result = design_process(sim_results, target_lifetime_years=10, max_cost=1000)

    assert set(result.keys()) == {
        "layer_thickness",
        "process_time",
        "material_usage",
        "estimated_cost",
    }


def test_design_process_values_are_numeric():
    sim_results = simulate_coating("titanium", "anodizing", "marine")
    result = design_process(sim_results, target_lifetime_years=10, max_cost=1000)

    for value in result.values():
        assert isinstance(value, (int, float))
