def kucukbul(a, b, c):
    enkucuk = None
    if (a < b):
        if (a < c):
            enkucuk = a
        else:
            enkucuk = c
    else:
        if (b < c):
            enkucuk = b
        else:
            enkucuk = c

    return enkucuk
