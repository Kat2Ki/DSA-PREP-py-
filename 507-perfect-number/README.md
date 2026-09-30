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
	
🔄 Approach: Divisor Pairs
A perfect number is a number whose positive divisors, excluding itself, add up to the number.

	
💡 Idea
Instead of checking every number from 1 to num, check only up to √num.
Divisors come in pairs.
If i divides num, then num // i is its paired divisor.
Start total = 1 because 1 is a divisor of every number greater than 1.
If i == num // i, the number is a perfect square, so add it only once.
Finally, check whether total == num.

⚡ Complexity

Time: O(√n)
Space: O(1)
	<li><code>1 &lt;= num &lt;= 10<sup>8</sup></code></li>
</ul>
