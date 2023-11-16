from dependency_injector import containers, providers
from ..View_Model import Conversion_VM, Response_VM
from ..Model import Conversion, Response
from ..Data.Data_Responses_CSV import Data_Responses_CSV
from ..helpers.Enums import BasicTypes
from ..helpers import settings

#
# Notes on di library usage: The declarative container can not have any methods or any other attributes then providers.
#  https://stackoverflow.com/questions/76294480/basic-inheritance-not-works-while-using-dependency-injector-library-declarativec
# 
class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=['flexion_challenge_dsnutter.View.Conversion_View', 
                 'flexion_challenge_dsnutter.View.Response_Input_View',
                 'flexion_challenge_dsnutter.View.Response_Output_View',
                 'flexion_challenge_dsnutter.View.Main_View'
                 ]
    )

    config_conversions = providers.Configuration()
    config_responses = providers.Configuration()
        
    conversion_factory = providers.Factory(Conversion.Conversion)

    conversions_vm = providers.Factory(
            Conversion_VM.Conversion_VM,
            type=config_conversions.item,
            backend_type=config_conversions.file_type, 
            config=settings.main_configurations,
            factory=conversion_factory.provider
    )

    repsonses_factory = providers.Factory(Response.Response)
    repsonses_data_csv = providers.Singleton(Data_Responses_CSV, 
                                             type=BasicTypes.Response,
                                             filename=settings.responses_filename)

    reponses_vm = providers.Factory(
            Response_VM.Response_VM,
            type=config_responses.item,
            backend_type=config_responses.file_type, 
            config=settings.main_configurations,
            factory=repsonses_factory.provider,
            data=repsonses_data_csv
        )




