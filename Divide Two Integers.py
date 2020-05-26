class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend/divisor) > (2**31-1):
            return (2**31-1)
        else:
            if (dividend>=0 and divisor>0) or (dividend<0 and divisor<0):
                return dividend/divisor
            elif (dividend>=0 and divisor<0) or (dividend<0 and divisor>0):
                dividend = -dividend
                return -(dividend/divisor)