# Big O Notation

Big O notation describes the **time complexity** and **space complexity** of algorithms, helping us understand how they scale as input size grows.

## What is Big O?

Big O describes the **worst-case scenario** for how an algorithm's runtime or memory usage grows relative to the input size (n).

## Common Time Complexities

### O(1) - Constant Time
- Runtime doesn't change with input size
- Example: Accessing an array element by index
```python
arr[0]  # Always takes the same time
```

### O(log n) - Logarithmic Time
- Runtime grows logarithmically as input doubles
- Example: Binary search in a sorted array
- Very efficient for large datasets

### O(n) - Linear Time
- Runtime grows linearly with input size
- Example: Iterating through an array once
```python
for i in range(n):  # Loops n times
    print(i)
```

### O(n log n) - Linearithmic Time
- Common in efficient sorting algorithms
- Example: Merge sort, Quick sort (average case)

### O(n²) - Quadratic Time
- Runtime grows with the square of input size
- Example: Nested loops
```python
for i in range(n):
    for j in range(n):  # n * n iterations
        # do something
```

### O(2^n) - Exponential Time
- Runtime doubles with each additional input
- Example: Recursive Fibonacci without memoization
- Very inefficient for large inputs

### O(n!) - Factorial Time
- Extremely slow, grows fastest
- Example: Generating all permutations

## Space Complexity

Space complexity measures how much additional memory an algorithm uses.

- **O(1)**: Constant space - only a few variables
- **O(n)**: Linear space - space grows with input (e.g., creating a new array)

## Big O Rules

1. **Drop Constants**: O(2n) → O(n), O(100) → O(1)
2. **Drop Non-Dominant Terms**: O(n² + n) → O(n²)
3. **Different Inputs Use Different Variables**: O(a + b) not O(n)
4. **Focus on Worst Case**: Assume the least favorable scenario

## Examples from Our Code

### Two Sum (Brute Force)
```python
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            return [i, j]
```
- **Time**: O(n²) - nested loops
- **Space**: O(1) - only using variables

### Two Sum (Two Pointers)
```python
while left < right:
    currSum = arr[left] + arr[right]
    if currSum == target:
        return [left, right]
    elif currSum < target:
        right -= 1
    else:
        left += 1
```
- **Time**: O(n) - single pass through array
- **Space**: O(1) - only using pointers

### Palindrome Check
```python
while left < right:
    if s[left] != s[right]:
        return False
    left += 1
    right -= 1
return True
```
- **Time**: O(n) - checking n/2 characters at most
- **Space**: O(1) - only using two pointers

## Why Big O Matters

- Helps choose the right algorithm for the problem size
- Small inputs: Any algorithm works
- Large inputs: O(n) vs O(n²) makes a huge difference
  - n = 1,000,000: O(n) = 1M operations vs O(n²) = 1 trillion operations!