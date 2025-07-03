# Q1
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if raining:
        return True
    elif temp < 60:
        return True
    else:
        return False

def wears_jacket(temp, raining):
    return raining or temp < 60

# Q2
def square(x):
    print("here!")
    return x * x

def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0

square(so_slow(5))
# Answer -> Infinite Loop

# Q3
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    start = 2
    while start < n:
        if n % start == 0:
            return False
        start += 1
    return n == 2 or n != 1