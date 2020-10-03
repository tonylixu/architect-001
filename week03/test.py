def dp_iterative(nums):
    if not nums: return 0
    if len(nums) == 1: return nums[0]

    def helper(nums, start, end):
        dp = [0] * (len(nums) + 2)
        print(f'nums={nums}, start={start}, end={end}')
        for i in range(end, start - 1, -1):
            print(i)
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])
        print(f'dp={dp}')
        return max(dp)

    return max(
        helper(nums, 0, len(nums) - 2),
        helper(nums, 1, len(nums) - 1))

n = [1, 2]

print(dp_iterative(n))