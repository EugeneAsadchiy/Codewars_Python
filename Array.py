def array_diff(a, b):
    for i in range(len(b)):
        for j in range(len(a)):
            if b[i] in a:
                a.remove(b[i])
    return a


print(array_diff([1, 2], [1]))
