
'''
Given an array nums of n integers where n > 1,
return an array output such that output[i] is
equal to the product of all the elements of
nums except nums[i].

Cannot use division.

Solve in O(n)

Input:  [1,2,3,4]
Output: [24,12,8,6]

Correct answer with division:

mul all elements
for each element divide by that element

'''

def mul_not_self(a):
  ret = []
  x = 1
  for i in a:
    x *= i
  for i in a:
    ret.append(x // i)
  return ret

def mul_not_self_inplace(a):
  x = 1
  for i in a:
    x *= i
  for i in range(len(a)):
    a[i] = x // a[i]

print(mul_not_self([1,2,3,4]))
a = [4,5,1,8,2,10,6]
mul_not_self_inplace(a)
print(a)

# vim: ai sw=2 ts=2 et showmatch
