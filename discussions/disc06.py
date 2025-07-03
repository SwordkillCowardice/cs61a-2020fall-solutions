# Q1
def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def f(g):
        nonlocal n
        n = g(n)
        return n
    return f


# Q2
def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """
    grouped = {}
    for el in s:
        key = fn(el)
        if key in grouped:
            grouped[key].append(el)
        else:
            grouped[key] = [el]
    return grouped


# Q3
def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs
    in s.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    result = [el for e in s if e == x]
    s.extend(result)

# Q4
def filter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter(range(5), is_even)) # a list of the values yielded from the call to filter
    [0 , 2 , 4]
    >>> all_odd = (2*y-1 for y in range (5))
    >>> list(filter(all_odd, is_even))
    []
    >>> s = filter(naturals(), is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    result = [x for x in iterable if fn(x)]
    yield from result


# Q5
def merge(a, b):
    """
    >>> def sequence(start, step):
    ... while True:
    ...
    yield start
    ...
    start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    # def helper_merge(s1, s2): # 自己写的一个错误版本A
    #     e1, e2 = next(s1), next(s2)
    #     if e1 == e2:
    #         yield(e1)
    #         helper_merge(a, b)
    #     elif e1 < e2:
    #         yield(e1)
    #         helper_merge(a, iter([e2]))
    #     else:
    #         yield(e2)
    #         helper_merge(iter([e1], b))
    # return helper_merge(a, b)

    # def helper_merge(s1, s2): # 参考AI意见后修改的版本B，可以通过range(10)的测试，但AI认为版本B行不通
    #     e1, e2 = next(s1), next(s2) # 我不明白B中yield from的必要性(尚未解决)，我认为只要执行递归函数就必定会不断yield
    #     if e1 == e2:
    #         yield e1
    #         yield from helper_merge(a, b)
    #     elif e1 < e2:
    #         yield e1
    #         yield from helper_merge(a, iter([e2]))
    #     else:
    #         yield e2
    #         yield from helper_merge(iter([e1]), b) 
    # return helper_merge(a, b)

    # 官方答案
    first_a, first_b = next(a), next(b)
    while True:    # 困住你的只是简简单单一个死循环......
        if first_a == first_b:
            yield first_a
            first_a, first_b = next(a), next(b)
        elif first_a < first_b:
            yield first_a
            first_a = next(a)
        else:
            yield first_b
            first_b = next(b)