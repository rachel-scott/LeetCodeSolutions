class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        myList = [0,0]
        i = 0
        while i < length:
            j = i + 1
            while j < length:
                if ((nums[i] + nums[j]) == target):
                    myList[0] = i
                    myList[1] = j
                    return myList
                j = j+1
            i = i + 1
