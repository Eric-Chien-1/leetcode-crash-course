#remove duplicate from arrray

#input = [1,1,2]  => output = [1,2]
#input = [0,0,1,1,1,2,2,3,3,4] => output = [0,1,2,3,4]
#input = [1,2,3,4,5] => output = [1,2,3,4,5]
'''
#brute force approach
def removeDuplicates(nums) -> list[int]:
    for i in range(len(nums) - 1, -1, -1):
        for j in range(len(nums) - 1, i, -1):
            if nums[i] == nums[j]:
                nums.pop(j)
    
    return nums


#fast and slow pointer approach

We have a pointer called left starting at idx 0 
We have another pointer called right starting at idx 1
if we find a duplicate, we move slow to right by swapping and right move up by 1.

Since the pointer is moving at the same time it will be O(n) time complexity

input = [0,0,1,1,1,2,2,3,3,4]
                   L     R

def remove_Duplicates(nums) -> list[int]:
    #edge case 
    if not nums:
        return 0

    #left pointer starting at 0 
    left = 0

    #right pointer continuously moves forward
    for right in range(1, len(nums)):

        #keep moving if we don't find a duplicate
        if nums[right] != nums[left]:
            #left pointer moves up by 1
            left += 1
            #swap the value at left with right
            nums[left] = nums[right]
        
        nums.append(nums[right])
         #slice the array to return unique values by removing the left pointer which points to the last unique value
    return nums[:left + 1]

#print(remove_Duplicates([0,0,1,1,1,2,2,3,3,4]))

'''


#Let's say you are given an array of 0's and 1's, swap the 0's to the left side and 1's to the right side of the array
#input = [0,1,0,1,1,0,0,1] => output = [0,0,0,0,1,1,1,1]
#input = [0,1,1,0,0] => output = [0,0,0,1,1]

def sortBinaryArray(nums) -> None:
    #left pointer to start at the beginning
    #right pointer to read the length of the array also
    #iterate through the array to see if the left pointer and the right pointer are equal to one another (while loop)
    #if the values are the same for the left and right value in the list, return 0
    #else if, return the value of 1
    #return the array values

    #left pointer starts at the first index of list
    #right pointer starts at the last index of list
    #start iiterating the list by checking the indexs if they are equal to Left = 0 and right = 1
    #if Left does not equal 0 and right does not equal 1 then we perform a switch
    #after the switch we move the left pointer to the right and we move the right pointer to the left
    #if the left does equal 0 but the right equals 1 then we move the right pointer to the left until we find a 0 and perform the switch
    #vise versa for the other side
    #the iteration end when the left and right pointer intersects 

    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] == 0:
            left += 1
        elif nums[right] == 1:
            right -= 1
        else:
            temp = nums[left] 
            nums[left] = nums[right] 
            nums[right] = temp
            left += 1
            right -= 1

    for i in range(len(nums)):
        print(nums[i])
            

sortBinaryArray([0,1,0,1,1,0,0,1]) #output = [0,0,0,0,1,1,1,1]   