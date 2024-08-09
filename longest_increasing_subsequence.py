# Write a function longest_increasing_subsequence(lst) that takes a list of integers lst as input and returns the length of the longest increasing subsequence.
# Use time complexity of O(n2) or better

def longest_increasing_subsequence(lst):
    # Write code here
    if not lst:
        return 0
    
    n = len(lst)
    dp = [1] * n  # Initialize the dp array with 1s
    
    for i in range(1, n):
        for j in range(i):
            if lst[i] > lst[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

print(longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80])) # 6
print(longest_increasing_subsequence([3, 4, -1, 0, 6, 2, 3])) # 4
print(longest_increasing_subsequence([1, 3, 2, 4, 6, 5, 8, 7, 9])) # 6
print(longest_increasing_subsequence([5, 4, 3, 2, 1])) # 1