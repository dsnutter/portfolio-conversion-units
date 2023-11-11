import json

#
# for importing configurations for conversions and old responses
#  that have been saved as JSON. This layer will allow replacement with
#  some type of data store/db in the future if we want it
#
class Import_Controller:
    def __init__(self, filename) -> None:
        self._conversions_config_file = filename

    @property
    def get_conversions_config(self) -> json:
        return self.to_json(self._conversions_config_file)
    
    # given json file, returns dictionary
    def to_json(self, filename) -> json:
        to_build = json.load(open(filename))

        return to_build
