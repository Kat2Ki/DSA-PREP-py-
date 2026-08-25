<h2><a href="https://leetcode.com/problems/palindrome-number">Palindrome Number</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given an integer <code>x</code>, return <code>true</code> if <code>x</code> is a <span data-keyword="palindrome-integer"><strong>palindrome</strong></span>, and <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 121
<strong>Output:</strong> true
<strong>Explanation:</strong> 121 reads as 121 from left to right and from right to left.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = -121
<strong>Output:</strong> false
<strong>Explanation:</strong> From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> x = 10
<strong>Output:</strong> false
<strong>Explanation:</strong> Reads 01 from right to left. Therefore it is not a palindrome.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup>&nbsp;&lt;= x &lt;= 2<sup>31</sup>&nbsp;- 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it without converting the integer to a string?


## 🧠 Approach: String Conversion + Reverse
Instead of reversing the number mathematically, I convert the integer into a string and compare it with its reversed version.


## 🚀 Algorithm

1. Convert integer `x` into a string.
2. Reverse the string using slicing `[::-1]`.
3. Compare the original string with the reversed string.
4. If both are equal, return `True`.
5. Otherwise, return `False`.


## ⏱️ Complexity Analysis

### Time Complexity: `O(n)`

* Converting integer to string takes `O(n)`.
* Reversing the string takes `O(n)`.
* Comparing both strings takes `O(n)`.

Where `n` = number of digits in `x`.


### Space Complexity: `O(n)`

* Extra space is required to store:

  * Original string
  * Reversed string

