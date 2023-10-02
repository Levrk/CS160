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
        #list is the list of excluded leaves
        self.points = points
        self.name = name


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


def traverse(node):
    #verify the argument provided is not None
    if node is not None:
        #recursively traverse the left child
        traverse(node.left)

        #traverse the current node
        if node.points != []:
            print(node.name + " : " + str(node.points)) 
        else:
            print("This is " + node.name)

        #recursively traverse the right child
        traverse(node.right)

test = makeTree(1.2)

traverse(test)