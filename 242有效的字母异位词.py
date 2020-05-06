def func(s, t):
    (list(s)).sort()
    (list(t)).sort()
    print(list(s), list(t))
    return s == t


print(func('abc', 'cba'))


def myfunc():
    return True if sorted(s) == sorted(t) else False