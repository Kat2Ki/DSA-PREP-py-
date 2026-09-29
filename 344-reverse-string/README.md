<h2><a href="https://leetcode.com/problems/reverse-string">Reverse String</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Write a function that reverses a string. The input string is given as an array of characters <code>s</code>.</p>

<p>You must do this by modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a> with <code>O(1)</code> extra memory.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = ["h","e","l","l","o"]
<strong>Output:</strong> ["o","l","l","e","h"]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = ["H","a","n","n","a","h"]
<strong>Output:</strong> ["h","a","n","n","a","H"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is a <a href="https://en.wikipedia.org/wiki/ASCII#Printable_characters" target="_blank">printable ascii character</a>.</li>
</ul>

# 🔄 Approach: Two Pointers

### 💡 Idea:

* Use **two pointers**:

  * `left` starts from the beginning → `0`
  * `right` starts from the end → `len(s) - 1`
* While `left < right`:

  * Swap the characters at `left` and `right`.
  * Move `left` one step forward.
  * Move `right` one step backward.
* Continue until the two pointers meet or cross.
* The string is reversed **in-place**, so no extra array is needed.

### 🧠 Pseudocode:

```text
left = 0
right = length of s - 1

while left < right:
    swap s[left] and s[right]
    left += 1
    right -= 1
```

### ⏱️ Time Complexity:

**O(n)** — We visit about half of the elements.

### 💾 Space Complexity:

**O(1)** — No extra array is used.

### 🔑 Pattern:

**Two Pointers → Opposite Ends → Swap → Move Inward**
