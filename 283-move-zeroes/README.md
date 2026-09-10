<h2><a href="https://leetcode.com/problems/move-zeroes">Move Zeroes</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given an integer array <code>nums</code>, move all <code>0</code>&#39;s to the end of it while maintaining the relative order of the non-zero elements.</p>

<p><strong>Note</strong> that you must do this in-place without making a copy of the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [0,1,0,3,12]
<strong>Output:</strong> [1,3,12,0,0]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0]
<strong>Output:</strong> [0]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you minimize the total number of operations done?

## 🔄 Approach: Two Pointers

[![Approach](https://img.shields.io/badge/Approach-Two%20Pointers-blue)](#)

### 💡 Idea:

[![Idea](https://img.shields.io/badge/Idea-Move%20Non--Zero%20Elements-green)](#)

* Use two pointers: `i` and `k`.
* `i` scans through the entire array.
* `k` keeps track of the position where the next **non-zero** element should be placed.
* When `nums[i] != 0`:

  * Place `nums[i]` at `nums[k]`.
  * Increment `k`.
* After all non-zero elements are placed, fill the remaining positions from `k` to the end with `0`.
* This maintains the relative order of all non-zero elements.
* The array is modified **in-place**, so no extra array is created.

### ⏱️ Time Complexity:

[![Time](https://img.shields.io/badge/Time-O\(n\)-orange)](#)

* We scan the array once to move non-zero elements.
* We scan the remaining positions once to fill them with zeroes.
* Overall: **O(n)**.

### 💾 Space Complexity:

[![Space](https://img.shields.io/badge/Space-O\(1\)-purple)](#)

* Only the two pointers `i` and `k` are used.
* No extra array or data structure is created.
* Therefore: **O(1)** auxiliary space.

