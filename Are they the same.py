def comp(array1, array2):
    c = 0
    print(array1, array2)
    if array1 == None or array2 == None:
        return False
    elif len(array1)!=len(array2):
        return False
    for i in array1:
        for j in array2:
            if i * i == j:
                array2.remove(j)
                c += 1
                break
    # print(c)
    if c == len(array1):
        return True
    else:
        return False