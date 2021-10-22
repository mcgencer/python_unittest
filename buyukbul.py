def buyukbul(a, b, c):
    enbuyuk = None
    if (a > b):
        if (a > c):
            enbuyuk = a
        else:
            enbuyuk = c
    else:
        if (b > c):
            enbuyuk = b
        else:
            enbuyuk = c

    return enbuyuk
