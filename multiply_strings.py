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

__O0 = ord('0')

def m2c(a, b):
    '''returns mul and carry of a and b'''
    x = ord(a) - __O0
    y = ord(b) - __O0
    return divmod(x * y, 10)

def mul2strs(a, b):
    '''does not check for input, assumes all digits'''
    a = list(reversed(list(a)))
    b = list(reversed(list(b)))

    gtot = 0
    tot = 0
    tens_tens = 0
    for c1 in a:
        tens_place = 0
        c_prev = 0
        for c2 in b:
            c, v = m2c(c1, c2)
            tot += (v + c_prev) * 10**tens_place
            c_prev = c
            tens_place += 1
        tot += (c_prev * 10**tens_place)
        gtot += tot * 10**tens_tens
        tot = 0
        tens_tens += 1

    return f'{gtot}'

if __name__ == '__main__':
    print(mul2strs('123', '456'))
    print(mul2strs('999', '888'))

# vim: ai sw=4 ts=4 et showmatch
