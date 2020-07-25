'''
Given a string, find the length of the longest substring
T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.

Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
'''

def long_ss(s, k):
    ss = set()
    ll = []
    longest = 0
    for start in range(len(s)):
        for i in s[start:]:
            ss.add(i)
            ll.append(i)
            if len(ss) > k:
                ss = set()
                ll = []
                continue
            if len(ll) > longest:
                longest = len(ll)
        ss = set()
        ll = []

    return longest


if __name__ == '__main__':
    from collections import namedtuple
    Test = namedtuple('Test', ['str', 'k'])
    tests = [
        Test('aa', 1),
        Test('eceba', 2),
        Test('ecebabaxaxaxa', 2),
        Test('michchhael', 3)
    ]

    for i, t in enumerate(tests):
        print(f'Inp {i}: {t}')
        l = long_ss(t.str, t.k)
        print(f'Out {i}: {l}')

# vim: ai sw=4 ts=4 et showmatch
