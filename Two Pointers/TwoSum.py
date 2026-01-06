'''
We are given a sorted array of integers `numbers` and a target integer `target`.
return the indices that is equal to target.

input : numbers = [2,7,11,15], target = 9

return : [0, 1]

target = 18
return: [1, 2] => 7 + 11 = 18

def findIdx(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]

Time Complexity: O(n * n + 1 ) => O(n^2 + 1) => O(n^2)
Space Complexity: O(1)

def findIdx(arr, target):
    #two pointers:
    # one starting at the start of our array
    # another one starting at the end of our array
    left = 0
    right = len(arr) - 1

    #we want to loop until the two pointer meets or intersect

    while left < right:
        #variable that stores the current sum of our index
        currSum = arr[left] + arr[right]

        if currSum == target:
            return [left, right]
        elif currSum < target:
            right -= 1
        else:
            left += 1

    return []

'''

#Example 1: Given a string s, return true if it is a palindrome, false otherwise.

# Test cases
s1 = "banana"
s2 = "racecar"
s3 = "tattarrattat"
s4 = "toohottohoot"

#potential questions to ask:
#what is a palindrome? A word that reads the same forwards and backwards
#Can we assume all characters are lowercase? Yes
#Should we consider white spaces? No
#Do I need need to consider special characters? No


def isPalindrome(s: str) -> bool:
    #add code here
    #reading in the string value s
    #2 variables that point to the start and end of the string
    #left pointer is going to be starting at index 0
    #right pointer is going to be starting at array.length - 1
    #need to create a loop that starts at the beginning left++ and the end which would be right--
    #after looping from each side of the array, we would then need to compare at each character pointer index
    #if they are equal, proceed to next index
    #otherwise return true

    #s1 = "banana"  -> false
    #s2 = "racecar" -> true

    #String = immutable  - cannot be changed 
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        else:
            left+=1
            right-=1
    return True

#Time Complexity: O(n)
#Space Complexity: O(1) 
             

print(f"'{s1}' is palindrome: {isPalindrome(s1)}")
print(f"'{s2}' is palindrome: {isPalindrome(s2)}")
print(f"'{s3}' is palindrome: {isPalindrome(s3)}")
print(f"'{s4}' is palindrome: {isPalindrome(s4)}")