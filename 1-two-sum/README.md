<h2><a href="https://leetcode.com/problems/two-sum">Two Sum</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>You are given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>Only one valid answer exists.</strong></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:&nbsp;</strong>Can you come up with an algorithm that is less than <code>O(n<sup>2</sup>)</code><font face="monospace">&nbsp;</font>time complexity?


### 🔄 Approach: Hash Map / Dictionary

[![svg](https://img.shields.io/badge/Approach-Hash%20Map-blue?style=flat-square)](#-idea)

### 💡 Idea:

* Create an empty dictionary `seen` to store **number → index**.
* Traverse the array using its index.
* For each number, calculate the number we need:
  `needed = target - nums[i]`
* Check if `needed` already exists in `seen`.
* If it exists, return:
  `[seen[needed], i]`
* Otherwise, store the current number and its index:
  `seen[nums[i]] = i`
* This also handles duplicates like `[3,3]` because the first `3` is stored before reaching the second one.

### ⏱️ Time Complexity:

[![svg](https://img.shields.io/badge/Time-O\(n\)-green?style=flat-square)](#-time-complexity)

* **O(n)** — We traverse the array once.
* Dictionary lookup is **O(1)** on average.

### 💾 Space Complexity:

[![svg](https://img.shields.io/badge/Space-O\(n\)-purple?style=flat-square)](#-space-complexity)

* **O(n)** — In the worst case, we store every element in the dictionary.


