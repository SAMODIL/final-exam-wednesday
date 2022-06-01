# Intro to CS Tutorial Final Exam

These are the instructions for your <b>final exam</b>.
<br><br>
<s>READ CAREFULLY</s>
<br><br>
## Max Product Segment of Array

For your final today, you will find the segment of an array with maximal product.

In the file `prod.py` you will see 3 functions: `prefix_prod`, `segment_prod`, `max_prod_segment`. Each function corresponds to a task you need to complete. For each next task **YOU MUST USE PREVIOUS FUNCTIONS**.

### Task 1
Complete the function `prefix_prod`, which takes `array` and returns an array of _prefix products_. Read the info in `prod.py` fo more
### Task 2
Complete the function `segment_prod`, which takes `array`, `left`, and `right` and returns the product of elements of `array` between and including indices  `left` and `right`. Assuming that `array` does not contain zeros, use `prefix_prod` for this. Note that to get an integer from division you should use `//` instead of `/`
### Task 3
Complete the function `max_prod_segment`, which takes `array` and returns maximal product of the segments of `array`.

### Testing
To run tests, run `python3 -m pytest -xv` from the folder of your final exam.
