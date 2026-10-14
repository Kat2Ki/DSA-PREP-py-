<h2><a href="https://leetcode.com/problems/longest-common-prefix">Longest Common Prefix</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Write a function to find the longest common prefix string amongst an array of strings.</p>

<p>If there is no common prefix, return an empty string <code>&quot;&quot;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;flower&quot;,&quot;flow&quot;,&quot;flight&quot;]
<strong>Output:</strong> &quot;fl&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;dog&quot;,&quot;racecar&quot;,&quot;car&quot;]
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> There is no common prefix among the input strings.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>

## 🔄 Approach: Character-by-Character Comparison

### 💡 Idea
- Take the first string as the reference.
- Compare characters at the same index across all strings.
- If a character mismatches or a string ends, return the prefix found so far.
- Otherwise, add the matching character to the prefix.

### 📝 Pseudocode
```text
ref = first string
prefix = ""

FOR each index i in ref:
    char = ref[i]

    FOR each string in strs:
        IF i >= length(string) OR string[i] != char:
            RETURN prefix

    prefix += char

RETURN prefix
```

### ⏱️ Complexity
- **Time:** O(n × m)
- **Space:** O(1) auxiliary space

Where `n` = number of strings and `m` = length of the first string.

	
	<li><code>1 &lt;= strs.length &lt;= 200</code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 200</code></li>
	<li><code>strs[i]</code> consists of only lowercase English letters if it is non-empty.</li>
</ul>
