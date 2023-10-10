def add(*args):
    sum_value = 0
    for arg in args:
        sum_value += arg
    return sum_value


sum_all = add(3, 2, 1, 6)
print(sum_all)
