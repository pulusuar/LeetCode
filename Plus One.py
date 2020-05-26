class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        sol = []
        for i in range(0, len(digits)):
            num = (num*10) + digits[i]
        num += 1
        
        while num!=0:
            sol.append(num%10)
            num = num/10
        return sol[::-1]