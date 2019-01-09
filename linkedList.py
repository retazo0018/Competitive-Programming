class node:
    def __init__(self,info=None,next_node=None):
        self.info = info
        self.next_node = next_node
    def get_info(self,info):
        return self.info
    def get_next(self):
        return self.next_node
    def set_next(self,new_next):
        self.next_node = new_next
class linked_list(node):
    def __init__(self,head=None):
        self.head = head
    def insert(self,info):
        new_node = node(info)
        new_node.set_next(head)
        self.head = new_node
    def size(self):
        cur = self.head
        count=0
        while cur:
            count+=1
            cur = cur.get_next()
        return count
    def delete(self,info):
        prev = None
        cur = cur.head
        found = False
        while found and prev is not True:
            if(cur.get_info()==info):
                found = True
            else:
                prev = cur.head()
                cur = cur.next()
            if(cur is None):
                raise ValueError("Data not found!")
            if(prev is None):
                self.head = cur.get_next()
            else:
                prev.set_next(cur.get_next())
obj = linked_list()
