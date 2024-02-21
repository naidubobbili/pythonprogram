#BinaryTree
class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def print_tree(self, level=0):
        print("   " * level + self.data)
        if self.left:
            self.left.print_tree(level + 1)
        if self.right:
            self.right.print_tree(level + 1)

def insert(self,new):
    """Inserting"""
    if not self:
        self=new
        return
    traversed=[]
    traversed.append(self)
    while traversed!=[]:
        k=traversed.pop(0)
        if k.left:
            traversed.append(k.left)
        else:
            k.left=new
            return
        if k.right:
            traversed.append(k.right)
        else:
            k.right=new
            return
        
def preorder(self):
    """Root Left Right"""
    if not self:
        return
    x.append(self.data)
    preorder(self.left)
    preorder(self.right)
        
def inorder(self):
    """Left Root Right"""
    if not self:
        return
    inorder(self.left)
    x.append(self.data)
    inorder(self.right)
        
def postorder(self):
    """Left Right Root"""
    if not self:
        return
    postorder(self.left)
    postorder(self.right)
    x.append(self.data)
    
def levelorder(self):
    """Top to Bottom"""
    if not self:
        return
    traversed=[]
    traversed.append(self)
    while traversed!=[]:
        x.append(traversed[0].data)
        k=traversed.pop(0)
        if k.left:
            traversed.append(k.left)
        if k.right:
            traversed.append(k.right)

def search(val,self):
    """Searching"""
    preorder(self)
    if val in x:
        print("Found")
    else:
        print("Not Found")
        

t=Tree("Drinks")
h=Tree("Hot")
c=Tree("Cold")
h1=Tree("Tea")
h2=Tree("Coffee")
c1=Tree("Coke")
c2=Tree("Sprite")
t.left=h
t.right=c
h.left=h1
h.right=h2
c.left=c1
c.right=c2

x=[]
preorder(t)
print(x)

x=[]
inorder(t)
print(x)

x=[]
postorder(t)
print(x)

search("Cold",t)

t.print_tree()

w=Tree("Water")
insert(t,w)

x=[]
levelorder(t)
print(x)

#help(Tree)
#help(levelorder)
