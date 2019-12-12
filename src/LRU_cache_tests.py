import unittest
from LRU_cache import LRU_cache, Cache_error, Cache_error_Item_not_found

test_data = {"oranges":33, "apples":41, "pears":89, "lemons":11, "berries":3}

class LRU_cache_tests_Constructor_and_methods(unittest.TestCase):
  def test_class_exists(self):
    cache = LRU_cache()
    self.assertIsInstance(cache, LRU_cache)

  def test_When_integer_passed_to_constructor_Then_size_is_value_passed(self):
    cache = LRU_cache(4)
    self.assertEqual(cache.size, 4)

  def test_When_no_value_passed_to_constructor_Then_default_size_is_1(self):
    cache = LRU_cache()
    self.assertEqual(cache.size, 1)

  def test_When_integer_less_than_1_passed_to_constructor_Then_exception(self):
    self.assertRaises(Cache_error, LRU_cache, 0)
    self.assertRaises(Cache_error, LRU_cache, -1)

  def test_When_non_integer_passed_to_constructor_Then_exception(self):
    self.assertRaises(Cache_error, LRU_cache, "chocolate")
    self.assertRaises(Cache_error, LRU_cache, 1.2)
    self.assertRaises(Cache_error, LRU_cache, [1])
    self.assertRaises(Cache_error, LRU_cache, {1})
    self.assertRaises(Cache_error, LRU_cache, {1:1})

  def test_can_store_data(self):
    cache = LRU_cache()
    cache.put("oranges", test_data["oranges"])
    self.assertEqual(cache.get("oranges"), test_data["oranges"])

  def test_can_evict_data(self):
    cache = LRU_cache()
    cache.put("oranges", test_data["oranges"])
    cache.evict()
    self.assertRaises(Cache_error_Item_not_found, cache.get, "oranges")

class LRU_cache_tests_Given_empty_cache(unittest.TestCase):
  def setUp(self):
    self.cache = LRU_cache()

  def test_Given_empty_cache_Then_head_is_None(self):
    self.assertIsNone(self.cache.head)

  def test_Given_empty_cache_Then_tail_is_None(self):
    self.assertIsNone(self.cache.tail)

  def test_Given_empty_cache_When_get_item_Then_exception(self):
    self.assertRaises(Cache_error_Item_not_found, self.cache.get, "oranges")

  def test_Given_empty_cache_When_evict_Then_exception(self):
    self.assertRaises(Cache_error, self.cache.evict)

class LRU_cache_tests_Given_1_item(unittest.TestCase):
  def setUp(self):
    self.cache = LRU_cache(5)
    self.cache.put("oranges", test_data["oranges"])

  def test_Given_1_item_Then_it_is_both_head_and_tail(self):
    self.assertEqual(self.cache.head.id, "oranges")
    self.assertEqual(self.cache.head, self.cache.tail)

  def test_Given_1_item_When_evict_Then_head_is_None(self):
    self.cache.evict()
    self.assertIsNone(self.cache.head)

  def test_Given_1_item_When_evict_Then_tail_is_None(self):
    self.cache.evict()
    self.assertIsNone(self.cache.tail)

  def test_Given_1_item_When_evict_twice_Then_exception(self):
    self.cache.evict()
    self.assertRaises(Cache_error, self.cache.evict)

class LRU_cache_tests_Given_4_items(unittest.TestCase):
  def setUp(self):
    self.cache = LRU_cache(5)
    self.cache.put("oranges", test_data["oranges"])
    self.cache.put("apples", test_data["apples"])
    self.cache.put("lemons", test_data["lemons"])
    self.cache.put("pears", test_data["pears"])

  def test_Given_4_items_Then_tail_points_to_firstIn_item(self):
    self.assertEqual(self.cache.tail.id, "oranges")
    self.assertEqual(self.cache.tail.data, test_data["oranges"])

  def test_Given_4_items_Then_head_points_to_lastIn_item(self):
    self.assertEqual(self.cache.head.id, "pears")
    self.assertEqual(self.cache.head.data, test_data["pears"])

  def test_Given_4_items_When_get_item_Then_tail_points_to_LRU_item(self):
    self.cache.get("oranges")
    self.assertEqual(self.cache.tail.id, "apples")
    self.assertEqual(self.cache.tail.data, test_data["apples"])

  def test_Given_4_items_When_get_item_Then_head_points_to_last_item_got(self):
    self.cache.get("oranges")
    self.assertEqual(self.cache.head.id, "oranges")
    self.assertEqual(self.cache.head.data, test_data["oranges"])

  def test_Given_4_items_When_get_item_Then_old_head_is_previous_to_new_head(self):
    self.cache.get("oranges")
    self.assertEqual(self.cache.head.previous().id, "pears")
    self.assertEqual(self.cache.head.previous().data, test_data["pears"])

  def test_Given_4_items_When_get_head_Then_head_does_not_change(self):
    self.assertEqual(self.cache.head.id, "pears")
    self.cache.get("pears")
    self.assertEqual(self.cache.head.id, "pears")

  def test_Given_4_items_When_get_item_Then_previous_of_item_old_next_is_item_old_previous(self):
    self.cache.get("apples")
    self.assertEqual(self.cache.items["lemons"].previous().id, "oranges")
    self.assertEqual(self.cache.items["lemons"].previous().data, test_data["oranges"])

  def test_Given_4_items_When_get_item_Then_next_of_item_old_previous_is_item_old_next(self):
    self.cache.get("apples")
    self.assertEqual(self.cache.items["oranges"].next().id, "lemons")
    self.assertEqual(self.cache.items["oranges"].next().data, test_data["lemons"])

  def test_Given_4_items_When_get_item_Then_new_tail_has_no_previous(self):
    self.cache.get("oranges")
    self.assertIsNone(self.cache.tail.previous())

  def test_Given_4_items_When_get_item_Then_new_head_has_no_next(self):
    self.cache.get("oranges")
    self.assertIsNone(self.cache.head.next())

  def test_Given_4_items_When_evict_Then_tail_points_to_LRU_item(self):
    self.cache.evict()
    self.assertEqual(self.cache.tail.id, "apples")
    self.assertEqual(self.cache.tail.data, test_data["apples"])

  def test_Given_4_items_When_evict_Then_new_tail_has_no_previous(self):
    self.cache.evict()
    self.assertIsNone(self.cache.tail.previous())

  def test_Given_4_items_When_evict_Then_only_firstIn_item_is_evicted(self):
    self.cache.evict()
    self.assertRaises(Cache_error_Item_not_found, self.cache.get, "oranges")
    self.assertEqual(self.cache.get("apples"), test_data["apples"])
    self.assertEqual(self.cache.get("lemons"), test_data["lemons"])
    self.assertEqual(self.cache.get("pears"), test_data["pears"])

  def test_Given_4_items_When_evict_Then_only_LRU_item_is_evicted(self):
    self.cache.get("oranges")
    self.cache.evict()
    self.assertRaises(Cache_error_Item_not_found, self.cache.get, "apples")
    self.assertEqual(self.cache.get("oranges"), test_data["oranges"])
    self.assertEqual(self.cache.get("lemons"), test_data["lemons"])
    self.assertEqual(self.cache.get("pears"), test_data["pears"])


class LRU_cache_tests_Given_full_cache(unittest.TestCase):
  def setUp(self):
    self.cache1 = LRU_cache(1)
    self.cache1.put("oranges", test_data["oranges"])

    self.cache4 = LRU_cache(4)
    self.cache4.put("oranges", test_data["oranges"])
    self.cache4.put("apples", test_data["apples"])
    self.cache4.put("lemons", test_data["lemons"])
    self.cache4.put("pears", test_data["pears"])

  def test_Given_full_cache_of_size_1_When_new_item_is_put_Then_old_item_is_evicted(self):
    self.cache1.put("apples", test_data["apples"])
    self.assertRaises(Cache_error_Item_not_found, self.cache1.get, "oranges")

  def test_Given_full_cache_of_size_1_When_new_item_is_put_Then_new_item_is_stored(self):
    self.cache1.put("apples", test_data["apples"])
    self.assertEqual(self.cache1.get("apples"), test_data["apples"])

  def test_Given_full_cache_of_size_4_When_new_item_is_put_Then_LRU_item_is_evicted(self):
    self.cache4.get("oranges")
    self.cache4.put("berries", test_data["berries"])
    self.assertRaises(Cache_error_Item_not_found, self.cache4.get, "apples")

  def test_Given_full_cache_of_size_4_When_new_item_is_put_Then_new_item_is_stored(self):
    self.cache4.get("oranges")
    self.cache4.put("berries", test_data["berries"])
    self.assertEqual(self.cache4.get("berries"), test_data["berries"])

class LRU_cache_tests_Special_cases(unittest.TestCase):
  def test_Given_cache_contains_item_When_same_id_is_used_for_new_item_Then_exception(self):
    cache = LRU_cache(2)
    cache.put("oranges", test_data["oranges"])
    self.assertRaises(Cache_error, cache.put, "oranges", test_data["apples"])

  def test_complex_sequence_of_operations(self):
    cache = LRU_cache(4)
    cache.put("oranges", test_data["oranges"])
    cache.put("apples", test_data["apples"])
    cache.get("oranges")
    cache.put("lemons", test_data["lemons"])
    cache.put("pears", test_data["pears"])
    cache.get("oranges")
    cache.get("apples")
    cache.get("pears")
    cache.put("berries", test_data["berries"])
    cache.get("apples")
    self.assertEqual(cache.head.id, "apples")
    self.assertEqual(cache.head.previous().id, "berries")
    self.assertEqual(cache.head.previous().previous().id, "pears")
    self.assertEqual(cache.head.previous().previous().previous().id, "oranges")
    self.assertEqual(cache.tail.id, "oranges")
    self.assertRaises(Cache_error_Item_not_found, cache.get, "lemons")

if __name__ == "__main__":
  unittest.main()