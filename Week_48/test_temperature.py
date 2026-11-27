import pytest
from temperature_reader import Temperature


def test_initialization():
    temp = Temperature(25, 'C')
    assert temp.value == 25
    assert temp.unit == 'C'

def test_read_only_properties():
    temp = Temperature(25, 'C')

    with pytest.raises(AttributeError):
        temp.value = 30

    with pytest.raises(AttributeError):
        temp.unit = 'F'

def test_validation():
    with pytest.raises(ValueError):
        Temperature(10, 'W')

    with pytest.raises(ValueError):
        Temperature(-1, 'K')

    with pytest.raises(ValueError):
        Temperature(-274, 'C')

    with pytest.raises(ValueError):
        Temperature(-460, 'F')

def test_conversions():
    assert Temperature(-273.15, 'C').to_fahrenheit() == pytest.approx(-459.67)
    assert Temperature(-459.67, 'F').to_kelvin() == pytest.approx(0)

    assert Temperature(-40, 'F').to_kelvin() == pytest.approx(233.15)
    assert Temperature(233.15, 'K').to_celsius() == pytest.approx(-40)

    assert Temperature(273.15, 'K').to_fahrenheit() == pytest.approx(32)
    assert Temperature(32, 'F').to_celsius() == pytest.approx(0)

    assert Temperature(37, 'C').to_kelvin() == pytest.approx(310.15)
    assert Temperature(310.15, 'K').to_fahrenheit() == pytest.approx(98.6)

    assert Temperature(100, 'C').to_fahrenheit() == pytest.approx(212)
    assert Temperature(212, 'F').to_kelvin() == pytest.approx(373.15)

def test_roundtrip():
    temp = Temperature(10, 'C')
    converted = temp.convert_to('F')
    converted = temp.convert_to('K')
    converted = temp.convert_to('C')

    assert converted == temp

def test_comparisons():
    assert Temperature(0, 'C') == Temperature(32, 'F')
    assert Temperature(0, 'C') < Temperature(100, 'C')
    assert Temperature(100, 'C') > Temperature(32, 'F')
    assert Temperature(0, 'C') <= Temperature(32, 'F')
    assert Temperature(100, 'C') >= Temperature(212, 'F')
    assert Temperature(0, 'C') != Temperature(100, 'C')

def test_str():
    temp = Temperature(25, 'C')
    assert str(temp) == '25.00 °C'

def test_repr():
    temp = Temperature(25, 'C')
    assert repr(temp) == 'Temperature(25, C)'
