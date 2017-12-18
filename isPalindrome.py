"""
Determine whether an integer is a palindrome. Do this without extra space.

"""
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x == 0):
            return True
        if (x < 0):
            return False
        else:
            xStr = str(x)
        if (xStr == xStr[::-1]):
            return True
        else:
            return False
