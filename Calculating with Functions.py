def zero(st=None):  # your code here
    if st is None:
        st = "0"
    else:
        st = "0"+st
        st = answer(st)
    return st


def one(st=None):  # your code here
    if st is None:
        st = "1"
    else:
        st = "1"+st
        st = answer(st)
    return st


def two(st=None):  # your code here
    if st is None:
        st = "2"
    else:
        st = "2"+st
        st = answer(st)
    return st


def three(st=None):  # your code here
    if st is None:
        st = "3"
    else:
        st = "3"+st
        st = answer(st)
    return st


def four(st=None):  # your code here
    if st is None:
        st = "4"
    else:
        st = "4"+st
        st = answer(st)
    return st


def five(st=None):  # your code here
    if st is None:
        st = "5"
    else:
        st = "5" + st
        st=answer(st)
    return st


def six(st=None):  # your code here
    if st is None:
        st = "6"
    else:
        st = "6"+st
        st = answer(st)
    return st


def seven(st=None):  # your code here
    if st is None:
        st = "7"
    else:
        st = "7"+st
        st = answer(st)
    return st


def eight(st=None):  # your code here
    if st is None:
        st = "8"
    else:
        st = "8" + st
        st = answer(st)
    return st


def nine(st=None):  # your code here
    if st is None:
        st = "9"
    else:
        st = "9"+st
        st = answer(st)
    return st


def plus(st):  # your code here
    st = "+" + st
    return st


def minus(st):  # your code here
    st = "-" + st
    return st


def times(st):  # your code here
    st = "*" + st
    return st


def divided_by(st):  # your code here
    st = "/" + st
    return st


def answer(st):
    if "*" in st:
        st = int(st[0]) * int(st[2])
    elif "+" in st:
        st = int(st[0]) + int(st[2])
    elif "-" in st:
        st = int(st[0]) - int(st[2])
    elif "/" in st:
        st = int(st[0]) // int(st[2])
    return st


print(seven(times(five())))
print(five(minus(two())))
print(eight(minus(three())))
print(six(divided_by(two())))
print(eight(divided_by(three())))