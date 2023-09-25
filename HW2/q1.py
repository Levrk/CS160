# a node is just a 2d space 

# the head node is the entire plane

# a leaf is a dead space (no longer being partitioned)

# a node is a living space (still being actively partitioned)

# we need a data structure for nodes/leaves that can represent any 2d space 

# our data structure is a list of spaces 

class Node:
    def __init__(self, left = None,right = None, list = None):
        #left and right can be either nodes or leafs
        self.left = None
        self.right = None
        #list is the list of excluded leaves
        self.list = []

class Leaf:
    def __init__(self, points = None):
        #list of tuples representing the points on the edge of the 2d space
        self.points = []
        


L1 = Leaf([(1,-1),(1,1),(1,0.8),((-1,0.8))])

N1 = Node(None,None,[L1.points])

HN = Node(L1, N1, [])


def makeTree(y):
    L1 = Leaf([(1,-1),(1,1),(1,y),((-1,y))])
    L2 = Leaf()
    L3 = Leaf()
    L4 = Leaf()
    L5 = Leaf()
    L6 = Leaf()
    L7 = Leaf()
    L8 = Leaf()

    N6 = Node(None,None,[L1.points,L2.points,L3.points,L4.points, L5.points,L6.points])
    N5 = Node(None,None,[L1.points,L2.points,L3.points,L4.points, L5.points])
    N4 = Node(None,None,[L1.points,L2.points,L3.points,L4.points])
    N3 = Node(None,None,[L1.points,L2.points,L3.points])
    N2 = Node(None,None,[L1.points,L2.points])
    N1 = Node(None,None,[L1.points])
    HN = Node(L1, N1, [])