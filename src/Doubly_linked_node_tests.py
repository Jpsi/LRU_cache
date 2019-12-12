import unittest
from Doubly_linked_node import Doubly_linked_node

class Doubly_linked_node_tests(unittest.TestCase):
  def test_class_exists(self):
    node = Doubly_linked_node()
    self.assertIsInstance(node, Doubly_linked_node)

  def test_When_no_previous_Then_previous_is_None(self):
    node = Doubly_linked_node()
    self.assertIsNone(node.previous())

  def test_When_no_next_Then_next_is_None(self):
    node = Doubly_linked_node()
    self.assertIsNone(node.next())

  def test_can_link_to_next_node(self):
    node1 = Doubly_linked_node()
    node2 = Doubly_linked_node()
    node1.set_next(node2)
    self.assertIs(node1.next(), node2)

  def test_can_link_to_previous_node(self):
    node1 = Doubly_linked_node()
    node2 = Doubly_linked_node()
    node1.set_previous(node2)
    self.assertIs(node1.previous(), node2)

  def test_When_set_next_not_supplied_object_of_this_class_Then_exception(self):
    node = Doubly_linked_node()
    self.assertRaises(TypeError, node.set_next, "sldkfj")

  def test_When_set_next_not_supplied_object_of_this_class_Then_exception(self):
    node = Doubly_linked_node()
    self.assertRaises(TypeError, node.set_previous, "sldkfj")

  def test_When_node2_is_set_next_of_node1_Then_node1_is_previous_of_node2(self):
    node1 = Doubly_linked_node()
    node2 = Doubly_linked_node()
    node1.set_next(node2)
    self.assertIs(node2.previous(), node1)

  def test_When_node2_is_set_previous_of_node1_Then_node1_is_next_of_node2(self):
    node1 = Doubly_linked_node()
    node2 = Doubly_linked_node()
    node1.set_previous(node2)
    self.assertIs(node2.next(), node1)

  def test_Given_node_has_previous_When_new_previous_is_set_Then_old_previous_has_no_next(self):
    node1 = Doubly_linked_node()
    node2 = Doubly_linked_node()
    node2.set_previous(node1)
    node3 = Doubly_linked_node()
    node2.set_previous(node3)
    self.assertIsNone(node1.next())

  def test_Given_node_has_next_When_new_next_is_set_Then_old_next_has_no_previous(self):
    node1 = Doubly_linked_node()
    node2 = Doubly_linked_node()
    node2.set_next(node1)
    node3 = Doubly_linked_node()
    node2.set_next(node3)
    self.assertIsNone(node1.previous())

  def test_Given_node_has_previous_When_previous_set_as_previous_of_another_node_Then_node_has_no_previous(self):
    node1 = Doubly_linked_node()
    node2 = Doubly_linked_node()
    node2.set_previous(node1)
    node3 = Doubly_linked_node()
    node3.set_previous(node1)
    self.assertIsNone(node2.previous())

  def test_Given_node_has_next_When_next_set_as_next_of_another_node_Then_node_has_no_next(self):
    node1 = Doubly_linked_node()
    node2 = Doubly_linked_node()
    node2.set_next(node1)
    node3 = Doubly_linked_node()
    node3.set_next(node1)
    self.assertIsNone(node2.next())

  def test_can_set_previous_to_None(self):
    node1 = Doubly_linked_node()
    node2 = Doubly_linked_node()
    node2.set_previous(node1)
    node2.set_previous(None)
    self.assertIsNone(node2.previous())

  def test_can_set_next_to_None(self):
    node1 = Doubly_linked_node()
    node2 = Doubly_linked_node()
    node2.set_next(node1)
    node2.set_next(None)
    self.assertIsNone(node2.next())

if __name__ == "__main__":
  unittest.main()