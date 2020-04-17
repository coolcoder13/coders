def construct_2D_matrix(arr, n):
    l=[]
    
    #creating each element of arr(list) as Node having right and down attribute
    
    for i in arr:
        x=[]
        for j in i:
            x.append(Node(j))
        l.append(x)
        
    #going till 2nd last element of l(list)    
    for i in range(n-1):
        
        # example: standing at index a[0][0] and attaching a[0][1] to it
        for j in range(n-1):
            l[i][j].right=l[i][j+1]
            
        # for each element a[i][j],a[i][j+1],..... attaching i+1 th list as its 2D
        for j in range(n):
            l[i][j].down=l[i+1][j]
            
    # last list is attached to its upper list but is not assigned to eachother
    for j in range(n-1):
        l[-1][j].right=l[-1][j+1]
    
    return l[0][0]



class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None



class LinkedList:
    def __init__(self):
        self.head = None
        
    # printing linked list in form of 2D matrix
    def display(self):
        t=self.head
        while (t):
            t1 = t
            while (t1):
                print(t1.data, end=" ")
                t1 = t1.right
            print()
            t=t.down
        print()



if __name__=='__main__':
    
    #matrix is n*n size
    n = 3
    
    arr=[[1,2,3],[4,5,6],[7,8,9]]
    
    '''
    arr = [[0 for i in range(n)] for j in range(n)]
    input_list = [1,2,3,4,5,6,7,8,9]
    k=0
    for i in range(n):
        for j in range(n):
            arr[i][j] = input_list[k]
            k=k+1
    '''

    llist = LinkedList()
    llist.head = construct_2D_matrix(arr, n)
    llist.display()