'''
Given two non-negative integers num1 and num2 represented as
strings, return the product of num1 and num2, also
represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

Note:

    The length of both num1 and num2 is < 110.
    Both num1 and num2 contain only digits 0-9.
    Both num1 and num2 do not contain any leading
    zero, except the number 0 itself.
    You must not use any built-in BigInteger
    library or convert the inputs to integer directly.


Notes:

mul 123 and 456:

    1
   123
   456
 -----
  1
   738
  615
 492
------
 56088

use ord('c') to get numeric value


'''

def mul2strs(a, b):
    a = ''.join(reversed(list(a)))
    b = ''.join(reversed(list(b)))

# vim: ai sw=4 ts=4 et showmatch


