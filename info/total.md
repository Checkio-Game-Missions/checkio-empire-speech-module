Now robots on the farm have restored some functions in calculation and can work more effective.
But we should improve communication and reporting module. Let's learn robots convert numbers in words.

You are given an integer number. Convert it word form in English.
All the words in the string must be separated by exactly one space character.
Be careful with spaces -- it's hard to see if you place two spaces instead one.

For example, 143 => 'one hundred forty three'.

**Input:** A number as an integer.

**Output:** The string representation of the number as a string.

**Example:**

```python
tell_number(4)=='four'
tell_number(143)=='one hundred forty three'
tell_number(12)=='twelve'
tell_number(101)=='one hundred one'
tell_number(212)=='two hundred twelve'
tell_number(40)=='forty'
```
**How it is used:**

This concept may be useful for the speech synthesis software or automatic reports systems.
This system can also be used when writing a chatbot by assigning words or phrases numerical
values and having a system retrieve responses based on those values.

**Precondition:**
```python
0 < number < 1000
```
