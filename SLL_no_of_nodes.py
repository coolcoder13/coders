# creating node by Node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#Single Linked list class
class LinkedList:
    def __init__(self):
        self.head=None

    # append at the end of the list
    def insert(self,new_node):
        if self.head is None:
            self.head=new_node
            return
        curr_node=self.head
        while curr_node.next is not None:
            curr_node=curr_node.next
        curr_node.next=new_node
    
# global function to count no of nodes in SLL
def Count(head_node):        # variable passed in head of list
    
    t=head_node
    count=0
    while t:
        count+=1
        t=t.next
    return count


# main() function
if __name__ == '__main__':
    n=6
    a=LinkedList()
    nodes=[16,25,34,43,52,61] #list containing nodes
    
    for x in nodes:
        
        # create a new node
        node=Node(x)
        a.insert(node)
        
    print("number of nodes in SLL is : %d"%(Count(a.head)))