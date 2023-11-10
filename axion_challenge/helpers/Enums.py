from enum import Enum

GradeTypes = Enum('GradeTypes', ['CORRECT', 'INCORRECT', 'INVALID'])

# DSN Notes: could be read from a file?
TemperatureTypes = Enum('TemperatureTypes', ['Kelvin', 'Celsius', 'Fahrenheit', 'Rankine'])

# DSN Notes: could be read from a file?
VolumeTypes = Enum('VolumeTypes', ['Liters', 'Tablespoons', 'CubicInches', 'Cups', 'CubicFeet', 'Gallons'])

