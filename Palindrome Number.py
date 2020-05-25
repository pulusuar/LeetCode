class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        elif x == 0:
            return True
        else:
            y = str(x)
            z = y[::-1]
            return y==z