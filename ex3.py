# Function to find the frequency of occurance of each element
def find_frequency(*args):
    res = {}  # Initialized an empty dictionary
    k = 0  # Variable to keep track of the list index
    for arg in args:  # Ietrating over each list
        freq = {}  # Initialize empty dict to store the frequency of each element in single list
        for item in arg:  # Iterate over the list elements
            if item in freq:  # If the element is present increase it's freq count
                freq[item] += 1
            else:  # Otherwise initialize freq count to one
                freq[item] = 1
        temp = {}  # Initialize a dict to store the sorted dict values
        for i in sorted(freq):
            temp[i] = freq[i]
        res[f"{k}"] = temp  # Then insert the freq dict value for each list to the final resultant dict
        k += 1  # Increment the list index
    return res


print(find_frequency([10, 12, 34, 46, 55, 79, 80], [12, 22, 33, 44, 45, 60, 70, 80],
                     [9, 10, 120, 130, 140, 55, 199], [20, 23, 4, 40, 50, 12, 23, 44, 55]))
