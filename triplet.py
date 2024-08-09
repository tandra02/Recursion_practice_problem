# Write a function named isTripletExists that gets an array of integers arr and an integer k and returns true if there is a triplet of numbers (3 numbers) which sum to k else return false.
# Example,

# isTripletExists([2, 7, 4, 3], 9)  ->  true (The triplet {2, 4, 3})

def isTripletExists(arr, k):
    # Write code here
    arr.sort()
    n = len(arr)
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == k:
                return True
            elif current_sum < k:
                left += 1
            else:
                right -= 1
    return False

print(isTripletExists([1, 2, 3, 4], 9))
print(isTripletExists([2, 7, 4, 3], 9))
print(isTripletExists([1, 5, 2, 0, 3, 1, 4], 13))
print(isTripletExists([1, 5, 2, 0, 3, 1, 4], 6))