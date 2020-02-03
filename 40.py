import random

def dz_40(number, length):
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    number = int(number)
    length = int(length)
    for n in range(number):
        password =''
        for i in range(length):
            password += random.choice(chars)
        print(password)

dz_40(2, 15)