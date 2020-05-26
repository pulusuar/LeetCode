class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        open_braces = set(['[', '{', '('])
        closed_braces = { ')': '(', '}': '{', ']': '['}
        for e in s:
            if e in open_braces:
                stack.append(e)
            else:
                if not stack or stack.pop()!=closed_braces[e]:
                    return False
        if stack:
            return False
        return True
        
            