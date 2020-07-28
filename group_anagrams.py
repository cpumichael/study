
'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate", "eat", "tea"],
  ["nat", "tan"],
  ["bat"]
]

'''

def group_anagrams(a):
    ret = []
    i = 0
    while i < len(a):
        print('i=',i)
        ana = set(a[i])
        ret.append(a[i])
        print(a[i])
        j = i + 1
        while j < len(a):
            if set(a[j]) == ana:
                print(ret)
                #ret[i].append(a[j])
                print(a[j])
                del a[j]
            else:
                j += 1
        i += 1
   
group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])


# vim: ai sw=4 ts=4 et showmatch
