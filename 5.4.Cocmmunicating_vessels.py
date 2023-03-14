# Author: Omer Gertler


INPUT = ('abc', [1, 2, 3], ('!', '@', '#'))


def interleave(*iterables):
    """
    return list of zipped iterables items (like strings, lists. tuples)
    :param iterables: iterables items
    :return: zipped list
    """
    return [i for item in zip(*iterables) for i in item]


def interleave2(*iterables):
    """
    generator version of the interleave function
    """
    zipped = zip(*iterables)
    for i in zipped:
        for j in i:
            yield j


list_interleave = interleave(*INPUT)
gen_interleave = interleave2(*INPUT)
print(list_interleave)
print(list(gen_interleave))




