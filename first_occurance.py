# Write a function named findIndex that gets a string s and character c and returns the index of the first occurrence of c in s, if it does not exist, return -1.
# Example:

# test, s -> 2 Because character s appears first time at index 2

def findIndex(s, c):
    # Write code here
    for i in range(len(s)):
        if s[i] == c:
            return i
    return -1
    
print(findIndex('test', 's'))
print(findIndex('tandra', 'f'))
print(findIndex('example', 'p'))