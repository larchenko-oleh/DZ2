def my_str(x, w):
    a = 'wxyz'
    if a.index(x) < a.index(w):
        print("x встречается раньше")
    elif a.index(w) < a.index(x):
        print("w встречается раньше")

my_str('x', 'w')