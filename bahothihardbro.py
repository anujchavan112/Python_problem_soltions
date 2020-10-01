a=[0,1,0,2,1,0,1,3,2,1,2,1]
k=[]
peaks = []
count = 0
for height in a:
    if not len(peaks) or len(peaks) == 1:
        peaks.append(count)

    else:
        while len(peaks) >= 2:
            if height >= a[peaks[-1]] and a[peaks[-2]] >= a[peaks[-1]]:
                peaks = peaks[:-1]
            else:
                break
        peaks.append(count)
    count += 1
water = 0
for i in range(len(peaks) - 1):
    for j in range(peaks[i] + 1, peaks[i + 1]):
        water += (min(a[peaks[i]], a[peaks[i + 1]]) - a[j])
print(water)

print(peaks)
