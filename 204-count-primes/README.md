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

🔄 Approach: Sieve of Eratosthenes
💡 Idea:
We need to count all prime numbers strictly less than n.
Initially, assume every number is prime.
0 and 1 are not prime, so mark them False.
Start from 2.
If i is still marked True, then i is prime.
Mark all multiples of i as False because they cannot be prime.
Start marking from i × i because smaller multiples have already been handled by smaller prime numbers.
We only need to process numbers up to √n.
Finally, sum(prime) counts the remaining True values because True = 1 and False = 0.

⏱️ Complexity

Time: O(n log log n)
Space: O(n)
