
from collections import deque

class LRUCache:
  def __init__(self, size):
    # should really be a linked list, python deques are a bit odd
    # because near O(1) insertions and deletions at the top/bottom
    # O(n) in the middle, why????
    self._deque = deque([], size)
    self._dict = dict() # O(1) lookup
    self.misses = 0
    # self.lock = .... needs to be threadsafe

  def get(self, val):
    # lock the LRU...
    if not val in self._dict:
      self.misses += 1
      raise RuntimeError('not found')
    self._deque.remove(val)
    self._deque.appendleft(val)
    return val
    # unlock LRU

  def put(self, val):
    # lock the LRU...
    if val in self._dict:
      self._deque.remove(val)
      self._deque.appendleft(val)
      self._dict[val] += 1 # increment the hitcount
    else:
      if len(self._deque) == self._deque.maxlen:
        # full, so adjust LRU
        old_item = self._deque.pop()
        del self._dict[old_item]
        self._deque.appendleft(val)
        self._dict[val] = 1
      else:
        # simply add item
        self._deque.appendleft(val)
        self._dict[val] = 1

  def stats(self):
    '''prints contents and stats of hits'''
    # lock
    for i in self._deque:
      print(i, '->', self._dict[i])
    # unlock

if __name__ == '__main__':
  import random
  lru = LRUCache(5)
  for i in range(100):
    lru.put(random.randint(0, 9))

  lru.stats()

  print('Finding -3->12')
  for i in range(-3, 12):
    try:
      val = lru.get(i)
      print(val, "Found")
    except RuntimeError:
      print(i, "Not Found!") # wtf??? Why are lower values None
    
# vim: ai sw=2 ts=2 et showmatch
