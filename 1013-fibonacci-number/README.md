<h2><a href="https://leetcode.com/problems/fibonacci-number">Fibonacci Number</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>The <b>Fibonacci numbers</b>, commonly denoted <code>F(n)</code> form a sequence, called the <b>Fibonacci sequence</b>, such that each number is the sum of the two preceding ones, starting from <code>0</code> and <code>1</code>. That is,</p>

<pre>
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n &gt; 1.
</pre>

<p>Given <code>n</code>, calculate <code>F(n)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> F(2) = F(1) + F(0) = 1 + 0 = 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> F(3) = F(2) + F(1) = 1 + 1 = 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong> F(4) = F(3) + F(2) = 2 + 1 = 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 30</code></li>
</ul>


## 🔄 Approach: Recursive Fibonacci

[svg](https://github.com/Kat2Ki/DSA-PREP-py-/tree/main/8-fibonacci-number#-approach-recursive-fibonacci)

### 💡 Idea:

[svg](https://github.com/Kat2Ki/DSA-PREP-py-/tree/main/8-fibonacci-number#-idea)

* Fibonacci follows the formula **`F(n) = F(n-1) + F(n-2)`**. 🔢
* For `n = 0` or `n = 1`, the answer is already known:

  * `F(0) = 0`
  * `F(1) = 1`
* These conditions form the **base case**, which stops the recursion. 🛑
* For `n > 1`, call the function recursively for:

  * `n - 1`
  * `n - 2`
* Add both results to get `F(n)`. ➕
* The recursion continues until it reaches the base cases. 🔁

### ⏱️ Time Complexity:

[svg](https://github.com/Kat2Ki/DSA-PREP-py-/tree/main/8-fibonacci-number#%EF%B8%8F-time-complexity)

**O(2ⁿ)** 🚀

* Each function call creates **two more recursive calls**.
* Many Fibonacci values are calculated repeatedly.

### 💾 Space Complexity:

[svg](https://github.com/Kat2Ki/DSA-PREP-py-/tree/main/8-fibonacci-number#-space-complexity)

**O(n)** 🧠

* The maximum depth of the recursive call stack is `n`.
* No extra data structure is used. ✅

