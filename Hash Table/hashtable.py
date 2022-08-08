class HashTable():
    def __init__(self):
        self.arr = [None] * 10

    def printAll(self):
        print(self.arr)

    def getHash(self, string):
        h=0
        for char in string:
            h += ord(char)
        return h%10

    def __setitem__(self, key, value):
        h = self.getHash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.getHash(key)
        return self.arr[h]

if __name__ == "__main__":
    ht = HashTable()
    ht["march 1"] = 31
    ht["march 2"] = 32
    ht["march 3"] = 33
    ht.printAll()
    print(ht["march 1"])