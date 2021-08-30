def find_frequency(*args):
    res = {}
    k = 1
    for arg in args:
        freq = {}
        for item in arg:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
        temp = {}
        for i in sorted(freq):
            temp[i] = freq[i]
        res[f"dict{k}"] = temp
        k += 1
    return res


print(find_frequency([10, 12, 34, 46, 55, 79, 80], [12, 22, 33, 44, 45, 60, 70, 80],
                     [9, 10, 120, 130, 140, 55, 199], [20, 23, 4, 40, 50, 12, 23, 44, 55]))
