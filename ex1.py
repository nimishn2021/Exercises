def max(num1, num2):
    if num1 > num2:
        return num1
    return num2


def min(num1, num2):
    if num1 < num2:
        return num1
    return num2


def greatest_and_least(x, arr):
    gr = float('-inf')
    lr = float('inf')
    for num in arr:
        y = num % x
        if y > 0 and y > gr:
            num1 = num
            gr = max(gr, y)
        if y > 0 and y < lr:
            num2 = num
            lr = min(lr, y)

    return [num1, num2]


gr, lr = greatest_and_least(10, [10, 20, 30, 40, 50, 44, 55, 60])
print(f"Greatest remainder number is {gr}")
print(f"Least remainder number is {lr}")
