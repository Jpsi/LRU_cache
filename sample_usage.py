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