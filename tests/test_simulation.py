import pytest

from simulation.chem_model import coatings_db, environments_db, simulate_coating


def test_simulate_coating_returns_expected_fields():
    result = simulate_coating("titanium", "anodizing", "marine")

    assert set(result.keys()) == {
        "binding_energy",
        "corrosion_index",
        "thermal_stability",
    }


def test_simulate_coating_unknown_metal_raises_value_error():
    with pytest.raises(ValueError):
        simulate_coating("unobtainium", "anodizing", "marine")


def test_simulate_coating_unknown_environment_raises_value_error():
    with pytest.raises(ValueError):
        simulate_coating("titanium", "anodizing", "space")


def test_simulate_coating_unknown_coating_raises_value_error():
    with pytest.raises(ValueError):
        simulate_coating("titanium", "unobtainium_coating", "marine")


def test_simulate_coating_applies_environment_factors():
    marine = simulate_coating("titanium", "anodizing", "marine")
    desert = simulate_coating("titanium", "anodizing", "desert")

    assert marine != desert


def test_simulate_coating_applies_coating_factors():
    anodizing = simulate_coating("titanium", "anodizing", "marine")
    peo = simulate_coating("titanium", "peo", "marine")

    assert anodizing != peo


@pytest.mark.parametrize("environment", environments_db.keys())
def test_simulate_coating_accepts_every_known_environment(environment):
    result = simulate_coating("titanium", "anodizing", environment)

    assert set(result.keys()) == {
        "binding_energy",
        "corrosion_index",
        "thermal_stability",
    }


@pytest.mark.parametrize("coating_type", coatings_db.keys())
def test_simulate_coating_accepts_every_known_coating(coating_type):
    result = simulate_coating("titanium", coating_type, "marine")

    assert set(result.keys()) == {
        "binding_energy",
        "corrosion_index",
        "thermal_stability",
    }
