def reverse (x) :
    result, xremaining = 0, abs(x)
    while xremaining:
        result = result * 10 + xremaining % 10
        xremaining //= 10
    return -result if x < 0 else result
print(reverse(1234))
print(int)
python3:

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = 0
        if x > 0:
            flag = 1
        else:
            flag = -1
        x = str(abs(x))
        s = int(x[::-1])
        if s <= 2**31-1:
            return flag*s
        else:
            return 0
