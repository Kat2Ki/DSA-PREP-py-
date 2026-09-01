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


🔄 Approach: Sorting + Sliding Window

💡 Idea:

Sort the array so the largest element of the current window is nums[right].
Use two pointers, left and right, to maintain a sliding window.
total stores the sum of elements inside the window.
To make every element equal to nums[right], calculate:
nums[right] * window_size - total
If the required operations are greater than k, shrink the window by moving left.
Keep track of the maximum valid window size.

⏱️ Time Complexity:
Sorting takes O(n log n).
The sliding window takes O(n).
Overall: O(n log n).

💾 Space Complexity:
Uses only a few extra variables.
Sorting is performed in-place.
Overall: O(1) auxiliary space.

Sorting is done in-place.
Overall: O(1) auxiliary space.
