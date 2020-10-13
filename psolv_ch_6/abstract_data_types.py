# We declare some new abstract data types

# First is the MAP ADT which is another name for dictionary

class HashTable:
    """Hash Table data type, size should be a prime number for more efficient collision resolution"""

    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self, key):
        """
        Simple hash function thet uises the modulo division to determine the slot where data is stored
        :param key: int | str | float
        :return: slot: int
        """
        key_value = key
        if type(key) == str:
            # Implementing string kley conversion with weighting to avoid collision of similar strings
            key_value = sum(ord(c) * i for i, c in enumerate(key))

        return key_value % self.size

    def rehash(self, old_hash):
        """Recalculate another slot if old slot is takem. We a using a constant value to evaluate the new slot"""
        return (old_hash + 1) % self.size

    def put(self, key, data):
        """Put a new value in the hash table, key value pair has to be provided because well the key is used
        for hashing"""
        if None not in self.slots:
            print("Table is full")
            return 

        hashvalue = self.hash_function(key)

        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            # If they have already provided this key before, we replace
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data

            else:
                print(f"Collision found rehashing {key}")
                nextslot = self.rehash(hashvalue)
                while (self.slots[nextslot] is not None) and (self.slots[nextslot] != key):
                    nextslot = self.rehash(nextslot)

                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data

                else:
                    self.data[nextslot] = data

    def get(self, key):
        startslot = self.hash_function(key)

        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position)
                if position == startslot:
                    stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
