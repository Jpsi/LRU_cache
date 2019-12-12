from Doubly_linked_node import Doubly_linked_node

class LRU_cache:
  def __init__(self, size=1):
    if not isinstance(size, int):
      raise Cache_error("Size must be integer")
    if size < 1:
      raise Cache_error("Size must be greater than 0")
    self.size = size
    self.items = {}
    self.tail = None
    self.head = None

  def put(self, new_item_id, new_item_data):
    if new_item_id in self.items:
      raise Cache_error("Item with this ID already exists")
    self.items[new_item_id] = Doubly_linked_node()
    new_item = self.items[new_item_id]
    new_item.id = new_item_id
    new_item.data = new_item_data
    if len(self.items) == 1:
      self.tail = new_item
      self.head = self.tail
    else:
      new_item.set_previous(self.head)
      self.head = self.head.next()
    if len(self.items) > self.size:
      self.evict()

  def get(self, requested_item_id):
    if requested_item_id not in self.items:
      raise Cache_error_Item_not_found
    requested_item = self.items[requested_item_id]
    if len(self.items) > 1:
      if requested_item is self.tail:
        self.tail = requested_item.next()
      if requested_item is not self.head:
        requested_item.next().set_previous(requested_item.previous())
        requested_item.set_previous(self.head)
        self.head = requested_item
    return requested_item.data

  def evict(self):
    if not self.items:
      raise Cache_error("Cache empty - nothing to evict")
    del self.items[self.tail.id]
    if not self.items:
      self.tail = None
      self.head = None
    else:
      self.tail = self.tail.next()
      self.tail.set_previous(None)

class Cache_error(Exception):
  pass

class Cache_error_Item_not_found(Cache_error):
  pass
