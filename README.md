# LRU Cache

## Description

A LRU cache is a data structure in which items are oganised by order of use. If the cache is full and a new item must be stored, then the Least Recently Used (LRU) item is evicted from the cache.

## Quick-start guide

1. Run the tests using `python3 run_all_tests.py`. All 49 tests should pass. They are written using Python's built-in unittest module.

2. See below for sample usage (also in `sample_usage.py`)

~~~python
from LRU_cache import LRU_cache, Cache_error_Item_not_found

# Initialize a cache object
cache = LRU_cache(size=3) # Default cache size is 1

# Store data into the cache
cache.put(new_item_id="apples", new_item_data=33)
cache.put(new_item_id="oranges", new_item_data=11)
cache.put(new_item_id="pears", new_item_data=78)

# Get an item from the cache using the item ID
print("Oranges: ", cache.get("oranges")) # 11

# Get the least recently used item
print("Tail ID: ", cache.tail.id) # apples
print("Tail data: ", cache.tail.data) # 33

# Get the most recently used item
print("Head ID: ", cache.head.id) # oranges
print("Head data: ", cache.head.data) # 11

# Putting a new item when the cache is at capacity results in evicting the LRU item
cache.put(new_item_id="berries", new_item_data=64)
print("Tail ID: ", cache.tail.id) # pears
print("Tail data: ", cache.tail.data) # 78
try:
  print(cache.get("apples"))
except Cache_error_Item_not_found:
  print("No apples in cache!")
~~~



## FAQ

**How is the LRU cache implemented?**

The LRU cache is implemented in the class `LRU_cache` using a hash table (a Python dictionary) and a doubly linked list (the `Doubly_linked_node` class). The dictionary is used to store items and ensure O(1) access, while the doubly linked list is used to sort them and ensure O(1) reordering, with the Least Recently Used item at the tail and the Most Recently Used item at the head.

**What is the intended behaviour if an item is not in the cache?**

`LRU_cache` raises a `Cache_error_Item_not_found` exception if it does not contain the item requested. It is up to the caller to put the item into the cache if required. E.g.:

```python
cache = LRU_cache()
cache.put(new_item_id="apples", new_item_data=33)
try:
  cache.get("oranges")
except Cache_error_Item_not_found:
  cache.put(new_item_id="oranges", new_item_data=read_from_disk("oranges"))
```

## Dependencies

- Python 3
