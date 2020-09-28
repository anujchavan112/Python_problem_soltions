def move(f,t):
    print("move disc from {} to {} ".format(f,t))
def movevia(f,v,t):
    move(f,v)
    move(v,t)
def hanoi(n,f,h,t):
    if n==0:
        pass
    else:

        hanoi(n-1,f,t,h)
        move(f,t)
        hanoi(n-1,h,f,t)

print(hanoi(5,'a','b','c'))
