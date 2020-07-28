
'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

'''

def group_anagrams(a):
    i = 0
    while i < len(a):
        ana = set(a[i])
        print(a[i])
        j = i + 1
        while j < len(a):
            if set(a[j]) == ana:
                print(a[j])
                del a[j]
            else:
                j += 1
        i += 1
   
group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])


# vim: ai sw=4 ts=4 et showmatch
