from dependency_injector import containers, providers
from .Conversions_Management import Conversions_Management
from ..Model import Conversion

#
# Notes on di library usage: The declarative container can not have any methods or any other attributes then providers.
#  https://stackoverflow.com/questions/76294480/basic-inheritance-not-works-while-using-dependency-injector-library-declarativec
# 
class Conversion_Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=['flexion_challenge_dsnutter.view.Conversion_View']
    )

    config = providers.Configuration()
        
    conversion_factory = providers.Factory(Conversion.Conversion)

    conversions_management = providers.Factory(
            Conversions_Management,
            conversion_type=config.item,
            config=config.definitions, 
            conversion_factory=conversion_factory.provider
        )


