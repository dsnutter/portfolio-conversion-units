from dsnutter_conversion_units.di.Container import Container
from dsnutter_conversion_units.di.Configurations import Configurations
from dsnutter_conversion_units.View import Conversion_View, Response_View
from dsnutter_conversion_units.helpers.Enums import FileTypes


conversions_filename = 'dsnutter_conversion_units/configuration/conversions_config.json'
responses_filename = 'dsnutter_conversion_units/configuration/responses_config.json'
types = ['temperature', 'volume']

c_json = Configurations(FileTypes.JSON, 
                        conversions_filename, 
                        responses_filename)

c_json.wire_up(types[0])

# execute the view for temperatures
Conversion_View.Conversion_View.All_Possible_Types()

# enter responses
Response_View.Response_View.Entry_Of_Single_Reponse(types[0])

# execute the view for responses
Response_View.Response_View.Display_Of_All_Responses()

c_json.wire_up(types[1])

# execute the view for temperatures
Conversion_View.Conversion_View.All_Possible_Types()

# execute the view for responses
Response_View.Response_View.Display_Of_All_Responses()



