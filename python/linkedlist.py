class Node(object):

    def __init__ (self, d, n = None):
        self.data = d
        self.next_node = n

    #gettter setter for the node
    def get_next (self):
        return self.next_node

    def set_next (self, n):
        self.next_node = n

    def get_data (self):
        return self.data

    def set_data (self, d):
        self.data = d


class LinkedList (object):

    def __init__(self):
        self.root = None #when linked list is craeted root elemet will be None
        self.size = 0

    def get_size (self):
        return self.size

    def add (self, d):
        new_node = Node (d, self.root) #create the new node  with the data and next node poiting to thr root node that is the first element
        self.root = new_node #change the root node as newly added n
        self.size += 1

    def remove (self, d):
        this_node = self.root #start from the root node
        prev_node = None  #we need this because we are changing the nexr pointer of the node to to be deleted

        while this_node:
            if this_node.get_data() == d:
                if prev_node: # this mean node does is not the first node
                    prev_node.set_next(this_node.get_next())
                else: #if node is the first node then change the root node to the next node so that first node is automatically neglected
                    self.root = this_node.get_next()
                self.size -= 1
                return True		# data removed
            else: #if the node is not the node ti be found then go to the next node
                prev_node = this_node
                this_node = this_node.get_next()
        return False  # data not found

    def find (self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None

myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
print("size="+str(myList.get_size()))
myList.remove(8)
print("size="+str(myList.get_size()))
print(myList.remove(12))
print("size="+str(myList.get_size()))
print(myList.find(5))