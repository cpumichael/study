
'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''

def merge(a, b):
    ret = []
    i, j = 0, 0
    a_end = len(a)
    b_end = len(b)

    while i < a_end and j < j_end:
        if a[i] < b[j]:
            ret.append(a[i])
            i += 1
        if a[i] == b[j]:
            ret.append(a[i])
            i += 1
            j += 1
        if b[j] < a[i]:
            ret.append(b[j])
            j += 1

    while i < a_end:
        ret.append(a[i])
        i += 1

    while j < b_end:
        ret.append(b[j])
        j += 1

    return ret

# vim: ai sw=4 ts=4 et showmatch
