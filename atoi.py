
''' implement an atoi() function like in C '''

import sys

def atoi(s):
   '''implements a crude atoi() function. Will ALWAYS return at least 0
   XXX shouldn't this throw and exception?'''
   a = list(s)
   while a.__len__() and a.__getitem__(0) == ' ':
      a.__delitem__(0)

   while a.__len__() and a.__getitem__(-1) == ' ':
      a.__delitem__(-1)

   mapping = {c:i for i,c in enumerate('0123456789')}

   negative = False

   digits = []
   for i, c in enumerate(a):
      if c == '-':
         negative = True
         continue
      if negative and c == '-': # undefined
         break
      tmp = mapping.get(c) # returns int(c) or None
      if tmp is not None:
         digits.append(tmp)
      else:
         break

   ret = 0
   for i, d in enumerate(reversed(digits)):
      print(f'ret = {ret}', file=sys.stderr)
      ret += (d * 10**i)

   if negative:
      ret = -ret
   
   return ret

samples = [
   '  6789 ',
   '   42 ',
   '   -42 ',
   ' --1 ',
   'alsdfkj',
   '42 a',
   '4',
]

for i, s in enumerate(samples):
   try:
      print('Inp {}: <<{}>>'.format(i, s.__repr__()))
      out = atoi(s)
      print('Out {}: <<{}>>'.format(i, out.__repr__()))
   except RuntimeError as e:
      print(s, e)

# vim: ai sw=3 ts=3 showmatch et
