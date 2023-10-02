# a node is just a 2d space 

# the head node is the entire plane

# a leaf is a dead space (no longer being partitioned)

# a node is a living space (still being actively partitioned)

# we need a data structure for nodes/leaves that can represent any 2d space 

# our data structure is a list of spaces 

class Node:
    def __init__(self, left = None,right = None, points = None, name=None):
        #left and right can be either nodes or leafs
        self.left = left
        self.right = right
        #area describes the space indicated by a leaf
        self.area = []
        self.name = name


def makeTree(n):
    if ( n > 7 or n < 1) :
        print("please select one of 7 lines by user the function with an integer argument between 1-7")
        return
    HN = Node(None, None, [],"Head Node")
    N1 = Node(None, None, [],"Node 1")
    N2 = Node(None, None, [],"Node 2")
    N3 = Node(None, None, [],"Node 3")
    N4 = Node(None, None, [],"Node 4")
    N5 = Node(None, None, [],"Node 5")
    N6 = Node(None, None, [],"Node 6")
    L1 = Node(None, None, [],"Leaf 1")
    L2 = Node(None, None, [],"Leaf 2")
    L3 = Node(None, None, [],"Leaf 3")
    L4 = Node(None, None, [],"Leaf 4")
    L5 = Node(None, None, [],"Leaf 5")
    L6 = Node(None, None, [],"Leaf 6")
    L7 = Node(None, None, [],"Leaf 7")
    L8 = Node(None, None, [],"Leaf 8")
    #user inputs which one should go first
    leafs = [L1,L2,L3,L4,L5,L6,L7,L8]
    nodes = [N1,N2,N3,N4,N5,N6]
    list = [["y",1,'l'],   ["x",-1.5,'l'] ,   ["x", 1.3, 'r'],   ["y", -1, 'r'],  ["x",-.4,'l'],  ["y",0,'r'] ,  ["-1.25", .3, 'l']]
    current = HN
    #we have to first make the head node with either the left or right child being the leaf selected by the user
    L1.area = list[n-1]
    if (L1.area[2] == 'l') :
        HN.left = L1
        HN.right = N1
        print(current.name)
        print(str(current.left.area) + "//     \\\\" + current.right.name)
        current = HN.right 
    else :
        HN.right = L1
        HN.left = N1
        print(current.name)
        print(current.left.name + "//     \\\\" + str(current.right.area))
        current = HN.left
    #Then we remove that item from list and iterate over list
    del list[n-1]
    #for each item in the list we have to update the current node by setting one child as the current item and the other child as the next node
    count = 0
    for leaf in list:
        #if we are at the last element
        if (leaf == list[-1]):
            #check if the last element is going right or left
            if (leaf[2] == 'l'):
                #if the last element is going left we must make the last right child a copy with the opposite direction
                current.left = leafs[count]
                current.left.area = leaf
                current.right = leafs[count+1]
                current.right.area = [leaf[0],leaf[1],'r']
            else:
                #if the last element is going right we must make the last left child a copy with the opposite direction
                current.right = leafs[count]
                current.right.area = leaf
                current.left = leafs[count+1]
                current.left.area = [leaf[0],leaf[1],'l']
            #print(str(current.left.area) + "//     \\\\" + str(current.right.area))
        elif (leaf[2] == 'l') :
            #if the next leaf is a left child we have to make it current's left child and update the area
            current.left = leafs[count]
            current.left.area = leaf
            #then we have to update the right child and make it the current node
            current.right = nodes[count]
            #print(str(current.left.area) + "//     \\\\" + current.right.name)
            current = current.right
        else :
            #if the next leaf is a right child we have to make it current's right child and update the area
            current.right = leafs[count]
            current.right.area = leaf
            #then we have to update the left child and make it the current node
            current.left = nodes[count]
            #print(current.left.name + "//     \\\\" + str(current.right.area))
            current = current.left
        count+=1
        #then we move on to the next item in the list and iterate the counter
    return HN




def traverse(node):
    #verify the argument provided is not None
    if node is not None:
        #recursively traverse the left child
        traverse(node.left)

        #traverse the current node
        if node.area != []:
            print(node.name + " : " + str(node.area)) 
        else:
            print("This is " + node.name)

        #recursively traverse the right child
        traverse(node.right)

test = makeTree(1)

traverse(test)




"""
This is the old version of makeTree from when I completely misunderstood the problem. I thought that the tree always started 
with the same horizontal line and we were just letting the user decide the y value of this line. 

def makeTree(y):
    third = 4/3
    L1 = Node(None, None, [((-2*y),(y)),   ((-2*y),(third * y)),   ((2*y),(y)),    ((2*y),(third * y))],"Leaf 1")
    L2 = Node(None, None, [((-2*y),(y)),   ((-1.5*y),(y)),((-2*y),   (-third * y)),((-1.5*y),   (-third * y))],"Leaf 2")
    L3 = Node(None, None, [((-2*y),(y)),   ((1.3*y),(y)),    ((-2*y),(-third * y)),    ((1.3*y),(-third * y))],"Leaf 3")
    L4 = Node(None, None, [((-1.5*y),(-y)),   ((-1.5*y),(-third * y)),    ((1.3*y),(-y)),    ((1.5*y),(-third * y))],"Leaf 4")
    L5 = Node(None, None, [((-1.5*y),y),    ((-.4*y),y),     ((-1.5*y),-y),    ((-.4*y),-y)],"Leaf 5")
    L6 = Node(None, None, [((-.4*y),0),   ((1.3*y),0),    ((-.4*y),-y),     ((1.3*y),-y)],"Leaf 6")
    L7 = Node(None, None, [((-.4 * y),(.9 * y)),    ((0.32 * y), 0),    ((-.4 * y),y)   ,((1.3*y),y),   ((1.3*y),0) ],"Leaf 7")
    L8 = Node(None, None, [((-.4 * y),(.9 * y)),    ((0.32 * y), 0),    ((-.4 * y), 0)],"Leaf 8")

    N6 = Node(L7,L8,[],"Node 6")
    N5 = Node(N6,L6,[],"Node 5")
    N4 = Node(L5,N5,[],"Node 4")
    N3 = Node(N4,L4,[],"Node 3")
    N2 = Node(N3,L3,[],"Node 2")
    N1 = Node(L2,N2,[],"Node 1")
    HN = Node(L1, N1, [],"Head Node")
    return HN

"""