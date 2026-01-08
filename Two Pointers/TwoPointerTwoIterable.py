'''
Move along both inputs simultaneously until all elements have been checked.

Create two pointers, one for each iterable. Each pointer should start at the first index.
Use a while loop until one of the pointers reaches the end of its iterable.
At each iteration of the loop, move the pointers forward. This means incrementing either one of the pointers or both of the pointers. 
Deciding which pointers to move will depend on the problem we are trying to solve.
Because our while loop will stop when one of the pointers reaches the end, the other pointer will not be at the end of its respective iterable when the loop finishes. 
Sometimes, we need to iterate through all elements - if this is the case, you will need to write extra code here to make sure both iterables are exhausted.


function fn(arr1, arr2):
    i = j = 0
    while i < arr1.length AND j < arr2.length:
        Do some logic here depending on the problem
        Do some more logic here to decide on one of the following:
            1. i++
            2. j++
            3. Both i++ and j++

    // Step 4: make sure both iterables are exhausted
    // Note that only one of these loops would run
    while i < arr1.length:
        Do some logic here depending on the problem
        i++

    while j < arr2.length:
        Do some logic here depending on the problem
        j++
'''

#: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.

#arr1 = [1, 4, 7, 20]    arr2 = [3, 5, 6]
#output = [1,3,4,5,6,7,20]



# res = []
# i = 0
# i starting at 0 for arr1 => 1

# j = 0
# j starting at 0 for arr2 => 3

#while i < len(arr1) and j < len(arr2):
#    if arr1[i] < arr2[j]:
#        res.append(arr1[i])
#        i += 1
#
#    if arr1[i] > arr2[j]:
#        res.append(arr2[j])
#        j += 1

#while i < len(arr1):
#    res.append(arr1[i])
#    i += 1

# while j < len(arr2):
#     res.append(arr2[j])
#     j += 1

# return res

#arr1 = [1,2] arr2= [3,75,100]
#output = [1,2,3,75,100]

# def mergeSortedArrays(arr1, arr2):
#     i = 0
#     j = 0
#     res = []

#     #i goes through arr1 and j goes through arr2
#     while i < len(arr1) and j < len(arr2):
#         #if arr1[i] is less than arr2[j]
#         if arr1[i] < arr2[j]:
#             res.append(arr1[i])
#             i += 1
#         else:
#             res.append(arr2[j])
#             j += 1

#     #exhaust remaining elements in arr1 and arr2
#     while i < len(arr1):
#         res.append(arr1[i])
#         i += 1
    
#     while j < len(arr2):
#         res.append(arr2[j])
#         j += 1
    
#     return res

#Time complexity: O(n + m + n + m) => O(2n + 2m) => O 2(n + m) => O(n + m) => O(n)
#Space Complexity: O(n)

# print(mergeSortedArrays([1,4,7,20], [3,5,6])) #[1,3,4,5,6,7,20]


'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a sequence of characters that can be obtained by deleting some (or none) of the characters from the original string,
while maintaining the relative order of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not.

s = "abc", t = "ahbgdc"
output = true

s = "axc", t = "ahbgdc"
output = false
'''

def isSubsequence(s: str, t: str) -> bool:
    #i be the s index of the beginning
    i = 0
    #j be the t index of the beginning
    j = 0
    
    #while the i of the length of the string s and j goes through the t string
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i+=1
        else:
            j+=1
    return i == len(s) 

print(isSubsequence("abc", "ahbgdc")) 
print(isSubsequence("axc", "ahbgdc"))