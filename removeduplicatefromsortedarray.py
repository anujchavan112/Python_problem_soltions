a=[1,1,2,2,3,3]

k=[]
for i in a:
    if i not in k:
        k.append(i)
print(k)
print(len(a))
