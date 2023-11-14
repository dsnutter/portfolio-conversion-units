from flexion_challenge_dsnutter.di.Container import Container
from flexion_challenge_dsnutter.di.Configurations import Configurations
from flexion_challenge_dsnutter.View import Conversion_View, Response_View
from flexion_challenge_dsnutter.helpers.Enums import FileTypes


conversions_filename = 'flexion_challenge_dsnutter/configuration/conversions_config.json'
responses_filename = 'flexion_challenge_dsnutter/configuration/responses_config.json'
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



