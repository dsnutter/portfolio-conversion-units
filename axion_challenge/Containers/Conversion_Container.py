from dependency_injector import containers, providers
from model.Conversion import Conversion


class Conversion_Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    conversion_provider = providers.Factory(
        Conversion,
        conversionType=config.name, 
        convert_to=config.convertTo,
    )