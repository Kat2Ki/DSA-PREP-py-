# LeetCode 1929: Concatenation of Array

## 🎯 Problem Explanation
We are given an integer array (or a list in Python). The goal is to create a new array that is twice the length of the original array, where the elements of the original array are repeated/concatenated back-to-back.

### Example:
* **Input:** `nums = [1, 2, 3]`
* **Output:** `[1, 2, 3, 1, 2, 3]`

---

## 🔍 Method 1: Using Loop and Append
In this beginner-friendly method, we create a fresh list and use loops to manually grab each element from the original list and append it to our new list. 

### 🧠 Approach:
1. Create an empty list called `result`.
2. Run a loop through the original list `nums` and `append()` each element to `result` for the first half.
3. Run a second loop through `nums` and `append()` each element again to fill the second half.
4. Return the completed `result` list.

---

## 💻 Python Code Implementation

```python
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        result = []
        
        # First pass: Copy the original list elements
        for num in nums:
            result.append(num)
            
        # Second pass: Copy them again to concatenate
        for num in nums:
            result.append(num)
            
        return result

# --- Local Testing ---
if __name__ == "__main__":
    obj = Solution()
    test_case = [1, 2, 1]
    
    output = obj.getConcatenation(test_case)
    print(f"Input:  {test_case}")
    print(f"Output: {output}")  # Expected: [1, 2, 1, 1, 2, 1]
```

---

## 📊 Complexity Analysis

* **Time Complexity:** $O(n)$ — We iterate through the original array of size $n$ exactly twice, making it a linear time operation.
* **Space Complexity:** $O(n)$ — We create a new `result` list that grows relative to the size of the input array to hold $2n$ elements.
