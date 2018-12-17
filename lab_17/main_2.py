import timeit


def func():
    # return NotImplemented
    return map(reversed, ['vasya', 'bodya', 'some', 'cool', 'vasya', 'bodya', 'some', 'cool', 'vasya', 'bodya', 'some', 'cool', 'vasya', 'bodya', 'some', 'cool'])


def func_comp():
    return [reversed(a) for a in ['vasya', 'bodya', 'some', 'cool', 'vasya', 'bodya', 'some', 'cool', 'vasya', 'bodya', 'some', 'cool', 'vasya', 'bodya', 'some', 'cool']]


def func_for():
    l = []
    for a in ['vasya', 'bodya', 'some', 'cool', 'vasya', 'bodya', 'some', 'cool', 'vasya', 'bodya', 'some', 'cool', 'vasya', 'bodya', 'some', 'cool']:
        l.append(reversed(a))
    return l


print(timeit.timeit('func()', setup='from __main__ import func', number=1000))
print(timeit.timeit('func_comp()', setup='from __main__ import func_comp', number=1000))
print(timeit.timeit('func_for()', setup='from __main__ import func_for', number=1000))
