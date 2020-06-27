class HashMap:
    def __init__(self):
        self.arr = [[] for x in range(10)]

    def get_hash(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % 10

    def __getitem__(self, index):
        h = self.get_hash(index)
        for element in self.arr[h]:
            if element[0] == index:
                return element[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))

    def __delitem__(self, key):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h].remove(element)
                found = True
                break
        if not found:
            print('Element %s not present in the Table' % key)

    def max_value(self):
        maxi = max(self.arr)
        
        if len(maxi) > 1:
            ans = 0
            for value in (maxi):
                if value[1]>ans:
                    ans = value[1]
            return ans
        return maxi[0][1]

t = HashMap()
t['march 12'] = 170
t['march 6'] = 120
t['march 17'] = 130
print(t.arr)
del t['march 17']
print(t.max_value())