def evenod(A):

    next_even,next_odd=0,len(A)-1
    while next_even< next_odd:
        if A[next_even]%2==0:
            next_even +=1
        else:
            next_even,next_odd=next_odd,next_even
            next_odd-=1

print(evenod([2,6,4,5,9,44]))
