import random
def estimate_pi(n):
    num_pnt_circle=0
    num_pnt_total=0
    for _ in range(n):
        x=random.uniform(0,1)
        y=random.uniform(0,1)
        dist=x**2+y**2
        if dist<1:
            num_pnt_circle+=1
        num_pnt_total +=1
    return 4*num_pnt_circle/num_pnt_total
print(estimate_pi(10000000))
