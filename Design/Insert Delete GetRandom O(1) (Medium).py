# 380. Insert Delete GetRandom O(1) - Medium
# Tags - Array, Hash Table, Design

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        self.indexdict = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.indexdict:
            return False
        else:
            self.lst.append(val)
            self.indexdict[val] = len(self.lst) - 1
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.indexdict:
            index = self.indexdict[val]
            self.lst[index], self.lst[-1] = self.lst[-1], self.lst[index]
            self.indexdict[self.lst[index]] = index
            self.lst.pop()
            self.indexdict.pop(val, None)
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        r = random.randint(0, len(self.lst)-1)
        return self.lst[r]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()