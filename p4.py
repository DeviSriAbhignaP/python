class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i


nums = [3, 2, 4]
target = 6

sol = Solution()
result = sol.twoSum(nums, target)
print("Indices:", result)
