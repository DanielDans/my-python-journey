class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string: str):
        result = 0
        for char in string:
            result += ord(char)
        return result

    def add(self, key: dict, value: dict):
        hash_val = self.hash(key)

        if hash_val not in self.collection:
            self.collection[hash_val] = {}

        self.collection[hash_val][key] = value

    def remove(self, key: dict):
        hash_val = self.hash(key)

        if hash_val in self.collection and key in self.collection[hash_val]:
            del self.collection[hash_val][key]

    def lookup(self, key: dict):
        hash_val = self.hash(key)

        if hash_val in self.collection and key in self.collection[hash_val]:
            return self.collection[hash_val][key]
        return None

# wasnt too hard