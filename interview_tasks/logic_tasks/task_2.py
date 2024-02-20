

input_dict = {
    "a": 1,
    "b": 2,
    "c": {
        "d": 3,
        "e": 4,
        "f": {
            "g": 5
        },
        "h": 6
    }
}

# output_dict = {
#     "a": 1,
#     "b": 2,
#     "c,d": 3,
#     "c,e": 4,
#     "c, f, g": 5,
#     "c,h": 6
# }


def remove_last_elem(s: list[str]):
    res = ''
    for elem in s[:-1]:
        res += f'{elem},'
    return res


def translate_from_dict(d: dict, full_key: str = ''):
    for k, v in d.items():
        full_key += f'{k},'

        if isinstance(v, dict):
            translate_from_dict(v, full_key)
        else:
            print(f'{full_key}: v')

        splitted_fk = full_key.split(',')
        full_key = '' if len(splitted_fk) <= 2 else remove_last_elem(splitted_fk)


translate_from_dict(input_dict)
