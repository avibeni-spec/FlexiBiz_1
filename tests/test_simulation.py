import pytest

from simulation.chem_model import environments_db, simulate_coating


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


def test_simulate_coating_unknown_environment_raises_value_error():
    with pytest.raises(ValueError):
        simulate_coating("titanium", "anodized", "space")


def test_simulate_coating_applies_environment_factors():
    marine = simulate_coating("titanium", "anodized", "marine")
    desert = simulate_coating("titanium", "anodized", "desert")

    assert marine != desert


@pytest.mark.parametrize("environment", environments_db.keys())
def test_simulate_coating_accepts_every_known_environment(environment):
    result = simulate_coating("titanium", "anodized", environment)

    assert set(result.keys()) == {
        "binding_energy",
        "corrosion_index",
        "thermal_stability",
    }
