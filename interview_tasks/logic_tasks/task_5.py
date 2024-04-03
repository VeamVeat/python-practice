# "На вход подается список, элементами списка может быть число, а так же список (который формируется точно так же).
# Необходимо сделать этот список плоским, сохраняя порядок
#
# Пример
# from typing import Iterable
#
# val = [1, [2, 3], [4, [5, [6], 7], [8, 9]], 10]
#
#
# def flatten(val):
#     pass
#
# assert flatten(val) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


val = [1, [2, 3], [4, [5, [6], 7], [8, 9]], 10]
a = []


# 1
def flatten (val):
    for item in val:
        if isinstance (item, list):
            flatten (item)
        else:
            a.append(item)
    return a


b = flatten(val)
print(b)


# 2
def flatten (val):
    for item in val:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


result = [i for i in flatten(val)]
print(result)
