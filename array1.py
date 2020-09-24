RED, WHITE, BLUE = range(3)
def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        for j in reversed(range(i)):
            if A[j]> pivot:
                A[i], A[j] = A[j], A[i]
                break
    return A
A=[1,2,3,4,5,6,7,8,9,8,7,4,5,6,1,2,3]
print(dutch_flag_partition(6,A))
