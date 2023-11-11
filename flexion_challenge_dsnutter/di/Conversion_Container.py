from typing import Any, Union
from dependency_injector import containers, providers
from dependency_injector.providers import Provider
from ..model import Conversion, Conversions_Many

#
# Notes on di library usage: The declarative container can not have any methods or any other attributes then providers.
#  https://stackoverflow.com/questions/76294480/basic-inheritance-not-works-while-using-dependency-injector-library-declarativec
# 
class Conversion_Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=['dsnutter_conversion_units.view.Conversion_View']
    )

    config = providers.Configuration()
        
    conversion_factory = providers.Factory(Conversion.Conversion)

    conversions_many = providers.Factory(
            Conversions_Many.Conversions_Many,
            conversion_type=config.item,
            config=config.definitions, 
            conversion_factory=conversion_factory.provider
        )


