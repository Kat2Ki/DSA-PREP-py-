<h2><a href="https://leetcode.com/problems/single-number">Single Number</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given a <strong>non-empty</strong>&nbsp;array of integers <code>nums</code>, every element appears <em>twice</em> except for one. Find that single one.</p>

<p>You must&nbsp;implement a solution with a linear runtime complexity and use&nbsp;only constant&nbsp;extra space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,2,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,1,2,1,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>


<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-3 * 10<sup>4</sup> &lt;= nums[i] &lt;= 3 * 10<sup>4</sup></code></li>
	<li>Each element in the array appears twice except for one element which appears only once.</li>
</ul>


## 🔄 Approach: XOR

[<img src="https://img.shields.io/badge/Approach-XOR-blue?style=for-the-badge" />](#-approach-xor)

### 💡 Idea:

[<img src="https://img.shields.io/badge/Idea-XOR-green?style=for-the-badge" />](#-idea)

* Every element appears **twice**, except one.
* XOR has an important property:

  * `a ^ a = 0` → identical numbers cancel each other.
  * `a ^ 0 = a` → the single number remains.
* Start with `k = 0`.
* XOR every element with `k`.
* After all elements are processed, all pairs cancel and `k` contains the **single element**.

### 🧠 Pseudocode:

```text
k = 0

FOR each number in nums:
    k = k XOR number

RETURN k
```

### 🔍 Example:

```text
nums = [4, 1, 2, 1, 2]

0 ^ 4 ^ 1 ^ 2 ^ 1 ^ 2

Pairs cancel:
1 ^ 1 = 0
2 ^ 2 = 0

Remaining:
4
```

**Answer = 4**

### ⏱️ Time Complexity:

[<img src="https://img.shields.io/badge/Time-O(n)-orange?style=for-the-badge" />](#-time-complexity)

* We traverse the array once.
* Therefore, **O(n)**.

### 💾 Space Complexity:

[<img src="https://img.shields.io/badge/Space-O(1)-purple?style=for-the-badge" />](#-space-complexity)

* Only one variable `k` is used.
* Therefore, **O(1)** extra space.
