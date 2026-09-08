<h2><a href="https://leetcode.com/problems/rotate-array">Rotate Array</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given an integer array <code>nums</code>, rotate the array to the right by <code>k</code> steps, where <code>k</code> is non-negative.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5,6,7], k = 3
<strong>Output:</strong> [5,6,7,1,2,3,4]
<strong>Explanation:</strong>
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,-100,3,99], k = 2
<strong>Output:</strong> [3,99,-1,-100]
<strong>Explanation:</strong> 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>

<ul>
	<li>Try to come up with as many solutions as you can. There are at least <strong>three</strong> different ways to solve this problem.</li>
	<li>Could you do it in-place with <code>O(1)</code> extra space?</li>
</ul>

## 🔄 Approach: Array Reversal

[<img src="https://img.shields.io/badge/LeetCode-189-orange?style=flat-square&logo=leetcode" />](https://leetcode.com/problems/rotate-array/)

### 💡 Idea:

[<img src="https://img.shields.io/badge/Approach-Reverse%20Array-blue?style=flat-square" />](https://leetcode.com/problems/rotate-array/)

* We need to rotate the array **right by `k` positions**.
* First calculate `n = len(nums)`.
* Use `k = k % n` so that `k` never exceeds the array length.
* Reverse the **entire array**.
* Reverse the **first `k` elements**.
* Reverse the **remaining `n-k` elements**.
* Use `nums[:] = ...` when reversing the whole array so that the original list is modified **in-place**.

Example:

```text
nums = [1,2,3,4,5,6,7], k = 3

Reverse entire array:
[7,6,5,4,3,2,1]

Reverse first k:
[5,6,7,4,3,2,1]

Reverse remaining:
[5,6,7,1,2,3,4]
```

### ⏱️ Time Complexity:

[<img src="https://img.shields.io/badge/Time-O(n)-green?style=flat-square" />](https://leetcode.com/problems/rotate-array/)

* Each part of the array is reversed once.
* Overall: **O(n)**.

### 💾 Space Complexity:

[<img src="https://img.shields.io/badge/Space-O(1)-purple?style=flat-square" />](https://leetcode.com/problems/rotate-array/)

* The algorithm modifies the array in-place.
* **O(1) auxiliary space**.

### 🐍 Python slicing reminder:

```python
nums[::-1]      # reverse entire array
nums[0:k]       # first k elements
nums[k:n]       # elements from k to the end
nums[:] = ...   # modify the original list in-place
```

**Pattern to remember:**
`Reverse all → Reverse first k → Reverse remaining`

