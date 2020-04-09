# making of node of doubly linked list
class Node:
    def __int__(self,data):
        self.data=data
        self.prev=None
        self.next=None


#creating class with meathods to perform different tasks
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        
    # how to insert node in a doubly linked list
    def insert(self,n):
        m = Node()                #creating instance of class node
        m.data = n
        m.next=None
        if self.head is None:
            m.prev=None            #assign null to previous of node
            self.head=m
            return
        
        last=self.head
        
        #traversing DLL to asssign node to end of DLL
        while last.next is not None:
            last=last.next
            
        last.next=m               # adding newly created node to end of DLL
        m.prev=last
        return
    
            
    # printing of DLL
    def display(self):
        t=self.head
        while t is not None:
            print(t.data,end=' ')
            t=t.next
        print()


# deleting element at position x from DLL

def DeleteNode(head, x):
    
    if x==1:
        head=head.next
        head.prev=None
    c=2
    t=head
    while t.next:
        if c==x:
            t.next=t.next.next
            
            # to avoid error of Nonetype
            if t.next:
                if t.next.next:
                    t.next.next.prev=t
            break
            
        c+=1
        t=t.next


if __name__=="__main__":
    n=4
    l=[1,5,2,9]
    a=DoublyLinkedList()   #creating instance
    for i in l:
        a.insert(i)
        
    pos = 3                #position to be deleted
    DeleteNode(a.head,pos)
    a.display()