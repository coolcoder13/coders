def ROTATE(llist, p):
    
    #making head,head1 pointing to llist.head
    head=llist.head
    head1=llist.head
    
    while p>0:
        head1=head1.next
        p-=1
    
    # for this list making 20.next as NONE
    head1.prev.next=None
    
    # for this example making 30.prev as NONE
    head1.prev=None
    
    #for this exmaple making 30 as head of DLL(llist.head)
    llist.head=head1
    
    temp=head1
    while temp.next:
        temp=temp.next
    temp.next=head
    head.prev=temp
    
    return llist




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None



class LinkedList:
    def __init__(self):
        self.head=None
        
    def display(self):
        t=self.head
        while t:
            print(t.data,end=' ')
            t=t.next
        print()


if __name__ == "__main__":
    
    #no of elements in DLL
    n = 6
    
    #no of rotations to do in DLL
    p = 2
    
    l = [10,20,30,40,50,60]
    llist = LinkedList()
    
    #creating DLL by elements of list
    for i in range(n):
        ptr = Node(l[i])
        if llist.head==None:
            llist.head=ptr
            cur=ptr
        else:
            cur.next = ptr
            ptr.prev = cur
            cur = ptr

    ROTATE(llist, p)
    
    llist.display()