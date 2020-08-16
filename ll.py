
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LL:
  def __init__(self, value=None):
    if value is not None:
      self.head = Node(value)
    else:
      self.head = None

  def append(self, value):
    if self.head is None:
      self.head = Node(value)
    else:
      curr = self.head
      while curr.next is not None:
        curr = curr.next
        curr.next = Node(value)

  def insert(self, value):
    n = Node(value)
    n.next = self.head
    self.head = n

  def delete(self, value):
    prev = None
    curr = self.head
    found = False
    while not found and curr is not None:
      if curr.value == value:
        found = True
        break
      prev = curr
      curr = curr.next

      if not found:
        raise IndexError('value not in list')

      if prev is None:
        self.head = curr.next
      else:
        prev.next = curr.next

  def show(self):
    print('-' * 10)
    if self.head is None:
      print('Empty')
      return
    curr = self.head
    print(curr.value)
    while curr.next is not None:
      curr = curr.next
      print(curr.value)

# vim: ai sw=2 ts=2 et showmatch :
