<h2><a href="https://leetcode.com/problems/largest-odd-number-in-string">Largest Odd Number in String</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>You are given a string <code>num</code>, representing a large integer. Return <em>the <strong>largest-valued odd</strong> integer (as a string) that is a <strong>non-empty substring</strong> of </em><code>num</code><em>, or an empty string </em><code>&quot;&quot;</code><em> if no odd integer exists</em>.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters within a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = &quot;52&quot;
<strong>Output:</strong> &quot;5&quot;
<strong>Explanation:</strong> The only non-empty substrings are &quot;5&quot;, &quot;2&quot;, and &quot;52&quot;. &quot;5&quot; is the only odd number.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = &quot;4206&quot;
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> There are no odd numbers in &quot;4206&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> num = &quot;35427&quot;
<strong>Output:</strong> &quot;35427&quot;
<strong>Explanation:</strong> &quot;35427&quot; is already an odd number.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num.length &lt;= 10<sup>5</sup></code></li>
	<li><code>num</code> only consists of digits and does not contain any leading zeros.</li>
</ul>

# 🔢 Largest Odd Number

### 💡 Idea:
- We need to find the **largest-valued odd number** that is a substring of `num`.
- An integer is odd if its **last digit is odd**.
- Start checking the string from **right → left**.
- Find the **rightmost odd digit**.
- Once found, take the substring from the beginning up to that digit.
- If no odd digit exists, return `""`.

### 🔄 Approach:
1. Start from the last index of `num`.
2. Move backwards through the string.
3. Check whether the current digit is odd using:
   ```python
   int(num[i]) % 2 == 1
   ```
4. If it is odd, return:
   ```python
   num[0:i+1]
   ```
5. If the loop finishes without finding an odd digit, return `""`.


### ⏱️ Time Complexity:
**O(n)** — in the worst case, we scan every digit once.

### 💾 Space Complexity:
**O(1)** auxiliary space.

