"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ret = 0
    for i in range(len(nums)):
        ret = ret ^ nums[i]
    return ret
    """
    XOR is a commutative operation so: 
    1^5^6^5^1 == 1^1 ^ 5^5 ^6 == 0^0^6 == 6
    """


def main():
	print(singleNumber([1, 5, 6, 5, 1]))

main()