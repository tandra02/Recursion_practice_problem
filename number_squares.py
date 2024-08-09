# Write a function named squareNum that gets an integer n and returns the minimum number of squares that sums to n.
# Examples,

# n=9  ->  9 = 32  ->  1
# n=10  ->  10=32+12  ->  2
# n=63  ->  63=72+32+22+12  ->  4

def squareNum(n):
    # Write code here
    dp = [n] * (n + 1)
    dp[0] = 0

    for target in range(1, n + 1):
        for s in range(1, target + 1):
            square = s * s
            if target - square < 0:
                break
            dp[target] = min(dp[target], 1 + dp[target-square])
    return dp[n]

print(squareNum(int(input())))