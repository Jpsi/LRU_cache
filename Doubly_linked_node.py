class Doubly_linked_node:
  def __init__(self):
    self.__next = None
    self.__previous = None

  def next(self):
    return self.__next

  def previous(self):
    return self.__previous

  def set_next(self, node):
    self.validate_type(node)
    if self.__next:
      self.__next.__previous = None
    self.__next = node
    if node:
      if node.__previous:
        node.__previous.__next = None
      node.__previous = self

  def set_previous(self, node):
    self.validate_type(node)
    if self.__previous:
      self.__previous.__next = None
    self.__previous = node
    if node:
      if node.__next:
        node.__next.__previous = None
      node.__next = self

  def validate_type(self, node):
    if node is not None and not isinstance(node, Doubly_linked_node):
      raise TypeError("Argument must be a Doubly_linked_node")
