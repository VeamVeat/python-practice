m_input = {
    "a": 1,
    "b": 2
}

# m_output = {
#     "A": 1,
#     "B": 2
# }


def b(**kwargs):
    dict_keys = list(kwargs.keys())

    for i in dict_keys:
        kwargs[i.upper()] = kwargs[i]
        del kwargs[i]

    return kwargs


e = b(**m_input)

print(e)
