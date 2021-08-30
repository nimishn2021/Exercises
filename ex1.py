# Max function to find the maximum of two numbers
def max(num1, num2):
    if num1 > num2:
        return num1
    return num2


# Max function to find the minimum of two numbers
def min(num1, num2):
    if num1 < num2:
        return num1
    return num2


# Function to find the greatest and least number
def greatest_and_least(x, arr):
    gr = float('-inf')  # Initialized with -infinity
    lr = float('inf')  # Initialized with positive infinity
    for num in arr:
        y = num % x
        if y > 0 and y > gr:  # If the remainder is greater than 0 and greater than prev remainder
            num1 = num
            gr = max(gr, y)
        if y > 0 and y < lr:  # If the remainder is greater than 0 and lesser than prev remainder
            num2 = num
            lr = min(lr, y)

    return [num1, num2]


gr, lr = greatest_and_least(10, [10, 20, 30, 40, 50, 44, 55, 60])
print(f"Greatest remainder number is {gr}")
print(f"Least remainder number is {lr}")
