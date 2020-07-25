
'''
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Example:

Input:  [0,1,0,3,12]
Output: [1,3,12,0,0]

Input:  [1,0,3,12]
Output: [1,3,12,0]

'''

class MyIntArr(list):
    def __init__(self, arr=None):
        if arr is None:
            super().__init__()
        else:
            super().__init__(arr)

    def mv0(self):
        '''moves all 0 integer values to end of array in place'''
        i = 0
        deleted = 0
        while i < self.__len__():
            if self.__getitem__(i) == 0:
                self.__delitem__(i)
                deleted += 1
            else:
                i += 1
        self.extend([0] * deleted)


def test(i, arr):
    print(f"Inp: {i}", arr)
    arr.mv0()
    print(f"Out: {i}", arr)

for i, t in enumerate([
           MyIntArr(),
           MyIntArr('foo'),
           MyIntArr([0,0,0,3,2,1]),
           MyIntArr([0,1,0,0,0,8]),
           MyIntArr([8,3,0,0,0,3]),
           MyIntArr([0,0,0,0,5,2,0]),
           MyIntArr([0]),
           MyIntArr([0,1,0,3,12]),
           MyIntArr([1,0,3,12])
          ]):

    test(i, t)

# vim: ai sw=4 ts=4 et showmatch
