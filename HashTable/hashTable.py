class HashTable():
    def __init__(self):
        self.arr = [[] for i in range(10)]

    def printAll(self):
        for i in range(len(self.arr)):
            for element in self.arr[i]:
                print(f"{element[0]}: {element[1]}")

    def getHash(self, string):
        h=0
        for char in string:
            h += ord(char)
        return h%10

    def __setitem__(self, key, value):
        h = self.getHash(key)
        existing = False
        for idx, val in enumerate(self.arr[h]):
            if val[0] == key:
                self.arr[h][idx] = (key, value)
                existing = True
        if not existing:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.getHash(key)
        for k, value in self.arr[h]:
            if k == key:
                return value

    def __delitem__(self, key):
        h = self.getHash(key)
        for idx, value in enumerate(self.arr[h]):
            if value[0] == key:
                self.arr[h].pop(idx)

if __name__ == "__main__":
    ht = HashTable()
    ht["march 6"] = "6 init"
    ht["march 7"] = "7"
    ht["march 6"] = "6 new"
    ht["march 17"] = "17"
    ht.printAll()
    del ht["march 6"]
    print(ht["march 6"])