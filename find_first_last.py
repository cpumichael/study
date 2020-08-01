
'''
Given an array of integers nums sorted in ascending
order, find the starting and ending position of a
given target value.

Your algorithm's runtime complexity must be in the
order of O(log n).

If the target is not found in the array,
return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

def f(a, t, lo, hi, ret):
    if lo < hi:
        mid = hi - lo
        if t < a[mid]:
            f(a, t, 0, mid-1, ret)
        elif t > a[mid]:
            f(a, t, mid+1, hi, ret)
        else:
            ret.append(mid)
            f(a, t, lo, mid-1, ret)
            f(a, t, mid+1, hi, ret)

def fd(a, t):
    ret = []
    if len(a) == 1 and a[0] == t:
        return [0]
    if len(a) == 1 and a[0] != t:
        return [-1, -1]

    f(a, t, 0, len(a)-1, ret)

    if ret:
        return ret
    else:
        return [-1, -1] # why????

if __name__ == '__main__':
    a = [5,7,7,8,8,10]
    print(fd(a, 8))
    a = [5,7,7,8,8,10]
    print(fd(a, 6))
    a = [1]
    print(fd(a, 1))
    print(fd(a, 9))

# vim: ai sw=4 ts=4 et showmatch
