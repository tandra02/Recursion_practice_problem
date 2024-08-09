# Write a function named lcp that gets an array of strings and returns the longest common prefix.
# For example,

# ["somehow", "somewhat", "something", "some"]  ->  "some"
# ["maximum", "minimum"]  ->  "m"
# ["llo", "lloon"]  ->  "llo"


def lcp(strs):
    # If the string is empty
    if not strs:
        # Return nothing
        return ""

    min_length = min(len(s) for s in strs)

    for i in range(min_length):
        # First element first letter
        char = strs[0][i]
        # Iterating over 2nd to rest of the elements of the list
        for s in strs[1:]:
            if s[i] != char:
                # Return 0 to ith - 1 letters
                return strs[0][:i]

    return strs[0][:min_length]


print(lcp(["somehow", "somewhat", "something", "some"]))  # Output: "some"
print(lcp(["maximum", "minimum"]))  # Output: "m"
print(lcp(["llo", "lloon"]))  # Output: "llo"
