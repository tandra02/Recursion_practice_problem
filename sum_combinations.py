# Write a function named printCombinations that gets an integer num and prints all the possible combinations of numbers from 1 to n having sum n.
# Make sure to print the combinations in specific order and way, check the test cases!
# The printing can be done in a recursive way, if it's not happening in the main recursive function.

def printCombinations(num):
    res = printCombinationsHelper(num)
    for i in res:
        print(' '.join([str(x) for x in i]))

def printCombinationsHelper(num):
    if num == 0:
        return []
    res = []
    for i in range(num):
        a = [num - i]
        a_res = printCombinationsHelper(i)
        for t in a_res:
            res.append(a + t)
        if len(a_res) == 0:
            res.append(a)
    return res

printCombinations(1)
printCombinations(2)
printCombinations(3)
printCombinations(4)
printCombinations(5)