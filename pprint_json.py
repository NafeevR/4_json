import json


def load_data(filepath):
    data_from_json_file = []
    with open(filepath) as data_file:
        data_from_json_file = json.load(data_file)
    return data_from_json_file


def pretty_print_json(data):
    print (json.dumps(data, indent=4, sort_keys=True))


if __name__ == '__main__':
    path_to_file = input('Input path to the file = ')
    json_info = load_data(path_to_file)
    pretty_print_json(json_info)