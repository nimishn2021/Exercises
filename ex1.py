def greatest_and_least(x, arr):
    gr = float('-inf')
    lr = float('inf')
    for i in range(len(arr)):
        y = arr[i] % x
        if y > 0 and y > gr:
            num1 = arr[i]
            gr = max(gr, y)
        if y > 0 and y < lr:
            num2 = arr[i]
            lr = min(lr, y)

    return [num1, num2]


gr, lr = greatest_and_least(10, [10, 20, 30, 40, 50, 44, 55, 60])
print(f"Greatest remainder number is {gr}")
print(f"Least remainder number is {lr}")
