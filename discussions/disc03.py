# Q1
def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if n == 0:
        return 0
    else:
        return m + multiply(m, n - 1)
    # if m == 0:
    #     return 0
    # else:
    #     return n + multiply(m - 1, n)


# Q2
# Answer: 求pow(x, y)


# Q3
def hailstone(n):
    """Printoutthehailstonesequencestartingatn,andreturnthe
    numberof elementsinthesequence.
    >>>a=hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>>a
    7
    """
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return hailstone(n // 2) + 1
    else:
        return hailstone(3 * n + 1) + 1


# Q4
def merge(n1, n2):
    """ Merges two numbers
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    else:
        x = n1 % 10
        y = n2 % 10
        if x <= y:
            return merge(n1 // 10, n2) * 10 + x
        else:
            return merge(n1, n2 // 10) * 10 + y


# Q5
def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """
    def repeat(times):
        if times == 0:
            return x
        else:
            return f(repeat(times - 1))
    return repeat


# Q6
def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    def prime_helper(x):
        if x == 0:
            return False
        elif x == 1:
            return True
        else:
            return n % x != 0 and prime_helper(x - 1)
    return prime_helper(n - 1)