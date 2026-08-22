# Reverse Integer

A logical approach to reversing the digits of a 32-bit signed integer using pure mathematical operations. 

## Overview

The goal of this algorithm is to take an integer input and reverse the order of its digits (e.g., turning `123` into `321`, or `-456` into `-654`). 

A key constraint in this classic problem is the **32-bit environment limit**. If the reversed integer exceeds the standard 32-bit signed integer range of $[-2^{31}, 2^{31} - 1]$, the function must return `0` to simulate integer overflow.

## The Approach

While it is tempting to convert the integer into a string, reverse the string, and parse it back into an integer, doing so consumes extra memory and often bypasses the core algorithmic challenge. 

Instead, this solution relies entirely on arithmetic operations—specifically **modulo** and **floor division**—to peel digits off the original number and construct the new reversed number one digit at a time.

### Step-by-Step Breakdown

1. **Sign Extraction:** 
   Because negative numbers can complicate modulo arithmetic, we first determine the sign of the input. We store a multiplier (`1` for positive, `-1` for negative) and then take the absolute value of the input. This standardizes the rest of the mathematical process.

2. **Digit Extraction (Popping):** 
   We process the standardized number in a loop until it reaches zero. In each iteration, we use the modulo operator (`% 10`) to extract the right-most digit. For example, `123 % 10` gives us `3`. 
   
3. **Number Reconstruction (Pushing):** 
   To build the reversed number, we take our running total (which starts at 0), multiply it by 10 to shift its current digits one place to the left, and add our newly extracted digit. 
   * *Iteration 1:* `0 * 10 + 3 = 3`
   * *Iteration 2:* `3 * 10 + 2 = 32`
   * *Iteration 3:* `32 * 10 + 1 = 321`

4. **Number Reduction:**
   After extracting a digit, we use floor division (`// 10`) on our original number to remove that right-most digit (e.g., `123 // 10` becomes `12`), moving us closer to the end of the loop.

5. **Sign Restoration and Overflow Validation:**
   Once the loop finishes, we multiply the reconstructed number by our stored sign multiplier. Finally, we check if this result falls outside the safe 32-bit integer range ($-2,147,483,648$ to $2,147,483,647$). If it does, we return `0` to indicate an overflow; otherwise, we return the reversed number.

## Complexity Analysis

* **Time Complexity:** $O(\log_{10}(x))$. The number of iterations in our loop is equal to the number of digits in the input integer $x$. Since the number of digits scales logarithmically with the size of the number in base 10, the time complexity is logarithmic.
* **Space Complexity:** $O(1)$. The algorithm is extremely memory-efficient. It does not allocate any arrays or strings, relying solely on a few integer variables to track the current state, regardless of how large the input number is.
