from dependency_injector import containers, providers
from ..View_Model import Conversion_VM, Response_VM
from ..Model import Conversion, Response

#
# Notes on di library usage: The declarative container can not have any methods or any other attributes then providers.
#  https://stackoverflow.com/questions/76294480/basic-inheritance-not-works-while-using-dependency-injector-library-declarativec
# 
class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=['flexion_challenge_dsnutter.View.Conversion_View', 'flexion_challenge_dsnutter.View.Response_View']
    )

    config_conversions = providers.Configuration()
        
    conversion_factory = providers.Factory(Conversion.Conversion)

    conversions_vm = providers.Factory(
            Conversion_VM.Conversion_VM,
            conversion_type=config_conversions.item,
            config=config_conversions.definitions, 
            factory=conversion_factory.provider
        )

    config_responses = providers.Configuration()

    repsonses_factory = providers.Factory(Response.Response)

    reponses_vm = providers.Factory(
            Response_VM.Response_VM,
            response_type=config_responses.item,
            config=config_responses.definitions, 
            factory=repsonses_factory.provider,
            load_preexisting=True
        )




