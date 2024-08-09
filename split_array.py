# Write a function named isSplitable that gets an array of integers and returns true if it's possible to split the array into two arrays where the sum of both of them is the same, otherwise false.
# Examples,

# [5, 2, 3]  ->  [5] and [2, 3]
# [2, 3]  ->  Not splitable

def isSplitable(arr):
    total_sum = sum(arr)
    
    # If total sum is odd, it's not possible to split into two equal parts
    if total_sum % 2 != 0:
        return False
    
    target_sum = total_sum // 2 # 5
    n = len(arr) # 3
    
    # DP array to store subproblem results
    dp = [False] * (target_sum + 1)
    dp[0] = True  # There is always a subset with sum 0 (empty subset)
    
    # Update the DP array
    for num in arr:
        # Iterate backwards from target_sum to num by preventing overcounting
        for j in range(target_sum, num - 1, -1):
            if dp[j - num]:
                dp[j] = True
    
    return dp[target_sum]


print(isSplitable([5, 2, 3]))  # Output: True (because [5] and [2, 3] have the same sum)
print(isSplitable([2, 3]))    # Output: False
print(isSplitable([5, 15, 4, 5]))
print(isSplitable([1, 2, 10, 3, 4]))


        