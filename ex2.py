# Function to find the greater number sum
def find_greater_sum(x, *args):
    res = []  # Initialize an empty list
    for arg in args:  # Iterate over each list one by one
        for item in arg:  # Then iterate over each element of the list
            if item > x and item not in res:  # If the number is greater than threshold and not present in the result then append it to the result
                res.append(item)

    total = 0
    for item in res:  # Iterate over the result list to find the total
        total += item
    return total


print(find_greater_sum(50, [10, 12, 34, 46, 55, 79, 80], [12, 22, 33, 44, 45, 60, 70, 80],
                       [9, 10, 120, 130, 140, 55, 199], [20, 23, 4, 40, 50, 12, 23, 44, 55]))
