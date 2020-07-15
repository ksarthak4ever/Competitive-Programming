# HashMap problem solving challenge

## Design a HashMap without using any built-in hash table libraries

To be specific, your design should include these functions:

- `put(key, value)`: Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value
- `get(key)`: Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
- `remove(key)`: Remove the mapping for the value key if this map contains the mapping for the key

Example:

```python
hash_map = HashMap()
hash_map.put(1, 1)
hash_map.put(2, 2)
hash_map.get(1)            // returns 1
hash_map.get(3)            // returns -1 (not found)
hash_map.put(2, 1)         // update the existing value
hash_map.get(2)            // returns 1
hash_map.remove(2)         // remove the mapping for 2
hash_map.get(2)            // returns -1 (not found)
```

Note:

- All keys and values will be in the range of [0, 1000000].
- The number of operations will be in the range of [1, 10000].
- Please do not use the built-in HashMap library.

## Instructions

- Complete the code in `hashmap.py`
- Run tests
    `python -m unittest discover`



<!--
Dictionaries and lists share the following characteristics :~
1. Both are mutable.
2. Both are dynamic. They can grow and shrink as needed.
3. Both can be nested. A list can contain another list. A dictionary can contain another dictionary. A dictionary can also contain a list, and vice versa.

Dictionaries differ from lists primarily in how elements are accessed :~
1. List elements are accessed by their position in the list, via indexing.
2. Dictionary elements are accessed via keys.
-->

# Approach

As we know a hashmap is a key value pair data structure which has/works on 0(1) complexity for all put,get,delete functions. The keys of hashmap are unique in nature and collisions in hashmaps are handled using techniques like linear probing etc.

- I have used array as the data structure to implement the hashmap and created a small helper function to calculate the hash value for the keys i.e the array index for the keys based on the ASCII value of the key and mod of it's size. 

-This will randomly map the data across the array. The put method will add data/update data to the array and in case of collisions i'm appending the values to the array cell itself. The get method and remove method will fetch and remove key value pairs respectively.