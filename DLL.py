#Node class, with getters and setters
class node:
    def __init__(self, data, next = None, previous = None):
        self.data = data
        self.next = next 
        self.previous = previous
    
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

    def set_data(self, data):
        self.data = data

    def set_data(self, next):
        self.next = next

    def set_previous(self, previous):
        self.previous = previous
    
#Linked list class 

class Linked_list(self, root = None):
    def __init__(self):
        self.root = root
        self.size = 0
        self.data = data
    
    def get_root(self):
        return self.root
    
    def get_size(self):
        return self.size
    
    def add(self, data):
        new_node = Node(data,self.root)
        self.root = new_node
        self.size += 1 
    
    def remove(self, data):
        this_node = self.root
        prev_node = None

        while this_node:
            if this_node.get_data() == data:
                if prev_node: 
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                    self.size -= one 
    
    def find(self, data):
        this_node = self.root
        while this_node:
            if this_node.get_data == data:
                return data
            else:
                this_node = this_node.get_next()
        return None
        


#instantiating 
n1 = node(1,2,None)
n2 = node(2,1,3)
n3 = node(3,None,2)