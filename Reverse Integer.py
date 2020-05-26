class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = 0
        sign = 0
        if x<0:
            x = -x
            sign =1
        while x!=0:
            y = (y*10)+(x%10)
            x = x/10
        if y>(2**31-1):
            return 0
        else:
            if sign == 1:
                return -y
            else:
                return y