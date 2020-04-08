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
    
    # printing of SLL
    def display(self):
        t=self.head
        while t:
            print(t.data,end=' ')
            t=t.next
        print()
        
    #making a loop
    def createloop(self,n):
        if n==0:
            return None
        
        t=self.head
        p=self.head
        c=1
        while c!=n:
            p=p.next
            c+=1
        while t.next:
            t=t.next
        t.next=p

def isCircular(head):
    # Code here
    t=head
    while True:
        if t.next==None:
            return 0
        elif t.next==head:
            return 1
        t=t.next


if __name__ == '__main__':
    
    a=LinkedList()
    nodes=[16,25,34,43,52,61]    #list containing nodes
    isloop=1                     # 1 means it is a cicular SLL
    
    for x in nodes:   
        # create a new node
        node=Node(x)
        a.insert(node)
        
    if isloop:
        a.createloop(1)
        
    if isCircular(a.head):
        print('First Linked List is circular')
    else:
        print('Second Linked List is not circular')
        
        
        
    a=LinkedList()
    nodes=[16,25,34,43,52,61]    #list containing nodes
    isloop=0                     # 0 means it is not a cicular SLL
    
    for x in nodes:   
        # create a new node
        node=Node(x)
        a.insert(node)
        
    if isloop:
        a.createloop(1)
        
    if isCircular(a.head):
        print('First Linked List is circular')
    else:
        print('Second Linked List is not circular')