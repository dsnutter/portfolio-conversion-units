import json, csv
from enum import Enum

BackendTypes = Enum('BackendTypes', ['JSON', 'CSV'])

def conversions_file_to_dict(filename: str, file_type: BackendTypes) -> dict:
    try:
        if file_type == BackendTypes.CSV:
            with open(filename, newline='') as file:
                lines = csv.DictReader(f=file, delimiter=',')
                result = {}
                for items in lines:
                    # DSN Notes: not totally sure this is the correct way to do this
                    if items["Type"] not in result:
                        result[items["Type"]] = {}
                    if items["From"] not in result[items["Type"]]:
                        result[items["Type"]][items["From"]] = {}
                    if items["To"] not in result[items["Type"]][items["From"]]:
                        result[items["Type"]][items["From"]][items["To"]] = {}
                    result[items["Type"]][items["From"]][items["To"]]['eq'] = items["equation"]
                    result[items["Type"]][items["From"]][items["To"]]['ID'] = items["ID"]
            file.close()
            return result
        elif file_type == BackendTypes.JSON:
            result = json.load(open(filename))
        else:
            result = None

        return result
    except FileNotFoundError:
        return {}
    
def save_conversion_dict_to_file(config: dict, filename: str, file_type: BackendTypes) -> dict:
    try:
        if file_type == BackendTypes.JSON:
            with open(filename, 'w+') as file:
                json.dump(obj=config, fp=file, indent=4)
            file.close()
        elif file_type == BackendTypes.CSV:
            with open(filename, 'w+', newline='') as file:
                lines = csv.DictWriter(file, [ 'Type', 'From', 'To', 'equation', 'ID' ])
                lines.writeheader()
                for cname in config:
                    for from_c in config[cname]:
                        for to_c in config[cname][from_c]:
                            lines.writerow({ 'Type': cname, 'From': from_c, 'To': to_c, 'equation': config[cname][from_c][to_c]['eq'], 'ID': config[cname][from_c][to_c]['ID'] })
            file.close()
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not write to: {filename}")


def convert_new_eq_from_test_parameters():
    eqs = '''
    #temperature,Farenheit,Celsius
    ("(x-32.0) * (5.0/9.0)", 100.0, 37.8)
    #temperature,Farenheit,Kelvin
    ("((x-32.0) * (5/9)) + 273.15", 100.0, 310.9)
    #temperature,Farenheit,Rankine
    ("x + 459.67", 100.0, 559.7)
    #temperature,Celsius,Farenheit
    ("(x * (9/5)) + 32.0", 100.0, 212)
    #temperature,Celsius,Kelvin
    ("x + 273.15", 100.0, 373.2)
    #temperature,Celsius,Rankine
    ("(x + 273.15) * 9/5", 100.0, 671.7)
    #temperature,Kelvin,Farenheit
    ("((x-273.15) * (9/5)) + 32.0", 100.0, -279.7)
    #temperature,Kelvin,Celsius
    ("x - 273.150", 100.0, -173.2)
    #temperature,Kelvin,Rankine
    ("x * 9/5", 100, 180)
    #temperature,Rankine,Farenheit
    ("x - 459.67", 100, -359.7)
    #temperature,Rankine,Celsius
    ("(x * 5/9) - 273.15", 100, -217.6)
    #temperature,Rankine,Kelvin
    ("x * 5/9", 100, 55.6)
    #temperature,ThinkDifferent,Kelvin
    ("x + 1", 100, 101)
    #volume,Liters,Tablespoons
    ("x * (67.0 + 2/3)", 100, 6766.6667)
    #volume,Liters,Cubic_inches
    ("x * 61.023744", 100, 6102.4)
    #volume,Liters,Cups
    ("x * 4.2267528377", 100, 422.7)
    #volume,Liters,Cubic_feet
    ("x / 28.317", 100, 3.5)
    #volume,Liters,Gallons
    ("x / 3.785", 100, 26.4)
    #volume,Tablespoons,Liters
    ("x / (67.0 + 2/3)", 100, 1.5)
    #volume,Tablespoons,Cubic_inches
    ("x * 0.902344", 100, 90.2)
    #volume,Tablespoons,Cups
    ("x * (1/16)", 100, 6.25)
    #volume,Tablespoons,Cubic_feet
    ("x / 1915", 100, 0.1)
    #volume,Tablespoons,Gallons
    ("x / 256", 100, 0.4)
    #volume,Cubic_inches,Liters
    ("x / 61.023744", 100, 1.6)
    #volume,Cubic_inches,Tablespoons
    ("x /  0.902344", 100, 110.8)
    #volume,Cubic_inches,Cups
    ("x / 14.438", 100, 6.9)
    #volume,Cubic_inches,Cubic_feet
    ("x / 1728", 100, 0.1)
    #volume,Cubic_inches,Gallons
    ("x / 231", 100, 0.4)
    #volume,Cups,Liters
    ("x / 4.2267528377", 100, 23.7)
    #volume,Cups,Tablespoons
    ("x / (1/16)", 100, 1600)
    #volume,Cups,Cubic_inches
    ("x * 14.438", 100, 1443.8)
    #volume,Cups,Cubic_feet
    ("x / 119.7", 100, 0.8)
    #volume,Cups,Gallons
    ("x * 0.0625", 100, 6.3)
    #volume,Cubic_feet,Liters
    ("x / 0.035315", 100, 2831.7)
    #volume,Cubic_feet,Tablespoons
    ("x * 1915.01", 100, 191501)
    #volume,Cubic_feet,Cubic_inches
    ("x * 1728", 100, 172800)
    #volume,Cubic_feet,Cups
    ("x * 119.688", 100, 11968.8)
    #volume,Cubic_feet,Gallons
    ("x * 7.480519", 100, 748.1)
    #volume,Gallons,Liters
    ("x / 0.264172", 100, 378.5)
    #volume,Gallons,Tablespoons
    ("x * 256", 100, 25600)
    #volume,Gallons,Cubic_inches
    ("x / 0.004329", 100, 23100)
    #volume,Gallons,Cups
    ("x / 0.0625", 100, 1600)
    #volume,Gallons,Cubic_feet
    ("x / 7.480519", 100, 13.4)
    '''

    items = eqs.split('\n')

    i = 0
    with open('./temp.csv', 'w+', newline='') as file:
        file.writelines(['Type,From,To,equation,ID\n'])
        for item in items:
            if item.startswith('#'):
                first_part = item.replace('#', '')
                print(first_part)
            else:
                print(item)
                length = len(item)
                # skip the first (
                item = item[1:length]
                arr = item.split(',')
                second_part = arr[0].replace('"', '')
            if i > 0 and i % 2 == 0:
                line = [f'{first_part},{second_part},\n']
                file.writelines(line)
                print('test')
            i += 1
        file.close()

def convert_csv_to_json_conversions():
    conversions_filename = '../src/dsnutter_conversion_units/configuration/conversions_config.csv'
    conversions_filename_to = './temp.json'

    hashmap = conversions_file_to_dict(conversions_filename, BackendTypes.CSV)

    save_conversion_dict_to_file(hashmap, conversions_filename_to, BackendTypes.JSON)

#convert_csv_to_json_conversions()