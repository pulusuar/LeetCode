class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = s.strip().split(" ");
        last = t[len(t)-1]
        return len(last)