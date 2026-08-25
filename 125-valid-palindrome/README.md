<h2><a href="https://leetcode.com/problems/valid-palindrome">Valid Palindrome</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>A phrase is a <strong>palindrome</strong> if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.</p>  <p>Given a string <code>s</code>, return <code>true</code><em> if it is a <strong>palindrome</strong>, or </em><code>false</code><em> otherwise</em>.</p>  <p>&nbsp;</p>  
<p><strong class="example">Example 1:</strong></p>  <pre>  
<strong>Input:</strong> s = &quot;A man, a plan, a canal: Panama&quot;  
<strong>Output:</strong> true  
<strong>Explanation:</strong> &quot;amanaplanacanalpanama&quot; is a palindrome.  
</pre>  <p><strong class="example">Example 2:</strong></p>  <pre>  
<strong>Input:</strong> s = &quot;race a car&quot;  
<strong>Output:</strong> false  
<strong>Explanation:</strong> &quot;raceacar&quot; is not a palindrome.  
</pre>  <p><strong class="example">Example 3:</strong></p>  <pre>  
<strong>Input:</strong> s = &quot; &quot;  
<strong>Output:</strong> true  
<strong>Explanation:</strong> s is an empty string &quot;&quot; after removing non-alphanumeric characters.  
Since an empty string reads the same forward and backward, it is a palindrome.  
</pre>  <p>&nbsp;</p>  
<p><strong>Constraints:</strong></p>  <ul>  
	<li><code>1 &lt;= s.length &lt;= 2 * 10<sup>5</sup></code></li>  
	<li><code>s</code> consists only of printable ASCII characters.</li>  
</ul>


## 🔍 Approach: Valid Palindrome

### 💡 Idea:

* Create an empty list `clean` to store only valid characters. 🧹
* Traverse the string and:

  * Check if the character is **alphanumeric** (letter or number). 🔤🔢
  * Convert it to lowercase to ignore case differences. 🔡
  * Add it to `clean`. ➕
* Compare `clean` with its reverse. 🔄
* If both are the same → it is a palindrome. ✅

Example:

```text
s = "A man, a plan, a canal: Panama"

After cleaning:
"amanaplanacanalpanama"

Reverse:
"amanaplanacanalpanama"

Both same → True ✅



### ⏱️ Time Complexity:

**O(n)** 🚀

* Traverse the string once → `n` operations.
* Reverse comparison also takes `n` operations.
* Total = `O(n)`



### 💾 Space Complexity:

**O(n)** 📦

* Extra list `clean` stores filtered characters.
* In worst case, it stores all characters of the string.



⚡ **Optimization Note:**
A more efficient approach uses **Two Pointers**:

* One pointer from start (`left`)
* One pointer from end (`right`)
* Compare characters while moving inward.

That gives:

* Time: **O(n)**
* Space: **O(1)** ✅



