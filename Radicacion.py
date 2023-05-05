def radicacion(a,b):
    if b == 0:
        return None
    elif a == 0:
        return 0
    elif b == 1:
        return a
    else:
            return a**(1/b)
