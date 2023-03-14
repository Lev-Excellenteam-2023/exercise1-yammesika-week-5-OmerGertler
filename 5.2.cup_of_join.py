# Author: Omer Gertler

from functools import reduce


def join(*lists, sep='-'):
    if len(lists) > 0:
        res = reduce(lambda x, y: x + ([sep] + y), lists, [])
        return res[1:]


print(join([1, 2], [8], [9, 5, 6], sep='@'))
print(join([1, 2], [8], [9, 5, 6]))
print(join([1]))
print(join())

