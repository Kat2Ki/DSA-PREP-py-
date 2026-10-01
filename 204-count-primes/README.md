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

# 🔢 Count Primes

### 🔄 Approach: Sieve of Eratosthenes

### 💡 Idea:

* Use the **Sieve of Eratosthenes** to efficiently find all prime numbers less than `n`.
* Initially consider every number as prime, then mark `0` and `1` as non-prime.
* For each number that is still prime, mark all of its multiples as non-prime.
* Start marking multiples from `i × i`, since smaller multiples have already been handled by smaller prime numbers.
* Only process numbers up to `√n`.
* Finally, count the numbers that remain marked as prime.

### ⏱️ Time Complexity:

**O(n log log n)**

### 💾 Space Complexity:

**O(n)**
