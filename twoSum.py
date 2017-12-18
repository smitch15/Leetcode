class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
		 """
        hm = {}
        retList = []
        for i in range(len(nums)):
            complement = target - nums[i]
            if (complement in hm):
                if (hm[complement] != i):
                    retList.append(i)
                    retList.append(hm[complement])
                    return retList
            hm[nums[i]] = i
