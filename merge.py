# Write a function named merge that gets two sorted arrays of integers and returns a merged array of the two, sorted.
# Examples:

# [1,5,7], [2, 6, 9] -> [1, 2, 5, 6, 7, 9]
# [-1, 5], [0, 9] -> [-1, 0, 5, 9]


def merge(a1, a2):
    if not a1:
        return a2
    if not a2:
        return a1

    if a1[0] < a2[0]:
        return [a1[0]] + merge(a1[1:], a2)
    else:
        return [a2[0]] + merge(a1, a2[1:])


print(merge([1, 5, 7], [2, 6, 9]))  # Output: [1, 2, 5, 6, 7, 9]
print(merge([-1, 5], [0, 9]))       # Output: [-1, 0, 5, 9]