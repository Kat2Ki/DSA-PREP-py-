<h2><a href="https://leetcode.com/problems/count-primes">Count Primes</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given an integer <code>n</code>, return <em>the number of prime numbers that are strictly less than</em> <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 0
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 5 * 10<sup>6</sup></code></li>
</ul>

# 🔢 Check for Prime Number

### 💡 Idea:
- A prime number has exactly two factors: `1` and itself.
- Numbers less than `2` are not prime.
- We only check divisors up to `√n` because if `n` has a factor greater than `√n`, its corresponding factor must be smaller than `√n`.
- If any number from `2` to `√n` divides `n`, return `False`.
- Otherwise, return `True`.

### 🔄 Approach:
**Trial Division up to √n**

### ⏱️ Time Complexity:
`O(√n)`

### 💾 Space Complexity:
`O(1)`

**O(n log log n)**

### 💾 Space Complexity:

**O(n)**
