# making of node of single linked list
class node:
    def __int__(self,val):
        self.val=val
        self.next=None    


#creating class with meathods to perform different work
class LinkedList:
    def __init__(self):
        self.head=None
        
    # how to insert node in a single linked list
    def insert(self,n):
        if self.head==None:
            x=node()               #creating instance of class node
            x.data=n               #assigning value to the data of node
            x.next=None            #assign null to next of node
            self.head=x
        else:
            t=self.head
            
            #traversing SLL to asssign node to end of SLL
            while t.next:
                t=t.next
                
            x=node()               
            x.data=n               
            x.next=None            
            t.next=x               # adding newly created node to end of SLL
    
    def deleteAlt(self):
        if (self.head == None): 
            return

        # Initialize prev and node to be deleted
        prev = self.head
        now = prev.next

        while (prev != None and now != None):  

            # Change next link of previous node  
            prev.next = now.next

            # Free memory  
            now = None

            # Update prev and node  
            prev = prev.next
            if (prev != None):  
                now = prev.next
            
    # printing of SLL
    def display(self):
        t=self.head
        while t:
            print(t.data,end=' ')
            t=t.next
        print()



if __name__=="__main__":
    lis=LinkedList()
    n=6
    arr=[1,2,3,4,5,6]
    for i in arr:
        lis.insert(i)
    lis.display()
    lis.deleteAlt()
    lis.display()