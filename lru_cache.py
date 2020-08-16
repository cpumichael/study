
from collections import deque

class LRUCache:
  def __init__(self, size):
    # should really be a linked list, python deques are a bit odd
    # because near O(1) insertions and deletions at the top/bottom
    # O(n) in the middle, why????
    self._deque = deque([], size)
    self._dict = dict() # O(1) lookup
    # self.lock = .... needs to be threadsafe

  def get(self, val):
    # lock the LRU...
    if not val in self._dict:
      raise RuntimeError('not found')
    self._deque.remove(val)
    self._deque.appendleft(val)
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
    for i in self._deque:
      print(i, '->', self._dict[i])

if __name__ == '__main__':
  import random
  lru = LRUCache(5)
  for i in range(100):
    lru.put(random.randint(0, 9))
  lru.stats()

  print('Finding 0->19')
  for i in range(20):
    try:
      val = lru.get(i)
      print(val, "Found")
    except RuntimeError:
      print(i, "Not Found!")
    
# vim: ai sw=2 ts=2 et showmatch
