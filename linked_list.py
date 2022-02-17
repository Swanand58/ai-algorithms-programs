
class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Linked_list1:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        curr = self.head

        while curr.next!= None:
            curr = curr.next
        curr.next = new_node

    def lent(self):
        tot = 0
        cur = self.head

        while cur.next!=None:
            tot += 1
            cur = cur.next
        return tot

    def display(self):
        elem = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elem.append(cur_node.data)
        print(elem)


    def get(self, index):
        if index >= self.lent():
            print("ERROR")
            return None
        cur_ind = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_ind == index:
                return cur_node.data
            cur_ind += 1            

    def delete(self, index):
        if index >= self.lent():
            print("ERROR")
            return None
        cur_ind = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_ind == index:
                last_node.next = cur_node.next
                return
            cur_ind += 1         

my_ist = Linked_list1()
my_ist.append(0)
my_ist.append(1)
my_ist.append(10)
my_ist.append(3)
my_ist.append(4)
my_ist.display() 
x = my_ist.lent()
print(x)
print(my_ist.get(2))
my_ist.delete(4)
my_ist.display()            
