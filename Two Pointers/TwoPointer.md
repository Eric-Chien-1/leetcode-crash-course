# Two Pointers Algorithm

## What is the Two Pointers Technique?

The Two Pointers technique is an efficient algorithm pattern that uses two pointers (or indices) to traverse a data structure, typically an array or string. Instead of using nested loops, we strategically move two pointers to solve problems in a more optimal way.

The two pointers can move:
- **Opposite directions**: One pointer starts at the beginning, another at the end, and they move toward each other
- **Same direction**: Both pointers start at the beginning (or same position) and move forward at different speeds

## When to Use Two Pointers?

Use the Two Pointers technique when:

- ✅ Working with **sorted arrays** or strings
- ✅ You need to find **pairs or triplets** with specific properties
- ✅ Checking for **palindromes** or symmetry
- ✅ **Removing duplicates** from sorted arrays
- ✅ **Merging** sorted arrays
- ✅ Finding elements that satisfy certain **sum conditions**
- ✅ Optimizing from O(n²) brute force to O(n) time complexity

## Advantages

- **Time Efficiency**: Reduces O(n²) nested loops to O(n) linear time
- **Space Efficiency**: Usually O(1) space complexity (in-place operations)
- **Simple to Implement**: Clear and readable code logic

---

## Python Code Examples

### Example 1: Two Pointers from Opposite Ends (Two Sum - Sorted Array)

**Problem**: Given a sorted array of integers, find two numbers that add up to a specific target.

```python
def two_sum_sorted(numbers, target):
    """
    Find two numbers in a sorted array that sum to target.
    
    Time Complexity: O(n) - single pass through array
    Space Complexity: O(1) - only using two pointers
    
    Args:
        numbers: sorted list of integers
        target: target sum
    
    Returns:
        List of two indices [left, right] or empty list if not found
    """
    # Initialize two pointers
    left = 0                    # Start at the beginning
    right = len(numbers) - 1    # Start at the end
    
    # Move pointers toward each other
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        # Found the target sum
        if current_sum == target:
            return [left, right]
        
        # Sum is too small, move left pointer right to increase sum
        elif current_sum < target:
            left += 1
        
        # Sum is too large, move right pointer left to decrease sum
        else:
            right -= 1
    
    # No solution found
    return []

# Test cases
print(two_sum_sorted([2, 7, 11, 15], 9))   # Output: [0, 1]
print(two_sum_sorted([2, 7, 11, 15], 18))  # Output: [1, 2]
print(two_sum_sorted([1, 3, 5, 7, 9], 12)) # Output: [2, 4]
```

**Why it works**: Since the array is sorted, if the sum is too small, we need a larger number (move left pointer right). If the sum is too large, we need a smaller number (move right pointer left).

---

### Example 2: Two Pointers from Opposite Ends (Palindrome Check)

**Problem**: Check if a string is a palindrome (reads the same forwards and backwards).

```python
def is_palindrome(s):
    """
    Check if a string is a palindrome using two pointers.
    
    Time Complexity: O(n) - check each character once
    Space Complexity: O(1) - only using two pointers
    
    Args:
        s: input string
    
    Returns:
        True if palindrome, False otherwise
    """
    # Initialize pointers at opposite ends
    left = 0
    right = len(s) - 1
    
    # Compare characters while moving toward center
    while left < right:
        # If characters don't match, not a palindrome
        if s[left] != s[right]:
            return False
        
        # Move both pointers toward center
        left += 1
        right -= 1
    
    # All characters matched
    return True

# Test cases
print(is_palindrome("racecar"))        # Output: True
print(is_palindrome("banana"))         # Output: False
print(is_palindrome("tattarrattat"))   # Output: True
print(is_palindrome("a"))              # Output: True
print(is_palindrome("ab"))             # Output: False
```

**Why it works**: A palindrome has symmetry - characters at equal distances from the ends must match. We check from outside moving in.

---

### Example 3: Two Pointers in Same Direction (Remove Duplicates)

**Problem**: Remove duplicates from a sorted array in-place, returning the new length.

```python
def remove_duplicates(nums):
    """
    Remove duplicates from sorted array in-place.
    
    Time Complexity: O(n) - single pass through array
    Space Complexity: O(1) - modifying array in-place
    
    Args:
        nums: sorted list with possible duplicates
    
    Returns:
        Length of array after removing duplicates
    """
    # Edge case: empty array
    if not nums:
        return 0
    
    # Slow pointer tracks position of unique elements
    slow = 0
    
    # Fast pointer explores the array
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            # Found a new unique element
            slow += 1                    # Move slow pointer
            nums[slow] = nums[fast]      # Place unique element
    
    # Length is slow index + 1
    return slow + 1

# Test cases
arr1 = [1, 1, 2, 2, 3, 4, 4, 5]
length1 = remove_duplicates(arr1)
print(f"New length: {length1}, Array: {arr1[:length1]}")
# Output: New length: 5, Array: [1, 2, 3, 4, 5]

arr2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
length2 = remove_duplicates(arr2)
print(f"New length: {length2}, Array: {arr2[:length2]}")
# Output: New length: 5, Array: [0, 1, 2, 3, 4]
```

**Why it works**: The slow pointer marks where to place the next unique element. The fast pointer scans ahead to find new unique elements. Since the array is sorted, duplicates are adjacent.

---

## Two Pointers on Two Arrays

When working with **two separate arrays**, we can use one pointer for each array to efficiently solve problems that involve comparing, merging, or finding relationships between them. This pattern is especially powerful when both arrays are sorted.

### When to Use Two Pointers on Two Arrays?

Use this pattern when:
- ✅ **Merging** two sorted arrays into one
- ✅ Finding **common elements** or **intersection** between two sorted arrays
- ✅ Comparing elements from two arrays simultaneously
- ✅ Finding **differences** between two sorted sequences
- ✅ Processing two arrays in **synchronized order**

### Key Characteristics:
- Each array has its own pointer
- Pointers move independently based on comparison logic
- Usually requires both arrays to be sorted (but not always)
- Time complexity is typically O(m + n) where m and n are array lengths

---

### Example 4: Merge Two Sorted Arrays

**Problem**: Given two sorted arrays, merge them into the first array in sorted order.

```python
def merge_sorted_arrays(nums1, m, nums2, n):
    """
    Merge two sorted arrays into nums1.
    nums1 has enough space (size m+n) to hold all elements.
    
    Time Complexity: O(m + n) - visit each element once
    Space Complexity: O(1) - merge in-place (or O(m+n) if creating new array)
    
    Args:
        nums1: first sorted array with extra space
        m: number of valid elements in nums1
        nums2: second sorted array
        n: number of elements in nums2
    
    Returns:
        None - modifies nums1 in-place
    """
    # Start from the end to avoid overwriting elements
    p1 = m - 1      # Pointer for last element in nums1
    p2 = n - 1      # Pointer for last element in nums2
    p = m + n - 1   # Pointer for last position in merged array
    
    # Merge from back to front
    while p1 >= 0 and p2 >= 0:
        # Compare elements and place larger one at the end
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    # If nums2 still has elements, copy them
    # (no need to copy nums1 elements as they're already in place)
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

# Test cases
arr1 = [1, 3, 5, 0, 0, 0]
arr2 = [2, 4, 6]
merge_sorted_arrays(arr1, 3, arr2, 3)
print(f"Merged array: {arr1}")
# Output: Merged array: [1, 2, 3, 4, 5, 6]

arr3 = [4, 5, 6, 0, 0, 0]
arr4 = [1, 2, 3]
merge_sorted_arrays(arr3, 3, arr4, 3)
print(f"Merged array: {arr3}")
# Output: Merged array: [1, 2, 3, 4, 5, 6]
```

**Why it works**: By merging from back to front, we avoid overwriting elements in nums1 that we haven't processed yet. We compare elements from both arrays and place the larger one at the current position.

---

### Example 5: Find Common Elements in Two Sorted Arrays

**Problem**: Given two sorted arrays, return an array of elements that appear in both arrays.

```python
def find_common_elements(nums1, nums2):
    """
    Find all common elements between two sorted arrays.
    
    Time Complexity: O(m + n) - single pass through both arrays
    Space Complexity: O(min(m, n)) - for storing common elements
    
    Args:
        nums1: first sorted array
        nums2: second sorted array
    
    Returns:
        List of common elements (without duplicates)
    """
    result = []
    p1 = 0  # Pointer for nums1
    p2 = 0  # Pointer for nums2
    
    # Traverse both arrays simultaneously
    while p1 < len(nums1) and p2 < len(nums2):
        # Skip duplicates in nums1
        if p1 > 0 and nums1[p1] == nums1[p1 - 1]:
            p1 += 1
            continue
        
        # Skip duplicates in nums2
        if p2 > 0 and nums2[p2] == nums2[p2 - 1]:
            p2 += 1
            continue
        
        # Found a common element
        if nums1[p1] == nums2[p2]:
            result.append(nums1[p1])
            p1 += 1
            p2 += 1
        # nums1 element is smaller, move its pointer
        elif nums1[p1] < nums2[p2]:
            p1 += 1
        # nums2 element is smaller, move its pointer
        else:
            p2 += 1
    
    return result

# Test cases
print(find_common_elements([1, 2, 2, 3, 4], [2, 2, 3, 5]))
# Output: [2, 3]

print(find_common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
# Output: [3, 4, 5]

print(find_common_elements([1, 3, 5, 7], [2, 4, 6, 8]))
# Output: []
```

**Why it works**: Since both arrays are sorted, we can advance pointers based on which element is smaller. When elements match, we found a common element. We skip duplicates to ensure each common element appears only once in the result.

---

### Example 6: Intersection of Two Sorted Arrays

**Problem**: Given two sorted arrays, return the intersection (elements that appear in both), allowing duplicates based on frequency.

```python
def intersection_with_duplicates(nums1, nums2):
    """
    Find intersection of two sorted arrays, including duplicates.
    Each element appears as many times as it shows in both arrays.
    
    Time Complexity: O(m + n) - single pass through both arrays
    Space Complexity: O(min(m, n)) - for storing intersection
    
    Args:
        nums1: first sorted array
        nums2: second sorted array
    
    Returns:
        List of intersection elements (with duplicates)
    """
    result = []
    p1 = 0  # Pointer for nums1
    p2 = 0  # Pointer for nums2
    
    # Traverse both arrays
    while p1 < len(nums1) and p2 < len(nums2):
        # Found matching elements
        if nums1[p1] == nums2[p2]:
            result.append(nums1[p1])
            p1 += 1
            p2 += 1
        # nums1 element is smaller, advance p1
        elif nums1[p1] < nums2[p2]:
            p1 += 1
        # nums2 element is smaller, advance p2
        else:
            p2 += 1
    
    return result

# Test cases
print(intersection_with_duplicates([1, 2, 2, 3, 4], [2, 2, 3, 5]))
# Output: [2, 2, 3]

print(intersection_with_duplicates([1, 1, 2, 2], [2, 2, 3, 3]))
# Output: [2, 2]

print(intersection_with_duplicates([1, 2, 3], [4, 5, 6]))
# Output: []
```

**Why it works**: Both pointers advance together when elements match, capturing all duplicate occurrences. When elements don't match, we advance the pointer pointing to the smaller element to potentially find a match.

---

### Pattern 3: Two Arrays (One Pointer Each)

```python
# General template for two arrays
p1 = 0  # Pointer for first array
p2 = 0  # Pointer for second array

while p1 < len(array1) and p2 < len(array2):
    if array1[p1] meets_condition array2[p2]:
        # Process matching elements
        p1 += 1
        p2 += 1
    elif array1[p1] < array2[p2]:
        # First array element is smaller
        p1 += 1
    else:
        # Second array element is smaller
        p2 += 1

# Process remaining elements if needed
while p1 < len(array1):
    # Handle remaining elements in array1
    p1 += 1

while p2 < len(array2):
    # Handle remaining elements in array2
    p2 += 1
```

### Complexity Analysis for Two Arrays Pattern

| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| **Merge Two Arrays** | O(m + n) | O(1) or O(m+n) | O(1) if merging in-place, O(m+n) for new array |
| **Find Intersection** | O(m + n) | O(min(m, n)) | Need to store common elements |
| **Find Common Elements** | O(m + n) | O(min(m, n)) | Similar to intersection |

**Why O(m + n)?** Each pointer traverses its respective array at most once. Even though we have two pointers, they move independently through different arrays, so we visit each element exactly once.

---

## Time and Space Complexity

### Typical Complexities:

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| **Two Pointers (Opposite)** | O(n) | O(1) | Single pass, pointers meet in middle |
| **Two Pointers (Same Dir)** | O(n) | O(1) | One or both pointers traverse once |
| **Brute Force (Nested Loops)** | O(n²) | O(1) | Two Pointers is much more efficient |

### Why O(n)?
Even though we have two pointers, each element is visited at most once. The pointers collectively make a single pass through the data structure.

---

## Common Patterns Summary

### Pattern 1: Opposite Direction (Converging)
**Use for**: Palindromes, Two Sum in sorted arrays, Container with Most Water
```python
left = 0
right = len(array) - 1

while left < right:
    # Process elements at left and right
    # Move pointers based on condition
    left += 1  # or
    right -= 1
```

### Pattern 2: Same Direction (Fast and Slow)
**Use for**: Remove duplicates, Remove elements, Partition arrays
```python
slow = 0

for fast in range(len(array)):
    # Fast pointer explores
    # Slow pointer tracks valid position
    if condition:
        slow += 1
```

### Pattern 3: Two Arrays (One Pointer Each)
**Use for**: Merge sorted arrays, Find intersection, Compare two sequences
```python
p1, p2 = 0, 0

while p1 < len(array1) and p2 < len(array2):
    # Compare elements from both arrays
    # Move pointers based on comparison
    if array1[p1] == array2[p2]:
        # Process match
        p1 += 1
        p2 += 1
    elif array1[p1] < array2[p2]:
        p1 += 1
    else:
        p2 += 1
```

---

## Tips for Success

1. **Identify if array/string is sorted** - Many Two Pointers problems involve sorted data (for search/sum operations), but the technique also works on unsorted data (e.g., cycle detection, sliding window)
2. **Determine pointer direction** - Opposite or same direction based on problem
3. **Define pointer movement logic** - When and how to move each pointer
4. **Handle edge cases** - Empty arrays, single elements, no solution found
5. **Watch for infinite loops** - Ensure pointers always make progress

---

## Practice Problems

Great LeetCode problems to practice Two Pointers:

**Single Array Problems:**
- **Two Sum II** (Sorted Array) - Easy
- **Valid Palindrome** - Easy  
- **Remove Duplicates from Sorted Array** - Easy
- **Container With Most Water** - Medium
- **3Sum** - Medium
- **Trapping Rain Water** - Hard

**Two Arrays Problems:**
- **Merge Sorted Array** - Easy
- **Intersection of Two Arrays** - Easy
- **Intersection of Two Arrays II** - Easy
- **Squares of a Sorted Array** - Easy
- **Merge Two Sorted Lists** - Easy
- **Find Median of Two Sorted Arrays** - Hard

---

## Summary

The Two Pointers technique is a powerful optimization tool that can:
- Reduce time complexity from O(n²) to O(n)
- Work efficiently with sorted data
- Solve problems in-place with O(1) space
- Handle multiple arrays with O(m + n) time complexity

Master this technique by recognizing when problems involve:
- Searching pairs in sorted arrays
- Checking symmetry (palindromes)
- In-place array modifications
- **Merging or combining two arrays**
- **Finding intersections or common elements**
- Partitioning operations
