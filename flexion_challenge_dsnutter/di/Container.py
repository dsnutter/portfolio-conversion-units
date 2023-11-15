from dependency_injector import containers, providers
from ..View_Model import Conversion_VM, Response_VM
from ..Model import Conversion, Response

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
            type=config_conversions.item,
            backend_type=config_conversions.file_type, 
            responses_config=config_responses.definitions, 
            conversions_config=config_conversions.definitions,
            factory=conversion_factory.provider
    )

    repsonses_factory = providers.Factory(Response.Response)

    reponses_vm = providers.Factory(
            Response_VM.Response_VM,
            type=config_responses.item,
            backend_type=config_responses.file_type, 
            responses_config=config_responses.definitions, 
            conversions_config=config_conversions.definitions,
            factory=repsonses_factory.provider,
            load_preexisting=True
        )




