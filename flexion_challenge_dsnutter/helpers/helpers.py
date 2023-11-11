import json

# given json file, returns dictionary
def to_json(filename):
    to_build = json.load(open(filename))

    return to_build
