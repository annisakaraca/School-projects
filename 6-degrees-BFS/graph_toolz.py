import os
from collections import deque

class Graph(object):
    # Initializing empty graph
    def __init__(self):
        self.adj_list = dict()    # Initial adjacency list is empty dictionary
        self.vertices = set()    # Vertices are stored in a set
        self.degrees = dict()    # Degrees stored as dictionary
        self.color = dict()     # color of vertex stored as dictionary
        self.pred = dict()       # predecessor of vertex stored as dictionary
        self.distance = dict()   # distance of vertex from source stored as a dictionary

    # Checks if (node1, node2) is edge of graph. Output is 1 (yes) or 0 (no).
    def isEdge(self,node1,node2):
        if node1 in self.vertices:        # Check if node1 is vertex
            if node2 in self.adj_list[node1]:    # Then check if node2 is neighbor of node1
                return 1            # Edge is present!

        if node2 in self.vertices:        # Check if node2 is vertex
            if node1 in self.adj_list[node2]:    # Then check if node1 is neighbor of node2
                return 1            # Edge is present!

        return 0                # Edge not present!

    # Add undirected, simple edge (node1, node2)
    def addEdge(self,node1,node2):

        # print('Called')
        if node1 == node2:            # Self loop, so do nothing
            # print('self loop')
            return
        if node1 in self.vertices:        # Check if node1 is vertex
            nbrs = self.adj_list[node1]        # nbrs is neighbor list of node1
            if node2 not in nbrs:         # Check if node2 already neighbor of node1
                nbrs.add(node2)            # Add node2 to this list
                self.degrees[node1] = self.degrees[node1]+1    # Increment degree of node1

        else:                    # So node1 is not vertex
            self.vertices.add(node1)        # Add node1 to vertices
            self.adj_list[node1] = {node2}    # Initialize node1's list to have node2
            self.degrees[node1] = 1         # Set degree of node1 to be 1

        if node2 in self.vertices:        # Check if node2 is vertex
            nbrs = self.adj_list[node2]        # nbrs is neighbor list of node2
            if node1 not in nbrs:         # Check if node1 already neighbor of node2
                nbrs.add(node1)            # Add node1 to this list
                self.degrees[node2] = self.degrees[node2]+1    # Increment degree of node2

        else:                    # So node2 is not vertex
            self.vertices.add(node2)        # Add node2 to vertices
            self.adj_list[node2] = {node1}    # Initialize node2's list to have node1
            self.degrees[node2] = 1         # Set degree of node2 to be 1

    # Give the size of the graph. Outputs [vertices edges wedges]
    #
    def size(self):
        n = len(self.vertices)            # Number of vertices

        m = 0                    # Initialize edges/wedges = 0
        wedge = 0
        for node in self.vertices:        # Loop over nodes
            deg = self.degrees[node]      # Get degree of node
            m = m + deg             # Add degree to current edge count
            wedge = wedge+deg*(deg-1)/2        # Add wedges centered at node to wedge count
        return [n, m, wedge]            # Return size info

    # Print the graph
    def output(self,fname,dirname):
        os.chdir(dirname)
        f_output = open(fname,'w')

        for node1 in list(self.adj_list.keys()):
            f_output.write(str(node1)+': ')
            for node2 in (self.adj_list)[node1]:
                f_output.write(str(node2)+' ')
            f_output.write('\n')
        f_output.write('------------------\n')
        f_output.close()

    def path(self, src, dest):
        #""" implement your shortest path function here """
        shortest_path = []
        if (src == dest):
            shortest_path = [src]
            print (shortest_path)
            return shortest_path            
        for node in self.vertices:            # for each node in graph
            if (node != src):                 # and if the node is not the source node
                self.color[node] = "white"    # set node color to white
                self.distance[node] = 0       # set distance from node to src to 0
                self.pred[node] = None        # empty predecessor for node
        self.color[src] = "gray"              # src node is set to gray
        self.distance[src] = 0                # distance from src node to src node is 0
        self.pred[src] = None                 # src node has no predecessor
        Q = deque()                           # create empty deque Q
        Q.append(src)                         # add src to Q
        vertexpath = list()
        while (len(Q) != 0):                  # while the Q isn't empty
            u = Q.popleft()                   # remove the first item from Q, set to u
            nbrs = self.adj_list[u]           # nbrs is neighbors of u
            for node in nbrs:                 # iterate through every node that is a neighbor of u
                if (self.color[node] == "white"):                   # if the node has not yet been visited
                    self.color[node] = "gray"                       # change color of the node to gray
                    self.distance[node] = self.distance[u] + 1      # distance of discovered node is one more than distance of u
                    self.pred[node] = [u]                           # predecessor of discovered node is u and the predecessors of u
                    if (self.pred[u] != None):                        # if u has a predecessor
                        self.pred[node] = [u] + self.pred[u]          # append u's predecessor to the predecessor path of node
                    Q.append(node)                                    # add discovered node to Q
                    if (node == dest):                                # if discovered node is dest
                        shortest_path = [node] + self.pred[node]      # shortest path is list of predecessors
                        vertexpath.append([dest])                     # add destination to the end of the vertex path
                        print (shortest_path)                         # print shortest_path
                        return shortest_path                          # send shortest_path to path.txt


#        return shortest_path

    def levels(self, src):
        """ implement your level set code here """
        level_sizes = []
        level = []
        for node in self.vertices:         # for each node in graph
            if (node != src):              # and if the node is not the source node
                self.color[node] = "white"   # set node color to white
                self.distance[node] = 0    # set distance from node to src to 0
                self.pred[node] = None     # empty predecessor for node
        self.color[src] = "gray"             # src node is set to gray
        self.distance[src] = 0             # distance from src node to src node is 0
        self.pred[src] = None              # src node has no predecessor
        Q = deque()                        # create empty deque Q
        Q.append(src)                      # add src to Q
        level.append(0)
        i = 0
        while (len(Q) != 0):               # while the Q isn't empty
            u = Q.popleft()                # remove the first item from Q, set to u
            nbrs = self.adj_list[u]        # nbrs is neighbors of u
            for node in nbrs:              # iterate through every node that is a neighbor of u
                if (self.color[node] == "white"):                   # if the node has not yet been visited
                    self.color[node] = "gray"                       # change color of the node to gray
                    self.distance[node] = self.distance[u] + 1      # distance of discovered node is one more than distance of u
                    self.pred[node] = [u]                           # predecessor of discovered node is u and the predecessors of u
                    if (self.pred[u] != None):                      # if u has a predecessor
                        self.pred[node] = [u] + self.pred[u]        # append u's predecessor to the predeccessor path of node
                    Q.append(node)                                  # add discovered node to Q
                    if (self.distance[node] < 7):                   # if there are 6  degrees or less of separation between src and node
                        level.append(self.distance[node])           # append the degree of separation to level list
                    else:                                           # if there are greater than 7 degrees of separation between src and node
                        level.append(7)                             # append 7 to the level list
        while i < 7:                                                # for i from 0 to 7
            level_sizes.append(level.count(i))                      # the ith value of level_sizes is the number of i's present in level
            i += 1                                                  # increment i
        return level_sizes                                          # output the sizes of all levels
        
