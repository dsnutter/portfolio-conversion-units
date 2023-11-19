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
        modules=['dsnutter_conversion_units.View.Conversion_View',
                 'dsnutter_conversion_units.View.Response_Input_View',
                 'dsnutter_conversion_units.View.Response_Output_View',
                 'dsnutter_conversion_units.View.Main_View'
                 ]
    )

    config_conversions = providers.Configuration()
    config_responses = providers.Configuration()

    conversion_factory = providers.Factory(Conversion.Conversion)

    conversions_vm = providers.Factory(
        Conversion_VM.Conversion_VM,
        question_type=config_conversions.item,
        backend_type=config_conversions.file_type,
        config=settings.main_configurations,
        factory=conversion_factory.provider
    )

    responses_factory = providers.Factory(Response.Response)
    responses_data_csv = providers.Singleton(Data_Responses_CSV,
                                             question_type=BasicTypes.Response,
                                             filename=settings.responses_filename)

    reponses_vm = providers.Factory(
        Response_VM.Response_VM,
        question_type=config_responses.item,
        backend_type=config_responses.file_type,
        config=settings.main_configurations,
        factory=responses_factory.provider,
        data=responses_data_csv
    )
