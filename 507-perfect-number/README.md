<h2><a href="https://leetcode.com/problems/perfect-number">Perfect Number</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>A <a href="https://en.wikipedia.org/wiki/Perfect_number" target="_blank"><strong>perfect number</strong></a> is a <strong>positive integer</strong> that is equal to the sum of its <strong>positive divisors</strong>, excluding the number itself. A <strong>divisor</strong> of an integer <code>x</code> is an integer that can divide <code>x</code> evenly.</p>

<p>Given an integer <code>n</code>, return <code>true</code><em> if </em><code>n</code><em> is a perfect number, otherwise return </em><code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 28
<strong>Output:</strong> true
<strong>Explanation:</strong> 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 7
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	
# 🔢 Perfect Number

[![LeetCode](https://img.shields.io/badge/LeetCode-Perfect%20Number-orange)](https://leetcode.com/problems/perfect-number/)

### 🔄 Approach: Divisor Pairs

### 💡 Idea:

* A perfect number is equal to the sum of its positive divisors **excluding itself**.
* Instead of checking every number from `1` to `num`, we check only up to `√num`.
* Divisors always come in pairs:

  * `i`
  * `num // i`
* If `i` divides `num`, add both divisors to `total`.
* If `i == num // i`, it is a perfect-square divisor, so add it only once.
* Start `total = 1` because `1` is always a proper divisor for `num > 1`.
* Finally, check whether `total == num`.

### ⏱️ Time Complexity

`O(√n)`

### 💾 Space Complexity

`O(1)`
	<li><code>1 &lt;= num &lt;= 10<sup>8</sup></code></li>
</ul>
