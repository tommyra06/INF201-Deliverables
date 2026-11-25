class Temperature:

    def __init__(self, value: float, unit: str):
        unit = unit.upper()
        self.absolue_zero = {
            'K': 0, 
            'C': -273.15, 
            'F': -459.67
            }
        
        if unit not in ('K', 'C', 'F') or value < self.absolue_zero[unit] - 1e-9:
            raise ValueError('Invalid unit')
        
        self._value = value
        self._unit = unit

    def to_celsius(self) -> float:
        if self._unit == 'F':
            return((self._value - 32) * (5 / 9))
        elif self._unit == 'K':
            return(self._value - 273.15)
        else:
            return(self._value)

    def to_fahrenheit(self) -> float:
        if self._unit == 'C':
            return((self._value * (9 / 5)) + 32)
        elif self._unit == 'K':
            return((self._value - 273.15) * (9 / 5) + 32)
        else:
            return(self._value)

    def to_kelvin(self) -> float:
        if self._unit == 'C':
            return(self._value + 273.15)
        elif self._unit == 'F':
            return((self._value - 32) * (5 / 9) + 273.15)
        else:
            return(self._value)

    def convert_to(self, target_unit: str) -> object:
        converters = {
            'K': self.to_kelvin, 
            'F': self.to_fahrenheit, 
            'C': self.to_celsius
            }
        target_unit = target_unit.upper()

        if target_unit not in converters:
            raise ValueError('Invalid unit')
        
        return Temperature(converters[target_unit](), target_unit)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return abs(self.to_kelvin() - other.to_kelvin()) <= 1e-9

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return not self.__eq__(other)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_kelvin() < other.to_kelvin()

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return self < other or self == other

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return other < self

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return other <= self
    
    def __repr__(self) -> str:
        return(f'Temperature({self._value}, {self._unit})')

    def __str__(self) -> str:
        degree_sign = '\N{DEGREE SIGN}'
        return(f'{self._value:.2f} {degree_sign + self._unit}')

    @property
    def value(self) -> float:
        return self._value

    @property
    def unit(self) -> str:
        return self._unit



        