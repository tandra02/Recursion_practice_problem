# The knapsack problem is a famous problem.
# In this problem, you have a knapsack that has a predefined weight it can take and items where each item has a weight and a value.
# Your task is to take as much value in the bounds of the knapsack weight. 

# For example,

# values - [20, 5, 40, 10, 15]

# weights - [1, 2, 8, 3, 7]

# Weight of knapsack - 10


# The solution is to take the items with the weights 1 and 8 and the values 20 and 40.
# The max value is 60, and the total weight is 9 (which is smaller or equals 10 meaning that it is a valid weight).
# Write a function named knapsack that gets an integer W and two arrays of integers values and weights and returns the solution for the knapsack problem using the input values (the maximum value the knapsack can take).

def knapsack(W, values, weights):
    # Number of items.
    n = len(values)
    dp = [0] * (W + 1)

    for i in range(n):
        # Iterate backwards through the dp array from W down to weights[i]
        for w in range(W, weights[i] - 1, -1):
            # Update dp[w] to be the maximum of its current value (dp[w]) 
            # and the value of adding the current item (values[i]) to the best value achievable with the remaining capacity (dp[w - weights[i]]).
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    return dp[W]


print(knapsack(10, [20, 5, 10, 40, 15, 25], [1, 2, 3, 8, 7, 4]))
print(knapsack(5, [3, 3, 2, 2, 3, 4, 3], [1, 1, 1, 1, 1, 1, 1]))