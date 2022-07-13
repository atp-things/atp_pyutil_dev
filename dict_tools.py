import json


def get_keys(dictionary: dict, keys: list):
    return {key: dictionary[key] for key in dictionary.keys() & keys}


def load(path: str) -> dict:
    with open(path) as file_:
        ret = dict(json.load(file_))

    return ret
