import json


def get_keys(dict_: dict, keys: list):
    return {key: dict_[key] for key in dict_.keys() & keys}


def load(path: str) -> dict:
    with open(path) as file_:
        ret = dict(json.load(file_))

    return ret


def get_values_from_list(list_of_dict: list, key: str, unique: bool = False):

    list_ = []
    for item in list_of_dict:
        list_.append(item[key])

    if unique:
        return list(set(list_))

    return list_


def convert_list_to_dict(list_of_dict: list, key: str):

    dict_ = {}
    duplicates_counter = 0
    for item in list_of_dict:
        key_name = item[key]
        if key_name in dict_:
            key_name = f"{key_name}_{duplicates_counter}"
            duplicates_counter += 1
        dict_[key_name] = item

    return dict_
