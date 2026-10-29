<h2><a href="https://leetcode.com/problems/isomorphic-strings">Isomorphic Strings</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>Given two strings <code>s</code> and <code>t</code>, <em>determine if they are isomorphic</em>.</p>

<p>Two strings <code>s</code> and <code>t</code> are isomorphic if the characters in <code>s</code> can be replaced to get <code>t</code>.</p>

<p>All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;egg&quot;, t = &quot;add&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>The strings <code>s</code> and <code>t</code> can be made identical by:</p>

<ul>
	<li>Mapping <code>&#39;e&#39;</code> to <code>&#39;a&#39;</code>.</li>
	<li>Mapping <code>&#39;g&#39;</code> to <code>&#39;d&#39;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;f11&quot;, t = &quot;b23&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p>The strings <code>s</code> and <code>t</code> can not be made identical as <code>&#39;1&#39;</code> needs to be mapped to both <code>&#39;2&#39;</code> and <code>&#39;3&#39;</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;paper&quot;, t = &quot;title&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>



<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>t.length == s.length</code></li>
	<li><code>s</code> and <code>t</code> consist of any valid ascii character.</li>
</ul>

<h2>Approach 💡</h2>
<ul>
	<li>Create two dictionaries: <code>mapping</code> for mapping characters from <code>s</code> to <code>t</code>, and <code>reverse_mapping</code> for mapping characters from <code>t</code> to <code>s</code>.</li>
	<li>Iterate through both strings using their indices.</li>
	<li>Check if a character in <code>s</code> is already mapped to a different character in <code>t</code>. If yes, return <code>False</code>.</li>
	<li>Check if a character in <code>t</code> is already mapped to a different character in <code>s</code>. If yes, return <code>False</code>.</li>
	<li>Store the mappings in both dictionaries.</li>
	<li>If all characters follow the mapping rules, return <code>True</code>.</li>
</ul>

<h2>Pseudocode 📝</h2>
<pre><code>Create an empty mapping dictionary
Create an empty reverse_mapping dictionary

For each index i from 0 to length of s - 1:

    If s[i] exists in mapping AND mapping[s[i]] != t[i]:
        Return False

    If t[i] exists in reverse_mapping AND reverse_mapping[t[i]] != s[i]:
        Return False

    mapping[s[i]] = t[i]
    reverse_mapping[t[i]] = s[i]

Return True
</code></pre>

<h2>Time Complexity ⏱️</h2>
<p><strong>O(n)</strong> &mdash; We traverse the strings once, and dictionary operations take O(1) average time.</p>
