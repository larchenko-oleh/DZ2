def dz_32(x):
    return len(x)
list = ['123456','234','34567','12']
list.sort(key=dz_32)
print(list)