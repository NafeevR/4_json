import json


def load_data(filepath):
    data = []
    with open(filepath) as data_file:
        data = json.load(data_file)
    return data


def pretty_print_json(data):
    print (json.dumps(data, indent=4, sort_keys=True))


if __name__ == '__main__':
    path_to_the_file = input('Input path to the file = ')
    json_info = load_data(path_to_the_file)
    pretty_print_json(json_info)