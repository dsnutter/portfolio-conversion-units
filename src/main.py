from dsnutter_conversion_units.di.main import run_as_app
from dsnutter_conversion_units.helpers.settings import conversions_filename, responses_filename

if __name__ == "__main__":

    conversions_filename = 'src/dsnutter_conversion_units/configuration/conversions_config.csv'
    responses_filename = 'src/dsnutter_conversion_units/configuration/responses_config.csv'

    run_as_app()
