from buyukbul import buyukbul
from kucukbul import kucukbul
class Sayilar:
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    kucuk = kucukbul(a,b,c)
    buyuk = buyukbul(a,b,c)
    print("Küçük sayı:", kucuk, "\nBüyük sayı:", buyuk)
