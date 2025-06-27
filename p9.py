class Solution(object):
    def partitionArray(self, nums, k):
        nums.sort()
        count = 1
        start = nums[0]

        for num in nums:
            if num - start > k:
                count += 1
                start = num

        return count

# Hardcoded input
nums = [1, 5, 6, 2, 8, 10]
k = 3

sol = Solution()
result = sol.partitionArray(nums, k)
print("Minimum number of partitions:", result)
