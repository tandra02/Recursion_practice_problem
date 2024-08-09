# Write a function named isInterleaving that gets 3 strings s1, s2, s3 and returns true if s1 is interleaving of s2 and s3.
# s1 is interleaving by s2 and s3 if it is formed by all the characters from s2 and s3 and the order of characters is preserved.

# Examples,

# isInterleaving("ACDB", "AB", "CD")  ->  true
# isInterleaving("ACDB", "A", "CD")  ->  false
# isInterleaving("123456", "136", "245")  ->  true

def isInterleaving(s1, s2, s3):
    # Write code here
    # Base case: if all strings are empty, return true
    if not s1 and not s2 and not s3:
        return True

    # If s1 is empty but s2 or s3 are not, return false
    if not s1:
        return False

    # Check if the first character of s1 matches the first character of s2
    match_s2 = (len(s2) > 0 and s1[0] == s2[0]) and isInterleaving(s1[1:], s2[1:], s3)
    
    # Check if the first character of s1 matches the first character of s3
    match_s3 = (len(s3) > 0 and s1[0] == s3[0]) and isInterleaving(s1[1:], s2, s3[1:])
    
    # Return true if either of the above matches is true
    return match_s2 or match_s3

print(isInterleaving("ACDB", "AB", "CD"))  # True
print(isInterleaving("ACDB", "A", "CD"))  # False
print(isInterleaving("123456", "136", "245"))  # True