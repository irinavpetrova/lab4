import random

def field(lst, *args):
    assert len(args) > 0
    for i in lst:
        if len(args) == 1:
            if args[0] in i:
                yield i[args[0]]
        elif len(args) > 1:
            result = {}
            for k in args:
                if k in i:
                    result[k] = i[k]
            if result != {}:
                yield result


def gen_random(start, stop, number):
    for i in range(number):
        yield random.randrange(start, stop)
