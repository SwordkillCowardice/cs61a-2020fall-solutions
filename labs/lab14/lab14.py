from operator import add, sub, mul


def prune_min(t):
    """Prune the tree mutatively from the bottom up.

    >>> t1 = Tree(6)
    >>> prune_min(t1)
    >>> t1
    Tree(6)
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune_min(t2)
    >>> t2
    Tree(6, [Tree(3)])
    >>> t3 = Tree(6, [Tree(3, [Tree(1), Tree(2)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune_min(t3)
    >>> t3
    Tree(6, [Tree(3, [Tree(1)])])
    """
    "*** YOUR CODE HERE ***"
    if t.branches:
        min_bra = min(t.branches, key=lambda bra: bra.label)
        prune_min(min_bra)
        t.branches = [min_bra]


def num_splits(s, d):
    """Return the number of ways in which s can be partitioned into two
    sublists that have sums within d of each other.

    >>> num_splits([1, 5, 4], 0)  # splits to [1, 4] and [5]
    1
    >>> num_splits([6, 1, 3], 1)  # no split possible
    0
    >>> num_splits([-2, 1, 3], 2) # [-2, 3], [1] and [-2, 1, 3], []
    2
    >>> num_splits([1, 4, 6, 8, 2, 9, 5], 3)
    12
    """
    "*** YOUR CODE HERE ***"
    # def difference_so_far(s, difference): # 官答
    #     if not s:
    #         if abs(difference) <= d:
    #             return 1
    #         else:
    #             return 0
    #     element = s[0]
    #     s = s[1:]  # 依次考虑将元素加入左边或右边，等到原集合划分完毕后，判断是否为有效划分，同时注意对称性
    #     return difference_so_far(s, difference + element) + difference_so_far(s, difference - element)
    # return difference_so_far(s, 0)//2

    # def split_two(seq): # 自己写的穷举法
    #      if not seq:
    #          return
    #      elif len(seq) == 1:
    #          return [[[seq[0]], []]]
    #      else:
    #          ans = []
    #          for case in split_two(seq[1:]):
    #              change_case0, change_case1 = case[0][:], case[1][:]
    #              change_case0.append(seq[0])
    #              change_case1.append(seq[0])
    #              ans.append([change_case0, case[1]])
    #              ans.append([case[0], change_case1])
    #          return ans

    # division, count = split_two(s), 0
    # for div in division:
    #     if not div[1]:
    #         if sum(div[0]) <= d:
    #             count += 1
    #     elif abs(sum(div[0]) - sum(div[1])) <= d:
    #         count += 1
    # return count

    def cur_div(rest, cur_dif): # 官答复写
        if not rest:
            return 1 if abs(cur_dif) <= d else 0
        cur_el = rest[0]
        return cur_div(rest[1:], cur_el + cur_dif) + cur_div(rest[1:], cur_dif - cur_el)
    return cur_div(s, 0) // 2


class Account(object):
    """A bank account that allows deposits and withdrawals.

    >>> eric_account = Account('Eric')
    >>> eric_account.deposit(1000000)   # depositing my paycheck for the week
    1000000
    >>> eric_account.transactions
    [('deposit', 1000000)]
    >>> eric_account.withdraw(100)      # buying dinner
    999900
    >>> eric_account.transactions
    [('deposit', 1000000), ('withdraw', 100)]
    """

    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        """Increase the account balance by amount and return the
        new balance.
        """
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the
        new balance.
        """
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance
    
class CheckingAccount(Account):
    """A bank account that charges for withdrawals.

    >>> check = Check("Steven", 42)  # 42 dollars, payable to Steven
    >>> steven_account = CheckingAccount("Steven")
    >>> eric_account = CheckingAccount("Eric")
    >>> eric_account.deposit_check(check)  # trying to steal steven's money
    The police have been notified.
    >>> eric_account.balance
    0
    >>> check.deposited
    False
    >>> steven_account.balance
    0
    >>> steven_account.deposit_check(check)
    42
    >>> check.deposited
    True
    >>> steven_account.deposit_check(check)  # can't cash check twice
    The police have been notified.
    """
    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)
    
    def deposit_check(self, check):
        if self.holder != check.holder:
            print("The police have been notified.")
        elif check.deposited:
            print("The police have been notified.")
        else:
            check.deposited = True
            return self.deposit(check.money)

class Check(object):
    "*** YOUR CODE HERE ***"
    def __init__(self, check_holder, check_money):
        self.holder = check_holder
        self.money = check_money
        self.deposited = False
    

def align_skeleton(skeleton, code):
    """
    Aligns the given skeleton with the given code, minimizing the edit distance between
    the two. Both skeleton and code are assumed to be valid one-line strings of code. 

    >>> align_skeleton(skeleton="", code="")
    ''
    >>> align_skeleton(skeleton="", code="i")
    '+[i]'
    >>> align_skeleton(skeleton="i", code="")
    '-[i]'
    >>> align_skeleton(skeleton="i", code="i")
    'i'
    >>> align_skeleton(skeleton="i", code="j")
    '+[j]-[i]'
    >>> align_skeleton(skeleton="x=5", code="x=6")
    'x=+[6]-[5]'
    >>> align_skeleton(skeleton="return x", code="return x+1")
    'returnx+[+]+[1]'
    >>> align_skeleton(skeleton="while x<y", code="for x<y")
    '+[f]+[o]+[r]-[w]-[h]-[i]-[l]-[e]x<y'
    >>> align_skeleton(skeleton="def f(x):", code="def g(x):")
    'def+[g]-[f](x):'
    """
    skeleton, code = skeleton.replace(" ", ""), code.replace(" ", "")

    def helper_align(skeleton_idx, code_idx):
        """
        Aligns the given skeletal segment with the code.
        Returns (match, cost)
            match: the sequence of corrections as a string
            cost: the cost of the corrections, in edits
        """
        if skeleton_idx == len(skeleton) and code_idx == len(code):
            return "", 0
        if skeleton_idx < len(skeleton) and code_idx == len(code):
            edits = "".join(["-[" + c + "]" for c in skeleton[skeleton_idx:]])
            return edits, len(skeleton) - skeleton_idx
        if skeleton_idx == len(skeleton) and code_idx < len(code):
            edits = "".join(["+[" + c + "]" for c in code[code_idx:]])
            return edits, len(code) - code_idx
        
        possibilities = []
        skel_char, code_char = skeleton[skeleton_idx], code[code_idx]
        # Match
        if skel_char == code_char:
            match, cost = helper_align(skeleton_idx + 1, code_idx + 1)
            possibilities.append((skel_char + match, cost))
        else:
            # Insert
            match, cost = helper_align(skeleton_idx, code_idx + 1)
            cur_op = "" + "+[" + code[code_idx] + "]"
            possibilities.append((cur_op + match, cost + 1))
            # Delete
            match, cost = helper_align(skeleton_idx + 1, code_idx)
            cur_op = "" + "-[" + skeleton[skeleton_idx] + "]"
            possibilities.append((cur_op + match, cost + 1))
        return min(possibilities, key=lambda x: x[1])
    result, cost = helper_align(0, 0)
    return result


def foldl(link, fn, z):
    """ Left fold
    >>> lst = Link(3, Link(2, Link(1)))
    >>> foldl(lst, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    >>> foldl(lst, add, 0) # (((0 + 3) + 2) + 1)
    6
    >>> foldl(lst, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    if link is Link.empty:
        return z
    "*** YOUR CODE HERE ***"
    return foldl(link.rest, fn, fn(z, link.first))


def foldr(link, fn, z):
    """Right fold: apply fn recursively from the right end of the list.
    >>> s = Link(1, Link(2, Link(3)))
    >>> foldr(s, add, 0)  # 1 + (2 + (3 + 0))
    6
    """
    if link is Link.empty:
        return z
    return fn(link.first, foldr(link.rest, fn, z))

def filterl(lst, pred):
    """ Filters LST based on PRED
    >>> lst = Link(4, Link(3, Link(2, Link(1))))
    >>> filterl(lst, lambda x: x % 2 == 0)
    Link(4, Link(2))
    """
    "*** YOUR CODE HERE ***"
    # 自己写的：使用foldl+逆序/插入
    # reverse_lst = foldl(lst, lambda cur_ls, el: Link(el, cur_ls) if pred(el) else cur_ls, Link.empty)
    # return reverse(reverse_lst)

    # def lst_append(lst, el):
    #     if lst is Link.empty:
    #         return Link(el, lst)
    #     tmp = lst
    #     while tmp.rest is not Link.empty:
    #         tmp = tmp.rest
    #     tmp.rest = Link(el, Link.empty)
    #     return lst

    # return foldl(lst, lambda cur_ls, el: lst_append(cur_ls, el) if pred(el) else cur_ls, Link.empty)

    # 官答: 使用foldr
    def filtered(x, xs):
        if pred(x):
            return Link(x, xs)
        return xs
    return foldr(lst, filtered, Link.empty)

def reverse(lst):
    """ Reverses LST with foldl
    >>> reverse(Link(3, Link(2, Link(1))))
    Link(1, Link(2, Link(3)))
    >>> reverse(Link(1))
    Link(1)
    >>> reversed = reverse(Link.empty)
    >>> reversed is Link.empty
    True
    """
    "*** YOUR CODE HERE ***"
    # return foldl(lst, lambda cur, el: Link(el, cur), Link.empty) # 法0

    # len, track = 0, lst # 法一：类似冒泡排序
    # while track is not Link.empty:
    #     track, len = track.rest, len + 1
    # while len :
    #     track, count = lst, 0
    #     while count < len - 1:
    #         track.first, track.rest.first  = track.rest.first, track.first
    #         track, count = track.rest, count + 1
    #     len = len - 1
    # return lst

    # if lst is Link.empty or lst.rest is Link.empty: # 法二:递归+拷贝
    #     return lst
    # reverse_res, first_elm, tmp = reverse(lst.rest), lst.first, lst 
    # while tmp != Link.empty and reverse_res != Link.empty:
    #     tmp.first = reverse_res.first
    #     tmp, reverse_res = tmp.rest, reverse_res.rest
    # tmp.first = first_elm
    # return lst

    # Extra for experience # 官答，很巧妙。折射出我对指针操作完全不够灵活，同时理解也有偏差
    if lst is Link.empty: 
        return lst
    elif lst.rest is not Link.empty:
        second, last = lst.rest, lst # 这一行你要注意：second和last只是指在同一条链的不同位置。
        lst = reverse(second)        # 你推演着推演着都变成新开一条链了，能看懂才怪
        second.rest, last.rest = last, Link.empty 
        # 关键且你应该找到的信息：reverse(x)之后，x指针没有被拐走，他的位置是逆序链表的末尾
        # 必须采用第三行赋值的原因：本题限制不能用Link构造函数，所以为了添加第一个元素，只能拼接并修改原链表
    return lst

    # if lst is Link.empty or lst.rest is Link.empty:  # 看懂官答后自己再写一遍
    #     return lst  # 抓住三个指针就好：原链表头指针、子列表逆序后的头指针以及尾指针
    # else:           # 前两个比较好找，第三个要明白：reverse(x)之后，x指针没有被拐走，他的位置是逆序链表的末尾
    #     head, new = lst, reverse(lst.rest) 
    #     lst.rest.rest, head.rest = head, Link.empty
    #     return new



identity = lambda x: x

def foldl2(link, fn, z):
    """ Write foldl using foldr
    >>> list = Link(3, Link(2, Link(1)))
    >>> foldl2(list, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    >>> foldl2(list, add, 0) # (((0 + 3) + 2) + 1)
    6
    >>> foldl2(list, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    def step(x, g):
        "*** YOUR CODE HERE ***"
        # return lambda y: fn(g(y), x) # 错解：(((0 - 1) - 2) - 3)
        return lambda a: g(fn(a, x)) # 官答: (((0 - 3) - 2) - 1)
    return foldr(link, step, identity)(z)

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

