def find_greater_sum(x, *args):
    res = []
    for arg in args:
        for item in arg:
            if item > x and item not in res:
                res.append(item)

    total = 0
    for item in res:
        total += item
    return total


print(find_greater_sum(50, [10, 12, 34, 46, 55, 79, 80], [12, 22, 33, 44, 45, 60, 70, 80],
                       [9, 10, 120, 130, 140, 55, 199], [20, 23, 4, 40, 50, 12, 23, 44, 55]))
