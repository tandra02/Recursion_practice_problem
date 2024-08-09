# Write a function named test that gets a string s and a pattern p and returns true if the pattern matches the string, otherwise false.
# The pattern can contain letters, numbers, white spaces and the following wildcards,

# * - match any sequence of letters, numbers and white spaces.
# . - match exactly one letter, number or white space.
# ? - optionally match any sequence of letters, numbers and white spaces.
# Examples,

# test("My name is Jake", "My name is *")  ->  true
# test("My name is Jake", "Your name is *")  ->  false
# test("Maximum", "M..imum")  ->  true 
# test("Mimum", "M?imum")  ->  true 
# test("Minimum", "K?imum")  ->  false 
# The pattern must match all the string, not partial substring!

def test(s, p):
    if len(s) == 0 and len(p) == 0:
        return True
    if len(s) == 0 or len(p) == 0:
        return False

    next_p = p[0]
    next_s = s[0]

    if next_p == '.':
        return test(s[1:], p[1:])
    elif next_p == '*':
        return test(s[1:], p[1:]) or test(s[1:], p)
    elif next_p == '?':
        return test(s[1:], p[1:]) or test(s[1:], p) or test(s, p[1:])
    elif next_p == next_s:
        return test(s[1:], p[1:])
    else:
        return False

# Examples
print(test("My name is Jake", "My name is *"))  # true
print(test("My name is Jake", "Your name is *"))  # false
print(test("Maximum", "M..imum"))  # true
print(test("Mimum", "M?imum"))  # true
print(test("Minimum", "K?imum"))  # false