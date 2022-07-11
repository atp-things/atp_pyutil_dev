def get_keys(dictionary: dict, keys: list):
    return {key: dictionary[key] for key in dictionary.keys() & keys}
