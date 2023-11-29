from enum import Enum

GradeTypes = Enum('GradeTypes', ['CORRECT', 'INCORRECT', 'INVALID'])

BackendTypes = Enum('BackendTypes', ['JSON', 'CSV'])

BasicTypes = Enum('BasicType', ['Conversion', 'Response'])
