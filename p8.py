class Solution(object):
    def divideArray(self, nums, k):
        nums.sort()
        result = []
        for i in range(0, len(nums), 3):
            group = nums[i:i+3]
            if len(group) == 3 and group[2] - group[0] <= k:
                result.append(group)
            else:
                return []
        return result


nums = [3, 6, 9, 1, 2, 4]
k = 3

sol = Solution()
output = sol.divideArray(nums, k)
print("Output groups:", output)
