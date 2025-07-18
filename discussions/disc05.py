# Q1
def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    else:
        return max([height(bran) for bran in branches(t)]) + 1
    

# Q2
def max_path_sum(t):
    """Return the maximum path sum of the tree.
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    if is_leaf(t):
        return label(t)
    else:
        return max([max_path_sum(bran) for bran in branches(t)]) + label(t)
    

# Q3
def square_tree(t):
    """Return a tree with the square of every element in t
    >>> numbers = tree(1,
    ...
    [tree(2,
    ...
    ...
    ...
    ...
    ...
    ...
    [tree(3),
    tree(4)]),
    tree(5,
    [tree(6,
    [tree(7)]),
    tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
    4
    9
    16
    25
    36
    49
    64
    """
    if is_leaf(t):
        return tree(label(t) ** 2)
    else:
        return tree(label(t) ** 2, [square_tree(bran) for bran in branches(t)])
    

# Q4
def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    # if label(tree) == x: 自己写的低效率(递归两次)、奇怪版本。陷入惯性思维, 认为if后面的下一个大段一定以else开头
    #     return [x]
    # elif not is_leaf(tree):
    #     path = [find_path(bran, x) for bran in branches(tree) if find_path(bran, x)]
    #     if path:
    #         return [label(tree)] + path[0]
        
def find_path(tree, x): # 官方答案, 优雅简洁
    if label(tree) == x:
        return [label(tree)]
    for b in branches(tree):
        path = find_path(b, x)
        if path:
            return [label(tree)] + path


# Q5
def prune_binary(t, nums):
    if is_leaf(t):
        if label(t) in nums:
            return t
        return None # 这里的None还是觉得奇怪, 应该是[]代表空树
    else:
        next_valid_nums = [x[1:] for x in nums if x[0] == label(t)]
        new_branches = []
        for sub in branches(t):
            pruned_branch = prune_binary(sub, next_valid_nums)
            if pruned_branch is not None:
                new_branches = new_branches + [pruned_branch]
        if not new_branches:
            return None
    return tree(label(t), new_branches)


def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    if change_abstraction.changed:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return {'label': label, 'branches': list(branches)}
    else:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [label] + list(branches)


def label(tree):
    """Return the label value of a tree."""
    if change_abstraction.changed:
        return tree['label']
    else:
        return tree[0]


def branches(tree):
    """Return the list of branches of the given tree."""
    if change_abstraction.changed:
        return tree['branches']
    else:
        return tree[1:]


def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if change_abstraction.changed:
        if type(tree) != dict or len(tree) != 2:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True
    else:
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True


def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)


def change_abstraction(change):
    change_abstraction.changed = change
change_abstraction.changed = False