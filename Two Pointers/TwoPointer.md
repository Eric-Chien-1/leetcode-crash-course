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

## Common Patterns

### Pattern 1: Opposite Direction (Converging)
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
```python
slow = 0

for fast in range(len(array)):
    # Fast pointer explores
    # Slow pointer tracks valid position
    if condition:
        slow += 1
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
- **Two Sum II** (Sorted Array) - Easy
- **Valid Palindrome** - Easy  
- **Remove Duplicates from Sorted Array** - Easy
- **Container With Most Water** - Medium
- **3Sum** - Medium
- **Trapping Rain Water** - Hard

---

## Summary

The Two Pointers technique is a powerful optimization tool that can:
- Reduce time complexity from O(n²) to O(n)
- Work efficiently with sorted data
- Solve problems in-place with O(1) space

Master this technique by recognizing when problems involve:
- Searching pairs in sorted arrays
- Checking symmetry (palindromes)
- In-place array modifications
- Merging or partitioning operations
