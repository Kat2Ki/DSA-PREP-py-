<h2><a href="https://leetcode.com/problems/contains-duplicate">Contains Duplicate</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given an integer array <code>nums</code>, return <code>true</code> if any value appears <strong>at least twice</strong> in the array, and return <code>false</code> if every element is distinct.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>The element 1 occurs at the indices 0 and 3.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p>All elements are distinct.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1,3,3,4,3,2,4,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

## 🔄 Approach: Hashing / Set

[<img src="https://img.shields.io/badge/Approach-Hashing-blue?style=flat-square" />](#approach-hashing--set)

### 💡 Idea:

[<img src="https://img.shields.io/badge/Idea-Set-orange?style=flat-square" />](#idea)

* Create a `set` called `seen` to store elements we have already encountered.
* Traverse the array one element at a time.
* If the current element is already in `seen`, a duplicate exists → return `True`.
* Otherwise, add the current element to `seen`.
* If the entire loop finishes without finding a duplicate, return `False`.

### ⏱️ Time Complexity:

[<img src="https://img.shields.io/badge/Time-O(n)-green?style=flat-square" />](#time-complexity)

* **O(n)** — We traverse the array once.
* Set lookup and insertion take **O(1)** average time.

### 💾 Space Complexity:

[<img src="https://img.shields.io/badge/Space-O(n)-purple?style=flat-square" />](#space-complexity)

* **O(n)** — In the worst case, the set stores all `n` elements.
