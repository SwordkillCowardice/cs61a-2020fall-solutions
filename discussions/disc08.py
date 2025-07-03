# Q1
def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    total = 0
    while lnk is not Link.empty:
        total += lnk.first
        lnk = lnk.rest
    return total


# Q2
def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # Note: you might not need all lines in this skeleton code
    test = any([True for ls in lst_of_lnks if ls is Link.empty])
    if test:
        return Link.empty
    ans = Link(1)
    for lnk in lst_of_lnks:
        ans.first *= lnk.first
    lst_of_res = [x.rest for x in lst_of_lnks]
    ans.rest = multiply_lnks(lst_of_res)
    return ans

    # import operator  # 官方给的一种迭代解法
    # from functools import reduce

    # def prod(factors):
    #     return reduce(operator.mul, factors, 1)
    
    # head = Link.empty
    # tail = head
    # while Link.empty not in lst_of_lnks:
    #     all_prod = prod([l.first for l in lst_of_lnks])
    #     if head is Link.empty:
    #         head = Link(all_prod)
    #         tail = head
    #     else:
    #         tail.rest = Link(all_prod)
    #         tail = tail.rest
    #     lst_of_lnks = [l.rest for l in lst_of_lnks]
    # return head


# Q3
def flip_two(lnk):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    if lnk is Link.empty or lnk.rest is Link.empty:
        return
    lnk.first, lnk.rest.first = lnk.rest.first, lnk.first
    flip_two(lnk.rest.rest)


# Q4
def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> next(g)
    StopIteration
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    while link is not Link.empty: 
        if f(link.first):
            yield link.first
        link = link.rest

    # if link is not Link.empty: # 自己还写了一个递归解
    #     if f(link.first):
    #         yield link.first
    #     yield from filter_link(link.rest, f)


# Q5
def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    # if t.label % 2 != 0:  
    #     t.label += 1
    # if not t.is_leaf(): # 自己写的答案，这一行是不需要的，因为如果t是叶子, 下面的for loop自然不会执行
    #     for bra in t.branches:
    #         make_even(bra)

    if t.label % 2 != 0:
        t.label += 1
    for bra in t.branches:
        make_even(bra)


# Q6
def square_tree(t):
    """Mutates a Tree t by squaring all its elements."""
    t.label = t.label * t.label
    for bra in t.branches:
        square_tree(bra)


# Q7
def find_paths(t, entry):
    """ 
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    >>> find_paths(Tree(1, [Tree(2, [Tree(3), Tree(2)])]), 2) 
    [[1, 2], [1, 2, 2]]
    """
    # paths = []
    # if t.label == entry:
    #     return [[t.label]] # 错误的实现, 在于这一行, 当前标签等于所求不应该直接返回, 因为可能还有其他路径
    # for bra in t.branches: # 最后一个测试用例是自己写的
    #     for path in find_paths(bra, entry):
    #         paths.append([t.label] + path)
    # return paths

    paths = []
    if t.label == entry:
        paths.append([t.label])
    for bra in t.branches:
        for path in find_paths(bra, entry):
            paths.append([t.label] + path)
    return paths


# Q8
def combine_tree(t1, t2, combiner):
    """
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """
    new_label = combiner(t1.label, t2.label)
    new_branches = []
    for bra1, bra2 in zip(t1.branches, t2.branches):
        new_branches.append(combine_tree(bra1, bra2, combiner))
    return Tree(new_label, new_branches)


# Q9
def alt_tree_map(t, map_fn):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x:-x
    >>> alt_tree_map(t, negate)
    Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
    """
    t.label = map_fn(t.label) # 复刻课上John老师的思路写的
    for next_bra in t.branches:
        for bra in next_bra.branches:
            alt_tree_map(bra, map_fn)

    # def helper(t, depth):  官答, 但由于缺乏_repr_方法, 仍然无法通过文档测试
    #     if depth % 2 == 0:
    #         label = map_fn(t.label)
    #     else:
    #         label = t.label
    #     branches = [helper(b, depth + 1) for b in t.branches]
    #     return Tree(label, branches)
    # return helper(t, 0)


class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)
    
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'   
    

class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches