def parity(x):
    res=0
    while x:
        res ^=1
        x&=x-1
    return res
print(parity(101010101010112))
#parity is 1 if the number of 1 is odd
