# Write a function named repeatedSubseq that gets a string s and returns a repeated subsequence  s if it exists, otherwise an empty string.
# A repeated subsequence must have 2 or more characters.
# For example,

# repeatedSubseq("XYBAXB")  ->  "XB" (XBXB)
# repeatedSubseq("BANAN")  ->  "AN" (ANAN)
# repeatedSubseq("XYZX")  ->  "" (None)
# repeatedSubseq("XYXYX")  ->  "XYX"
# Make sure to return the longest repeated subsequence!

def repeatedSubseq(s):
    def lcs(x, y, m, n, memo):
        if m == 0 or n == 0:
            return ""
        if (m, n) in memo:
            return memo[(m, n)]
        
        if x[m - 1] == y[n - 1] and m != n:
            result = lcs(x, y, m - 1, n - 1, memo) + x[m - 1]
        else:
            result = max(lcs(x, y, m, n - 1, memo), lcs(x, y, m - 1, n, memo), key=len)
        
        memo[(m, n)] = result
        return result
    
    memo = {}
    n = len(s)
    result = lcs(s, s, n, n, memo)
    
    return result if len(result) > 1 else ""

print(repeatedSubseq("XYBAXB"))  # -> "XB"
print(repeatedSubseq("BANAN"))   # -> "AN"
print(repeatedSubseq("XYZX"))    # -> ""
print(repeatedSubseq("XYXYX"))   # -> "XYX"
