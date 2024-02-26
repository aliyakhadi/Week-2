# Abdelrhman Mohamed 11/314a

class Solution(object):
    def countKDifference(self, nums, k):
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)): 
                if abs(nums[i] - nums[j]) == k:
                    count += 1 
        
        return count
# this code has a time complexity O(n^2)
# the task was to make an algorithm which works at time O(n) 
