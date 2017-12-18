"""
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment which could only 
hold integers within the 32-bit signed integer range. For the
purpose of this problem, assume that your function
 returns 0 when the reversed integer overflows.

Example 1:

Input: -123
Output: -321

"""

class Solution:
    def reverse(self, x):
        isNeg = False
        if (x == 0):
            return 0
        intStr = str(x)
        if (intStr[0] == '-'):
            intStr = intStr[1:]
            isNeg = True
        intStr = intStr[::-1]
        if (isNeg):
            intStr = '-' + intStr
        revX = int(intStr)
        if (revX > 2**31 -1 or revX < -2**31):
            return 0
        return revX

"""
let n = length of characters in integer
time complexity: O(n) 
	reverse operation takes n (or n/2) iterations
space complexity: O(n)
	allocate n characters for the string

"""
