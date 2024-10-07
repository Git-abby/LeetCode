# 1. Two Sum
# Easy
# Topics
# Companies
# Hint
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}

        # Loop through the list by index and value using enumerate
        for i, num in enumerate(nums):
            complement = target - num

            # Check if the complement is already in the dictionary
            if complement in num_map:
                return [num_map[complement], i]

            # Store the current number with its index
            num_map[num] = i

        return []

# Example usage:
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
print(solution.twoSum(nums, target))
