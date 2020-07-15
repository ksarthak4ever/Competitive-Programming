import unittest

from hashmap import HashMap


class TestHashMap(unittest.TestCase):
    def test_hash_map(self):
        hash_map = HashMap()

        # Inserts
        hash_map.put(1, 1)
        hash_map.put(2, 2)
        self.assertEqual(hash_map.get(1), 1)
        self.assertEqual(hash_map.get(3), -1)

        # Updates
        hash_map.put(2, 1)
        self.assertEqual(hash_map.get(2), 1)

        # Delete
        hash_map.remove(2)
        self.assertEqual(hash_map.get(2), -1)
