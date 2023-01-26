def max_sequence(arr):
    if len(arr) == 0:
        return 0
    best_sum = 0
    summa = 0
    for x in arr:
        summa = max(x, summa + x)
        best_sum = max(best_sum, summa)
    return best_sum