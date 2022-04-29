import math as ma

dane = input()
liczby = dane.split(" ")
print(liczby)
n = int(liczby[0])
k = int(liczby[1])

if 0 <= k <= n:
    counting = ma.comb(n,k)
    print(counting)
elif k==1 and k==n:
    print("1")
elif k>n:
    print("0")
    