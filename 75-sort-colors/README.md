<h2><a href="https://leetcode.com/problems/sort-colors">Sort Colors</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>You are given an array <code>nums</code> with <code>n</code> objects colored red, white, or blue, sort them <strong><a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a> </strong>so that objects of the same color are adjacent, with the colors in the order red, white, and blue.</p>

<p>We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.</p>

<p>You must solve this problem without using the library&#39;s sort function.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,0,2,1,1,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,0,1,1,2,2]</span></p>

<p><strong>Explanation:</strong></p>

<p>The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first, then all 1s, then all 2s.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,0,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,1,2]</span></p>

<p><strong>Explanation:</strong></p>

<p>The array has one each of 0, 1, and 2, arranged in-place in the order 0, 1, 2.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 300</code></li>
	<li><code>nums[i]</code> is either 0, 1, or 2.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong>&nbsp;Could you come up with a one-pass algorithm using only&nbsp;constant extra space?</p>

# 🎨 Sort Colors

## 🔄 Approach: Counting

[![View](https://img.shields.io/badge/Approach-Counting-blue?style=flat-square\&logo=github)](#)

### 💡 Idea:

[![View](https://img.shields.io/badge/Idea-Count%20%26%20Overwrite-purple?style=flat-square\&logo=github)](#)

* The array contains only **three values:** `0`, `1`, and `2`.
* Count how many times each value occurs.
* Store the counts in:

  * `count0` → number of `0`s
  * `count1` → number of `1`s
  * `count2` → number of `2`s
* Then overwrite the original array:

  * Put `0` → `count0` times.
  * Put `1` → `count1` times.
  * Put `2` → `count2` times.
* Use an `index` variable to keep track of the position where the next value should be placed.
* This modifies the original array, so it satisfies the **in-place** requirement.
* We do **not** use Python's built-in `sort()` function.

### 🧪 Example:

```text
nums = [2, 0, 2, 1, 1, 0]

Counts:
0 → 2
1 → 2
2 → 2

Overwrite:
[0, 0, 1, 1, 2, 2]
```

### ⏱️ Time Complexity:

[![View](https://img.shields.io/badge/Time-O\(n\)-green?style=flat-square\&logo=github)](#)

* First pass counts the elements → `O(n)`
* Second pass overwrites the array → `O(n)`
* Overall → **O(n)**

### 💾 Space Complexity:

[![View](https://img.shields.io/badge/Space-O\(1\)-orange?style=flat-square\&logo=github)](#)

* Only a few variables (`count0`, `count1`, `count2`, `index`) are used.
* No extra array is created.
* Therefore → **O(1)** auxiliary space.

