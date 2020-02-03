def dz_24(a):
    if len(a) >= 10:
        print(a[0:6])
    else:
        print(a.ljust(12, "O"))

dz_24(input('Напишите слово: '))