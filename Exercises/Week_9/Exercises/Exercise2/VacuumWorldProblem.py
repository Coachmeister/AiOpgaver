class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent=None, depth=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth

    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)  # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH)


'''
Search the tree for the goal state and return path from initial state to goal state
'''


def TREE_SEARCH():
    fringe = []
    initial_node = Node(INITIAL_STATE)
    fringe = INSERT(initial_node, fringe)
    while fringe is not None:
        node = REMOVE_FIRST(fringe)
        if GOAL_STATE.__contains__(node.STATE):
            return node.path()
        children = EXPAND(node)
        fringe = INSERT_ALL(children, fringe)
        print("fringe: {}".format(fringe))


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''


def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(node)  # create node for each in state list
        s.STATE = child  # e.g. result = 'F' then 'G' from list ['F', 'G']
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        successors = INSERT(s, successors)
    return successors


'''
Insert node in to the queue (fringe).
'''


def INSERT(node, queue):
    queue.append(node)
    return queue


'''
Insert list of nodes into the fringe
'''


def INSERT_ALL(list, queue):
    queue.extend(list)
    return queue


'''
Removes and returns the first element from fringe
'''


def REMOVE_FIRST(queue):
    return queue.pop(0)


'''
Successor function, mapping the nodes to its successors
'''


def successor_fn(state):  # Lookup list of successor states
    return STATE_SPACE[state]  # successor_fn( 'C' ) returns ['F', 'G']


DIRTY = 'DIRTY'
CLEAN = 'CLEAN'

INITIAL_STATE = ('A', DIRTY, DIRTY)
GOAL_STATE = ('A', CLEAN, CLEAN), ('B', CLEAN, CLEAN)

STATE_SPACE = {('A', DIRTY, DIRTY): [('A', CLEAN, DIRTY), ('A', DIRTY, DIRTY), ('B', DIRTY, DIRTY)],
               ('A', CLEAN, DIRTY): [('B', CLEAN, DIRTY)],
               ('B', DIRTY, DIRTY): [('B', DIRTY, CLEAN), ('A', DIRTY, DIRTY)],
               ('B', CLEAN, DIRTY): [('B', CLEAN, DIRTY), ('B', CLEAN, CLEAN)],
               ('B', DIRTY, CLEAN): [('A', DIRTY, CLEAN)],
               ('A', DIRTY, CLEAN): [('A', CLEAN, CLEAN), ('B', DIRTY, CLEAN)],
               ('A', CLEAN, CLEAN): [('B', CLEAN, CLEAN)],
               ('B', CLEAN, CLEAN): [('A', CLEAN, CLEAN)]}

#STATE_SPACE = {'A': ['B', 'C'],
 #              'B': ['D', 'E'], 'C': ['F', 'G'],
  #             'D': [], 'E': [], 'F': [], 'G': ['H', 'I', 'J'],
   #            'H': [], 'I': [], 'J': [], }

'''
Run tree search and display the nodes in the path to goal node
'''


def run():
    path = TREE_SEARCH()
    print('Solution path:')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()
