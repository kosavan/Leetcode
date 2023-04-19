class Solution(object):
    def twoSum(self, nums, target):
      for num1 in range(len(nums)):
        for num2 in range(len(nums)):
          if (nums[num1] + nums[num2] == target) & (num1 != num2):
            return [num1, num2]
