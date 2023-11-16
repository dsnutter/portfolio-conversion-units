from .Container import Container
from .Configurations import Configurations

# this was put in a separate file due to circular dependencies
class DI_Wireup:
    
    def __init__(self, file_type: str, config: Configurations) -> None:
        self._containers = {}
        self._file_type = file_type
        self._config = config
        self._stop = False

    def wire_up(self, type: str, modules: list):

        if type not in self._containers:
            self._containers[type] = {}

        # setups up injection of temperature/responses conversion Models derived from JSON files
        self._containers[type] = Container(config_conversions={'item': type, 'file_type': self._file_type},
                                            config_responses={'item': type, 'file_type': self._file_type})

        # wires the views to the Models, and depenency injection auto-creates the Models when they are neededd
        self._containers[type].wire(modules=modules)

    @property
    def types(self):
        return self._config.types
    
    @property
    def halt(self):
        return self._stop
    
    @halt.setter
    def halt(self, value):
        self._stop = value