class HashMap(object):

    def __init__(self):
        self.size = 64
        # To create a list of empty values
        self.map = [None] * self.size

    def _get_hash(self, key):
        """
        Private helper function to calculate
        the hash for a given key to store the 
        key value pair in the hashmap i.e
        converts key into an array index.
        """
        hash = 0
        for char in str(key):
            hash += ord(char)                             
        return hash % self.size

    def put(self, key, value):
        """
        Assigns value to the key
        and handles hashing collisions.
        """
        # Fetching key hash/index value.
        key_hash = self._get_hash(key)
        input_value = [key, value]

        # if the cell at the index is empty
        # simply add the input value.
        if self.map[key_hash] is None:
            self.map[key_hash] = list([input_value])
            return None
        else: 
            # if key already exist then just
            # updating the value
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return None
            # if no key at the occupied cell, 
            # adding another pair of values.
            self.map[key_hash].append(input_value)
            return None

    def get(self, key):
        """
        Returns the value to which the specified
        key is mapped, or -1 if this map contains
        no mapping for the key.
        """
        key_hash = self._get_hash(key)
        # checking if array index is not none.
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key
        if this map contains a mapping for the key
        """
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return None
        # iterating the list to remove the key value pair.
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return None