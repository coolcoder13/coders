def treeSize(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return treeSize(node.left)+treeSize(node.right)+1


class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None


from collections import deque


def buildTree(s):
    
    #if height of tree is null
    if len(s)==0 or s[0]=='N':
        return None
    
    root=Node(int(s[0]))
    
    # using deque() as it provides inserting deleting elements from 0th or last index in O(1)
    q=deque()
    #size of double ended queue
    size=0
    q.append(root)
    size+=1
    
    #traverse list from index 1 to last
    i=1
    
    #with each while loop a level of tree is inserted into it
    while i<len(s) and size>0:
        
        # store and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size-=1
        
        
        # If the left child is not null
        if s[i]!='N':
            currNode.left=Node(int(s[i]))
            q.append(currNode.left)
            size+=1
    
            
        # For the right child
        i+=1
        if i>=len(s):
            break
        
        # If the right child is not null
        if s[i]!='N':
            currNode.right=Node(int(s[i]))
            q.append(currNode.right)
            size+=1
        i+=1
        
    return root



#                10
#              /    \
#             20    30
#           /   \
#         40    60



if __name__=="__main__":
    s=['10', '20', '30', '40', '60', 'N', 'N']
    root=buildTree(s)
    print(treeSize(root))