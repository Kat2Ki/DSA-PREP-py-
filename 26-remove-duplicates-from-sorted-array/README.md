<h2><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array">Remove Duplicates from Sorted Array</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given an integer array <code>nums</code> sorted in <strong>non-decreasing order</strong>, remove the duplicates <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><strong>in-place</strong></a> such that each unique element appears only <strong>once</strong>. The <strong>relative order</strong> of the elements should be kept the <strong>same</strong>.</p>

<p>Consider the number of <em>unique elements</em> in&nbsp;<code>nums</code> to be <code>k<strong>​​​​​​​</strong></code>​​​​​​​. <meta charset="UTF-8" />After removing duplicates, return the number of unique elements&nbsp;<code>k</code>.</p>

<p><meta charset="UTF-8" />The first&nbsp;<code>k</code>&nbsp;elements of&nbsp;<code>nums</code>&nbsp;should contain the unique numbers in <strong>sorted order</strong>. The remaining elements beyond index&nbsp;<code>k - 1</code>&nbsp;can be ignored.</p>

<p><strong>Custom Judge:</strong></p>

<p>The judge will test your solution with the following code:</p>

<pre>
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i &lt; k; i++) {
    assert nums[i] == expectedNums[i];
}
</pre>

<p>If all assertions pass, then your solution will be <strong>accepted</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,2]
<strong>Output:</strong> 2, nums = [1,2,_]
<strong>Explanation:</strong> Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,0,1,1,1,2,2,3,3,4]
<strong>Output:</strong> 5, nums = [0,1,2,3,4,_,_,_,_,_]
<strong>Explanation:</strong> Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li>
</ul>


# 🔄 Approach: Two Pointers

[<svg aria-hidden="true" width="16" height="16" viewBox="0 0 16 16"><path d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0ZM6.94 4.5 11 8l-4.06 3.5v-2.25H5V6.75h1.94V4.5Z"/></svg>](#-idea)

### 💡 Idea:

[<svg aria-hidden="true" width="16" height="16" viewBox="0 0 16 16"><path d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0ZM6.94 4.5 11 8l-4.06 3.5v-2.25H5V6.75h1.94V4.5Z"/></svg>](#-idea)

* The array is already sorted, so duplicate elements are next to each other.
* Use **two pointers**:

  * `i` → scans through the array.
  * `k` → keeps track of the position of the last unique element.
* Start `k = 0` because the first element is always unique.
* Start scanning from index `1`.
* If `nums[i] != nums[k]`, we found a new unique element:

  * Increment `k`.
  * Store `nums[i]` at `nums[k]`.
* Return `k + 1` because `k` represents the **index**, while we need the **count** of unique elements.
* The elements after index `k` can be ignored.

### ⏱️ Time Complexity:

[<svg aria-hidden="true" width="16" height="16" viewBox="0 0 16 16"><path d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0ZM6.94 4.5 11 8l-4.06 3.5v-2.25H5V6.75h1.94V4.5Z"/></svg>](#-time-complexity)

**O(n)** — We scan the array once.

### 💾 Space Complexity:

[<svg aria-hidden="true" width="16" height="16" viewBox="0 0 16 16"><path d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0ZM6.94 4.5 11 8l-4.06 3.5v-2.25H5V6.75h1.94V4.5Z"/></svg>](#-space-complexity)

**O(1)** — We modify the array in-place and use only pointer variables.

