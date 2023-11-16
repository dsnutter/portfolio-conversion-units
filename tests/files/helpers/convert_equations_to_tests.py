import csv, json

# cmd line helper script to generate parameters for unit tests from the conversions CSV file

# copied here since this script is not in the main project so cannot include it
def conversions_file_to_dict(filename: str) -> dict:
    try:
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
            return result
    except FileNotFoundError:
        return {}


if __name__ == "__main__":
    conversions_filename = '../dsnutter_conversion_units/configuration/conversions_config.csv'
    hashmap = conversions_file_to_dict(conversions_filename) 
    filename = './parameters.csv'
    filename2 = './google-equations.csv'

    lines = []
    for type in hashmap:
        for from_type in hashmap[type]:
            for to_type in hashmap[type][from_type]:
                line = f'#{type},{from_type},{to_type}\n("{hashmap[type][from_type][to_type]["eq"]}", 0, 0),\n'
                lines.append(line)
                print(line)

    with open(filename, 'w+', newline='') as file:
        file.writelines(lines)
    file.close()

    lines = []
    for type in hashmap:
        for from_type in hashmap[type]:
            for to_type in hashmap[type][from_type]:
                line = f'100 {from_type} = ? {to_type}\n'
                lines.append(line)
                print(line)

    with open(filename2, 'w+', newline='') as file:
        file.writelines(lines)
    file.close()
