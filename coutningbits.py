def countbits(x):
    sum=0
    while x:
        sum+= x & 1
        x>>=1
    return sum
print(countbits(214))
