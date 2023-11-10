from ..helpers.Enums import TemperatureTypes, VolumeTypes

class Conversion:

    _convert = {}

    def __init__(self, conversionType, convert_to):
        self._conversionType = conversionType
        self._convert[self._conversionType] = convert_to

    def get_type(self):
        return self._conversionType

    # if want to add additional conversions manually, maybe needs removed?
    def define_conversion(self, toType, fnConvert):
        self._convert[self._conversionType][toType] = fnConvert

    def get_fn(self, toType):
        return self._convert[self._conversionType][toType]

