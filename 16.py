def dz_16(a, b):
    if len(a) > len(b) == True:
        print(a*(len(a)-len(b)))
    else:
        print(b*(len(b)-len(a)))

dz_16(a = 'hello', b = 'helloworld')