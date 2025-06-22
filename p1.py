class Solution(object):
    def divideString(self, s, k, fill):
        s == "abcdefghi"
        k == 3
        fill == "x"
        n = len(s)
        groups = (n + k - 1) // k
        result = []

        for i in range(groups):
            group = ''
            for j in range(k):
                index = i * k + j
                if index < n:
                    group += s[index]
                else:
                    group += fill  # Padding
            result.append(group)

        return result
s = input("Enter the string: ")
k = int(input("Enter the group size (k): "))
fill = input("Enter the fill character: ")


sol = Solution()
result = sol.divideString(s, k, fill)

print("Result:", result)
