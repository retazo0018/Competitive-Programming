class node(object):
    def __init__(self,info=None,next_node=None):
        self.info = info
        self.next_node = next_node
    def get_info(self):
        return self.info
    def get_next(self):
        return self.next_node
    def set_next(self,new_next):
        self.next_node = new_next
        
        
class linked_list(object):
    def __init__(self,head=None):
        self.head = head
    def insert(self,info):
        new_node = node(info)
        new_node.set_next(self.head)
        self.head = new_node
    def size(self):
        cur = self.head
        count=0
        while cur:
            count+=1
            cur = cur.get_next()
        return count
    def delete(self,info):
        cur = self.head
        previous = None
        found = False
        while cur and found is False:
            if cur.get_info() == info:
                found = True
                print("Deleted!")
            else:
                previous = cur
                current = cur.get_next()
        if cur is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = cur.get_next()
        else:
            previous.set_next(cur.get_next())
    def search(self, info):
        cur = self.head
        found = False
        while(cur and found is not True):
            if(cur.get_info()==info):
                print("Data is found")
                found = True
            else:
                cur = cur.get_next()
        if(cur is None):
                raise ValueError("Data not found!")
obj = linked_list()
obj.insert('1')
obj.insert('2')
obj.insert('3')
obj.insert('4')
obj.insert('5')
obj.insert('6')
obj.size()
obj.search('6')
obj.delete('6')
obj.size()
