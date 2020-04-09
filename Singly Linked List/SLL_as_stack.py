class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class Stack:
    
    def __init__(self):
        self.head=None
        
    # The method push to push element into stack    
    def push(self, data):
        ins = Node(data)
        
        if self.head is None:
            self.head=ins
            ins.next=None
            return
        
        ins.next=self.head
        self.head=ins
        return
        
        
    # The method pop which return the element poped out of the stack
    def pop(self):

        if self.head is None:
            return -1
        
        q=self.head
        self.head=self.head.next
        x=q.data
        q=None
        return x



#output of code is either -1 is stack is empty or elements which are popped

if __name__ == '__main__':
    s = Stack()
    q = 4                                  # no of opearations to be performed
    
    # list contains operations of two types
    #        1,o    where 1 represents that element o is to be pushed into stack
    #        2      where 2 represents pop operation is to be performed
    l = [2 ,1 ,4 ,1 ,5 ,2]
    i = 0
    while i < len(l):
        if l[i] == 1:
            s.push(l[i + 1])
            i = i + 2
        elif l[i] == 2:
            print(s.pop(), end=" ")
            i = i + 1
    print()