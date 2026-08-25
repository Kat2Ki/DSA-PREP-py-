<h2><a href="https://leetcode.com/problems/reverse-integer">Reverse Integer</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given a signed 32-bit integer <code>x</code>, return <code>x</code>&nbsp;with its digits reversed. If reversing <code>x</code> causes the value to go outside the signed 32-bit integer range <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>, then return <code>0</code>.</p>

<p><strong>Assume the environment does not allow you to store 64-bit integers (signed or unsigned).</strong></p>
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> x = 123
<strong>Output:</strong> 321
</pre>
<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> x = -123
<strong>Output:</strong> -321
</pre>
<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> x = 120
<strong>Output:</strong> 21
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>-2<sup>31</sup> &lt;= x &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

## 🔄 Approach: Reverse Integer

### 💡 Idea:

* First, store the **sign** of the number (`positive` or `negative`) separately. ➕➖
* Convert the number into its **absolute value** so we can reverse only the digits. 🔢
* Extract the last digit using **modulo (`% 10`)**. 🎯
* Add that digit to the reversed number:

  ```
  revn = revn * 10 + last_digit
  ```
* Remove the last digit from the original number using **integer division (`// 10`)**. ✂️
* After reversing all digits, apply the original sign back. 🔁
* Check if the result is within the **32-bit integer range**. ⚠️

  * If outside range → return `0`
  * Else → return reversed number ✅


### ⏱️ Time Complexity:

**O(log₁₀(n))** 🚀

* Because we process each digit of the number once.
* Number of digits in `n` = `log₁₀(n)`

Example:
12345 → 5 digits → 5 iterations


### 💾 Space Complexity:

**O(1)** 🧠

* Only constant variables are used:

  * `sign`
  * `n`
  * `revn`
  * `lastd`

No extra data structure is used. ✅



