def descending_order(num):
    num = str(num)
    num="".join(sorted(num, reverse=True))
    return int(num)