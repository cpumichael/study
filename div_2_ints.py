
'''
Given two integers dividend and divisor, divide
two integers without using multiplication,
division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero,
which means losing its fractional part.
For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.

Note:

    Both dividend and divisor will be 32-bit signed integers.
    The divisor will never be 0.
    Assume we are dealing with an environment which could only
    store integers within the 32-bit signed integer range:


    why???? Seems OK with regular numbers

    [−231,  231 − 1].
    For the purpose of this problem, assume that your function
    returns 231 − 1 when the division result overflows.

'''

def my_div(a, b):
    ''' returns trunc(a/b)'''
    if a < b:
        return 0
    return 1 + my_div(a-b, b)

def my_divd(a, b):
    neg = False
    if a < 0 and b > 0:
        neg = True
        a = -a
    if a > 0 and b < 0:
        neg = True
        b = -b

    if neg:
        return -my_div(a, b)
    else:
        return my_div(a, b)

if __name__ == '__main__':
    print(my_divd(7, 3))
    print(my_divd(10, 3))
    print(my_divd(-7, 3))
    print(my_divd(-10, 3))

# vim: ai sw=4 ts=4 et showmatch
