# Q1
def keep_ints(cond, n):
    i = 1
    while i <= n:
        if cond(i):
            print(i)
        i = i + 1

def make_keeper(n):
    def f(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i = i + 1
    return f

# Q2
curry2 = lambda h: lambda x: lambda y: h(x, y)

# Q3
def print_delayed(x):
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print

# Q4
def print_n(n):
    def inner_print(x):
        if n <= 0:
            print("done")
        else:
            print(x)
        return print_n(n - 1)
    return inner_print