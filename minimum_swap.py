# Write a function named minFind that gets an integer num and an integer k and returns the smallest number that can be generated after at most k swaps.
# Examples,

# minFind(3421, 1)  ->  1423 (1 - 3)
# minFind(3421, 2)  ->  1243 (1 - 3, 2 - 4)
# minFind(4231, 2)  ->  1234 (Minimum number after 1 swap)


def minFind(num, k):
    # Base case
    if k == 0:
        # No more swaps are allowed
        return num
    
    s = str(num)
    # Initializes a minimum value
    m = num
    # Iterates over the string and choose the first digit to swap
    for i in range(len(s)):
        # Choose the second digit to swap with the first one
        for j in range(i + 1, len(s)):
            # Create a copy of the string 's', keeping the original string unchanged
            t = s
            t = t[:i] + t[j] + t[i+1:j] + t[i] + t[j+1:]
            m = min(m, minFind(int(t), k - 1))
    return m


print(minFind(3421,2))       # 1243
print(minFind(2134532, 3))   # 1223534
print(minFind(4351231, 2))   # 1153234
print(minFind(123, 3))       # 123
print(minFind(274391, 3))    # 123497