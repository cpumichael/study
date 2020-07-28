
'''
Given a sorted array nums, remove the duplicates in-place
such that each element appear only once and return
the new length.

Do not allocate extra space for another array, you
must do this by modifying the input array in-place
with O(1) extra memory.
'''


def rmdups(a):
    i = 0
    end = len(a)
    while i < len(a):
        t0 = a[i]
        i += 1
        while i < len(a) and a[i] == t0:
            del a[i]

if __name__ == '__main__':
    def test(a):
        print(a)
        rmdups(a)
        print(a)

    test([1,1,2,3,4])
    test([1,1,2,3,3,3,3,4])
    test([1,1,2,3,3,3,3,4,4,4,4,4])

# vim: ai sw=4 ts=4 et showmatch
