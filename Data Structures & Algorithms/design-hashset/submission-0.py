class MyHashSet:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.hashSet = None

    def add(self, key: int) -> None:
        if self.hashSet is None:
            self.hashSet = self.Node(key)
        else:
            curr = self.hashSet
            
            while curr.next:
                if curr.data == key:
                    return
                curr = curr.next
            
            if curr.data == key:
                return
            else:
                newNode = self.Node(key)
                curr.next = newNode    

    def remove(self, key: int) -> None:
        if self.hashSet is None:
            return
        else:
            curr = self.hashSet
            if curr.data == key:
                self.hashSet = curr.next # Python garbage collector takes care of unreferenced Node
                return

            prev = curr
            while curr.next:
                if curr.data == key:
                    prev.next = curr.next
                    return
                prev = curr
                curr = curr.next
            
            if curr.data == key:
                prev.next = None

    def contains(self, key: int) -> bool:
        if self.hashSet is None:
            return False
        
        curr = self.hashSet
        
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)