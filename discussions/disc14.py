# Q1.1
def paths(x, y):
    """Return a list of ways to reach y from x by repeated
    incrementing or doubling.
    >>> paths(3, 5)
    [[3, 4, 5]]
    >>> sorted(paths(3, 6))
    [[3, 4, 5, 6], [3, 6]]
    >>> sorted(paths(3, 9))
    [[3, 4, 5, 6, 7, 8, 9], [3, 4, 8, 9], [3, 6, 7, 8, 9]]
    >>> paths(3, 3) # No calls is a valid path
    [[3]]
    """
    if x == y:
        return [[x]]
    elif x > y:
        return []
    else:
        a = [[x] + y for y in paths(x + 1, y)]
        b = [[x] + y for y in paths(2 * x, y)]
        return a + b
    

# Q1.2
def merge(s1, s2):
    """ Merges two sorted lists """
    if len(s1) == 0:
        return s2
    elif len(s2) == 0:
        return s1
    elif s1[0] < s2[0]:
        return [s1[0]] + merge(s1[1:], s2)
    else:
        return [s2[0]] + merge(s1, s2[1:])

def mergesort(seq):
    ans, length = seq[:], len(seq)
    if length == 2 and seq[1] < seq[0]:
        ans = seq[::-1]
    elif length > 2:
        ans = merge(mergesort(seq[0:length // 2]), mergesort(seq[length // 2:]))
    return ans


# Q2.1
def long_paths(tree, n):
    """Return a list of all paths in tree with length at least n.
    >>> t = Tree(3, [Tree(4), Tree(4), Tree(5)])
    >>> left = Tree(1, [Tree(2), t])
    >>> mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
    >>> right = Tree(11, [Tree(12, [Tree(13, [Tree(14)])])])
    >>> whole = Tree(0, [left, Tree(13), mid, right])
    >>> for path in long_paths(whole, 2):\
    print(path)
    <0 1 2>
    <0 1 3 4>
    <0 1 3 4>
    <0 1 3 5>
    <0 6 7 8>
    <0 6 9>
    <0 11 12 13 14>
    >>> for path in long_paths(whole, 3):\
    print(path)
    <0 1 3 4>
    <0 1 3 4>
    <0 1 3 5>
    <0 6 7 8>
    <0 11 12 13 14>
    >>> long_paths(whole, 4)
    [Link(0, Link(11, Link(12, Link(13, Link(14)))))]
    """
    if tree.is_leaf():
        return [Link(tree.label)] if n <= 0 else []
    ans = []
    for bra in tree.branches:
        for sub_path in long_paths(bra, n - 1):
            ans.append(Link(tree.label, sub_path))
    return ans


# Q2.2
def widest_level(t):
    """
    >>> sum([[1], [2]], [])
    [1, 2]
    >>> t = Tree(3, [Tree(1, [Tree(1), Tree(5)]),\
    Tree(4, [Tree(9, [Tree(2)])])])
    >>> widest_level(t)
    [1, 5, 9]
    """
    levels = [] # levels中每个元素都是一个列表，每个列表分别记录每一层的元素
    x = [t] # 存储位于同一层的树
    while x:
        levels.append([tre.label for tre in x])
        # x = sum([[bra] for cur_tre in x for bra in cur_tre.branches], [])
        x = sum([t.branches for t in x], []) # 官答：不需要使用二层嵌套，branches本身就是列表
    return max(levels, key=lambda seq: len(seq))


# Q3.1
# >>> cats = [1, 2]
# >>> dogs = [cats, cats.append(23), list(cats)]
# >>> cats
# Ans: [1, 2, 23]

# >>> dogs[1] = list(dogs)
# >>> dogs[1]
# Ans: [[1, 2, 23], None, [1, 2]]
[[1, 2, 23], None, [1, 2, 23]] # python列表评估元素，严格按照从左至右。此处在进行list(cats)之前，cats已经被修改

# >>> dogs[0].append(2)
# >>> cats
# Ans: [1, 2, 23, 2]

# >>> cats[1::2]
# Ans: [2, 2]

# >>> cats[:3]
# Ans: [1, 2, 23]

# >>> dogs[2].extend([list(cats).pop(0), 3])
# >>> dogs[3]
# Ans: Error

# >>> dogs
# Ans: [[1, 2, 23, 2], None, [1, 2, 1, 3]] 
[[1, 2, 23, 2], [[1, 2, 23, 2], None, [1, 2, 23, 1, 3]], [1, 2, 23, 1, 3]] # 别犯蠢


# Q3.2
def bake(banana, bread):
    # Ans: AC  # This line is Multiple Choice
    bread += banana[: (len(banana)- 1)]
    # banana.append(bread[banana[:1] + 1: banana[:1] + 1])
    banana.append(bread[bread[1]]) # 官答：我是小丑，没注意到第二个元素就是2
    return banana, bread
s = [1]
banana, bread = bake(s, [7, 2, s])


# Q3.3
def amon(g):
    n = 2 # n = 0
    def u(s):
        nonlocal n
        f = lambda x: x + g.pop(1) + n # f = lambda x: x + g.pop() + n
        n = n - 1 # n += 1
        return f(s)
    return u
g = [1, 2, 3]
skeld = amon(g)
pink = skeld(1)
purple = skeld(2)


# Q4.1
class Emotion():
    num = 0
    def __init__(self):
        Emotion.num += 1
        self.power = 5

    def feeling(self, other):
        if self.power == other.power:
            print("Together")
        elif self.power > other.power:
            self.catchphrase()
            other.catchphrase()
        else:
            other.catchphrase()
            self.catchphrase()

class Joy(Emotion):
    def catchphrase(self):
        print("Think positive thoughts")

class Sadness(Emotion):
    def catchphrase(self):
        print("I'm positive you will get lost")


# Q5.1
def remove_duplicates(lnk):
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> remove_duplicates(lnk)
    >>> lnk
    Link(1, Link(5))
    >>> lnk = Link(1, Link(2, Link(2, Link(1, Link(5)))))
    >>> remove_duplicates(lnk)
    >>> lnk
    Link(1, Link(2, Link(5)))
    """
    if lnk is Link.empty: # 自己写的迭代版本：具有通用性
        return
    have_seen, tmp = [lnk.first], lnk
    while tmp.rest is not Link.empty:
        if tmp.rest.first in have_seen:
            tmp.rest = tmp.rest.rest
        else:
            have_seen.append(tmp.rest.first)
            tmp = tmp.rest

    # if lnk is Link.empty or lnk.rest is Link.empty: # 官答：根据题干知链表已经排好序，所以重复元素必定是连续出现的
    #     return                                      # 这种解法不适用于非连续重复
    # if lnk.first == lnk.rest.first:
    #     lnk.rest = lnk.rest.rest
    #     remove_duplicates(lnk)
    # else:
    #     remove_duplicates(lnk.rest)
        

# Q6.1
def repeated(f):
    """
    >>> double = lambda x: 2 * x
    >>> funcs = repeated(double)
    >>> identity = next(funcs)
    >>> double = next(funcs)
    >>> quad = next(funcs)
    >>> oct = next(funcs)
    >>> quad(1)
    4
    >>> oct(1)
    8
    >>> [g(1) for _, g in zip(range(5), repeated(lambda x: 2 * x))]
    [1, 2, 4, 8, 16]
    """
    g = lambda x: x
    while True:
        yield g  # 还是老问题哈：记得画一画环境图，注意词法作用域和函数创建的过程，否则递归超出限度找不到g
        # g = lambda x: f(g(x)) 这个是第一遍写的错解，原因在上一行
        # g = (lambda ori_func, repe_func: lambda x: repe_func(ori_func(x)))(g, f)
        g = (lambda g: lambda x: f(g(x)))(g) # 官答：f为最早的父帧，不会丢失，不必作为参数传入


# Q6.2
def ben_repeated(f): 
    g = lambda x: x
    while True:
        yield g
        g = lambda x: f(g(x))
# Ans:不能正常工作，原因在Q6.1已经阐述过


# Q6.3
from operator import add, mul
def accumulate(iterable, f):
    """
    >>> list(accumulate([1, 2, 3, 4, 5], add))
    [1, 3, 6, 10, 15]
    >>> list(accumulate([1, 2, 3, 4, 5], mul))
    [1, 2, 6, 24, 120]
    """
    it = iter(iterable)
    cur = next(it)
    yield cur
    for el in it:
        cur = f(el, cur)
        yield cur


# Q7.1
# (define (deep-map fn lst)
#     (cond ((null? lst) lst)
#      ((list? (car lst)) (cons (deep-map fn (car lst)) (deep-map fn (cdr lst))))
#      (else (cons (fn (car lst)) (deep-map fn (cdr lst))))
#     )
# )


# Q8.1
# SELECT quarter FROM scoring GROUP BY quarter HAVING SUM(points) > 10;


# Q8.2
# SELECT SUM(points), team FROM scoring, players WHERE player = name GROUP BY team;


# 链表类
class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


# 树
class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()