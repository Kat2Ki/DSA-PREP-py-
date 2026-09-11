<h2><a href="https://leetcode.com/problems/max-consecutive-ones">Max Consecutive Ones</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given a binary array <code>nums</code>, return <em>the maximum number of consecutive </em><code>1</code><em>&#39;s in the array</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,0,1,1,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,0,1,1,0,1]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>

# 🔄 Approach: Counting Consecutive Ones

[![Approach](https://img.shields.io/badge/Approach-Counting-blueviolet.svg)](#)

### 💡 Idea:

[![Idea](https://img.shields.io/badge/Idea-Track%20Current%20%26%20Maximum-orange.svg)](#)

* Traverse the array from left to right.
* Maintain a variable `current` to count the **current consecutive `1`s**.
* If the element is `1`:

  * Increment `current`.
  * Update `maximum` if `current` becomes larger.
* If the element is `0`:

  * Reset `current` to `0` because the consecutive sequence is broken.
* Return `maximum` at the end.

### 🧠 Example:

```text
nums = [1, 1, 0, 1, 1, 1]

current:
1 → 2 → 0 → 1 → 2 → 3

maximum:
1 → 2 → 2 → 2 → 2 → 3

Answer = 3
```

### 📝 Pseudocode:

```text
current = 0
maximum = 0

FOR each element in nums:

    IF element == 1:
        current = current + 1

        IF current > maximum:
            maximum = current

    ELSE:
        current = 0

RETURN maximum
```

### ⏱️ Time Complexity:

[![Time](https://img.shields.io/badge/Time-O\(n\)-green.svg)](#)

`O(n)` — We traverse the array once.

### 💾 Space Complexity:

[![Space](https://img.shields.io/badge/Space-O\(1\)-yellow.svg)](#)

`O(1)` — Only two variables are used regardless of the input size.

### ⚠️ Key Learning:

* `i` → represents the **index**.
* `nums[i]` → represents the **element/value** at that index.
* `current` → tracks the **current streak**.
* `maximum` → tracks the **longest streak found so far**.
* When a `0` appears, reset the current streak.
