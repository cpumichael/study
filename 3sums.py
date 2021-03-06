
'''
Given an array nums of n integers, are there elements
a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the
sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''

import itertools

def sum3(a):
    ret = set()
    for i in itertools.combinations(a, 3):
        if sum(i) == 0:
            x = sorted(i)
            ret.add(str(x))
    ret = [eval(i) for i in ret]
    return ret

if __name__ == '__main__':
    print(sum3([-1, 0, 1, 2, -1, -4]))

# vim: ai sw=4 ts=4 et showmatch
