a=[1,2,3,4,5]
n=len(a)
k=4
l=[]
for _ in range(0,k):
    for i in (0,n-1):
        a[i],a[i+1]=a[i+1],a[i]
print(a)
