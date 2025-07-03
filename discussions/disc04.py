# Q1
def count_stair_ways(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)

# Q2
def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        ways, total = 0, k
        while total:
            ways += count_k(n - total, k)
            total -= 1
        return ways
    
# Q3
# >>> a = [1, 5, 4, [2, 3], 3]
# >>> print(a[0], a[-1])
# >>> len(a)
# >>> 2 in a
# >>> 4 in a
# >>> a[3][0]
# Answers：1)1 3 || 2)5 || 3)False || 4)True || 5)2

# Q4
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [s[index] * index for index in range(len(s)) if index % 2 == 0]

# Q5
def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if s == []:
        return 1
    else: # 按照取不取第一位来分类
        return max(s[0] * max_product(s[2:]), max_product(s[1:]))