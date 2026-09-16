import pytest

from simulation.chem_model import simulate_coating


def test_simulate_coating_returns_expected_fields():
    result = simulate_coating("titanium", "anodized", "marine")

    assert set(result.keys()) == {
        "binding_energy",
        "corrosion_index",
        "thermal_stability",
    }


def test_simulate_coating_unknown_metal_raises_value_error():
    with pytest.raises(ValueError):
        simulate_coating("unobtainium", "anodized", "marine")
