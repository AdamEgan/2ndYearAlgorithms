#Adam Egan 115359356
from time import sleep
from AdaptibleQueue import *
""" Sample solutions to Lab 05.

    Implements the graph as a map of (vertex,edge-map) pairs.
    (same representation as for Lab 04)
"""

#needed for searching using a stack

#from stack import Stack

import copy

class Vertex:
    """ A Vertex in a graph. """
    
    def __init__(self, element):
        """ Create a vertex, with data element. """
        self._element = element

    def __str__(self):
        """ Return a string representation of the vertex. """
        return str(self._element)

    def __lt__(self, v):
        return self._element < v.element()

    def element(self):
        """ Return the data for the vertex. """
        return self._element
    def __repr__(self):
        return self.__str__()
    
class Edge:
    """ An edge in a graph.

        Implemented with an order, so can be used for directed or undirected
        graphs. Methods are provided for both. It is the job of the Graph class
        to handle them as directed or undirected.
    """
    
    def __init__(self, v, w, element):
        """ Create an edge between vertice v and w, with label element.

            element can be an arbitrarily complex structure.
        """
        self._vertices = (v,w)
        self._element = element
        

    def __str__(self):
        """ Return a string representation of this edge. """
        return ('( Start ' + str(self._vertices[0]) + '-- End '
                   + str(self._vertices[1]) + ' : '
                   + str(self._element) + ')')
    

    def vertices(self):
        """ Return an ordered pair of the vertices of this edge. """
        return self._vertices

    def start(self):
        """ Return the first vertex in the ordered pair. """
        return self._vertices[0]

    def end(self):
        """ Return the second vertex in the ordered. pair. """
        return self._vertices[1]
    

    def opposite(self, v):
        """ Return the opposite vertex to v in this edge. """
        if self._vertices[0] == v:
            return self._vertices[1]
        elif self._vertices[1] == v:
            return self._vertices[0]
        else:
            return None

    def element(self):
        """ Return the data element for this edge. """
        return self._element
    def __repr__(self):
        return self.__str__()

class Graph:
    """ Represent a simple graph.

        This version maintains only undirected graphs, and assumes no
        self loops.
    """

    #Implement as a Python dictionary
    #  - the keys are the vertices
    #  - the values are the edges for the corresponding vertex
    #    Each edge set is also maintained as a dictionary,
    #    with opposite vertex as the key and the edge object as the value
    
    def __init__(self):
        """ Create an initial empty graph. """
        self._structure = dict()

    def __str__(self):
        """ Return a string representation of the graph. """
        hstr = ('|V| = ' + str(self.num_vertices())
                + '; |E| = ' + str(self.num_edges()))
        vstr = '\nVertices: '
        for v in self._structure:
            vstr += str(v) + '-'
        edges = self.edges()
        estr = '\nEdges: '
        for e in edges:
            estr += str(e) + ' '
        return hstr + vstr + estr

    #--------------------------------------------------#
    #ADT methods to query the graph

    

    def in_degree(self,x):
        deg=0
        edges=self.get_edges(x)
        for edge in edges:
            if edge.end()==x:
                   deg+=1
        return deg
    def out_degree(self,x):
        deg=0
        edges=self.get_edges(x)
        for edge in eges:
               if edge.start()==x:
                    deg+=1
        return deg
    def get_in_edges(self,x):
        edgelist = []
        edges=self.get_edges(x)
        for edge in edges:
            if edge.end()==x:
                edgelist+=[edge]
        return edgelist

    def get_out_edges(self,x):
        edgelist = []
        edges=self.get_edges(x)
        for edge in edges:
            if edge.start()==x:
                edgelist+=[edge]
        return edgelist

                
    def num_vertices(self):
        """ Return the number of vertices in the graph. """
        return len(self._structure)

    def num_edges(self):
        """ Return the number of edges in the graph. """
        num = 0
        for v in self._structure:
            num += len(self._structure[v])    #the dict of edges for v
        return num //2     #divide by 2, since each edege appears in the
                           #vertex list for both of its vertices

    def vertices(self):
        """ Return a list of all vertices in the graph. """
        return [key for key in self._structure]

    def get_vertex_by_label(self, element):
        """ get the first vertex that matches element. """
        for v in self._structure:
            if v.element() == element:
                return v
        return None

    def edges(self):
        """ Return a list of all edges in the graph. """
        edgelist = []
        for v in self._structure:
            for w in self._structure[v]:
                #to avoid duplicates, only return if v is the first vertex
                if self._structure[v][w].start() == v:
                    edgelist.append(self._structure[v][w])
        return edgelist

    def get_edges(self, v):
        """ Return a list of all edges incident on v. """
        if v in self._structure:
            edgelist = []
            for w in self._structure[v]:
                edgelist.append(self._structure[v][w])
            return edgelist
        return None

        

    def get_edge(self, v, w):
        """ Return the edge between v and w, or None. """
        if (self._structure != None
                         and v in self._structure
                         and w in self._structure[v]):
            return self._structure[v][w]
        return None

    def degree(self, v):
        """ Return the degree of vertex v. """
        return len(self._structure[v])

    #--------------------------------------------------#
    #ADT methods to modify the graph
    
    def add_vertex(self, element):
        """ Add a new vertex with data element.

            If there is already a vertex with the same data element,
            this will create another vertex instance.
        """
        v = Vertex(element)
        self._structure[v] = dict()
        return v

    def add_vertex_if_new(self, element):
        """ Add and return a vertex with element, if not already in graph.

            Checks for equality between the elements. If there is special
            meaning to parts of the element (e.g. element is a tuple, with an
            'id' in cell 0), then this method may create multiple vertices with
            the same 'id' if any other parts of element are different.

            To ensure vertices are unique for individual parts of element,
            separate methods need to be written.
        """
        for v in self._structure:
            if v.element() == element:
                #print('Already there')
                return v
        return self.add_vertex(element)

    def add_edge(self, v, w, element):
        """ Add and return an edge between two vertices v and w, with  element.

            If either v or w are not vertices in the graph, does not add, and
            returns None.
            
            If an edge already exists between v and w, this will
            replace the previous edge.
        """
        if not v in self._structure or not w in self._structure:
            return None
        e = Edge(v, w, element)
        self._structure[v][w] = e
        self._structure[w][v] = e
        return e
    def cost(self,x,y):
        print(x)
        print(y)
        if x==None or y==None:
            #print("THIS IS THE COST",self._structure[x][y].element())
            print("Cost x:",x)
            print("cost y:",y)
            return 1
        else:
            print("hi")
            return self._structure[x][y].element()
    def add_edge_pairs(self, elist):
        """ add all vertex pairs in elist as edges with empty elements. """
        for (v,w) in elist:
            self.add_edge(v,w,None)

    #--------------------------------------------------#
    #Additional methods to explore the graph
        
    def highestdegreevertex(self):
        """ Return the vertex with highest degree. """
        hd = -1
        hdv = None
        for v in self._structure:
            if self.degree(v) > hd:
                hd = self.degree(v)
                hdv = v
        return hdv            

    #--------------------------------------------------#
    #New methods for Lab 05
    
    def dfs_stack(self, v):
        """ Return a DFS tree from v, using a stack. """
        marked = {v:None}
        stack = Stack()
        stack.push(v)
        while stack.length() > 0:
            vertex = stack.pop()
            for e in self.get_edges(vertex):
                w = e.opposite(vertex)
                if w not in marked:
                    marked[w] = e
                    stack.push(w)
        return marked
        
    def depthfirstsearch(self, v):
        """ Return a DFS tree from v. """
        marked = {v:None}
        self._depthfirstsearch(v, marked)
        return marked

    def _depthfirstsearch(self, v, marked):
        """ Do a DFS from v, storing nodes in marked. """
        for e in self.get_edges(v):
            w = e.opposite(v)
            if w not in marked:
                marked[w] = e
                self._depthfirstsearch(w, marked)
                
    def breadthfirstsearch(self, v):
        """ Return a BFS tree from v. """
        marked = {v:None}
        level = [v]
        while len(level) > 0:
            nextlevel = []
            for w in level:
                for e in self.get_edges(w):
                    x = e.opposite(w)
                    if x not in marked:
                        marked[x] = e
                        nextlevel.append(x)
            level = nextlevel
        return marked

    def BFS_length(self, v):
        """ Return a BFS tree from v, with path lengths. """
        marked = {v:(None,0)}
        level = [v]
        levelint = 1
        while len(level) > 0:
            nextlevel = []
            for w in level:
                for e in self.get_edges(w):
                    x = e.opposite(w)
                    if x not in marked:
                        marked[x] = (w, levelint)
                        nextlevel.append(x)
            level = nextlevel
            levelint += 1
        return marked
    
    def breadthfirstsearchtree(self, v):
        """ Return a down-directed BFS tree from v. """
        marked = {v:[]}
        level = [v]
        while len(level) > 0:
            nextlevel = []
            for w in level:
                for e in self.get_edges(w):
                    x = e.opposite(w)
                    if x not in marked:
                        marked[x] = []
                        marked[w].append(x)
                        nextlevel.append(x)
            level = nextlevel
        return marked

    def transitiveclosure(self):
        """ Return the transitive closure using version of FloydWarshall. """
        gstar = copy.deepcopy(self)
        vs = gstar.vertices()
        n = len(vs)
        for k in range(n):
            for i in range(n):
                if i != k and gstar.get_edge(vs[i], vs[k]) is not None:
                    for j in range(n):
                        if (i != j and k != j
                                     and gstar.get_edge(vs[k],vs[j]) is not None):
                            if gstar.get_edge(vs[i],vs[j]) == None:
                                gstar.add_edge(vs[i],vs[j],1)
        return gstar
    def topological_sort(self):
        #assumed to be operating on a DAG
        inedgecount = {} #map of (vertex:in_degree) pairs
        tsort = [] #list of vertices in sort order
        available = [] #vertices with no active in-edges
        for v in self._structure:
            v_incount = self.in_degree(v)
            inedgecount[v] = v_incount
            if v_incount == 0:
                available.append(v)
        while len(available) > 0:
            w = available.pop()
            tsort.append(w)
            for e in self.get_edges(w):
                u = e.opposite(w)
                inedgecount[u] -= 1
                if inedgecount[u] == 0:
                    available.append(u)
        return tsort
    def Istopological_sort(self):
        #assumed to be operating on a DAG
        inedgecount = {} #map of (vertex:in_degree) pairs
        tsort = [] #list of vertices in sort order
        available = [] #vertices with no active in-edges
        for v in self._structure:
            v_incount = self.in_degree(v)
            inedgecount[v] = v_incount
            if v_incount == 0:
                available.append(v)
        while len(available) > 0:
            w = available.pop()
            tsort.append(w)
            for e in self.get_edges(w):
                u = e.opposite(w)
                inedgecount[u] -= 1
                if inedgecount[u] == 0:
                    available.append(u)
        if len(tsort)>0:
            return True
        else:
            return False

    #Dijkstra algorithm          
    def dijkstra(self,s):
        open_=PriorityQueue()
        locs={}
        closed={}
        preds={}
        preds[s]=None   
        elt=open_.add(0,s)  
        locs[s]=elt
        cost=0
        while open_.length()>0:
            v=open_.remove_min()
            locs.pop(v.getValueE())
            print(preds)
            vprev=preds.pop(v.getValueE())
            closed[v.getValueE()]=(cost,vprev)
            edges=self.get_edges(v.getValueE())
            for edge in edges:
                w=edge.opposite(v.getValueE())
                if w not in closed:
                    cost=v.getKey()+edge.element()  
                    if w  not in locs:
                        preds[w]=v
                        elt2=open_.add(cost,w)
                        locs[w]=elt2
                    elif cost<locs[w].getKey():
                        preds[w]=v.getValueE()
                        open_.update_key(locs[w],cost)
        return closed























        
    
    #End of class definition

#---------------------------------------------------------------------------#
#Test methods

def graphreader(filename):
    """ Read and return the route map in filename. """
    graph = Graph()
    file = open(filename, 'r')
    entry = file.readline() #either 'Node' or 'Edge'
    num = 0
    while entry == 'Node\n':
        num += 1
        nodeid = file.readline().split()[1]
        vertex = graph.add_vertex(nodeid)
        entry = file.readline() #either 'Node' or 'Edge'
    print('Read', num, 'vertices and added into the graph')
    num = 0
    while entry == 'Edge\n':
        num += 1
        source = file.readline().split()[1]
        sv = graph.get_vertex_by_label(source)
        target = file.readline().split()[1]
        tv = graph.get_vertex_by_label(target)
        length = float(file.readline().split()[1])
        edge = graph.add_edge(sv, tv, length)
        file.readline() #read the one-way data
        entry = file.readline() #either 'Node' or 'Edge'
    print('Read', num, 'edges and added into the graph')
    print(graph)
    return graph


def main():
    graph=graphreader("simplegraph2.txt")
    v=graph.get_vertex_by_label("14")
    print(graph.dijkstra(v))
    
if __name__=='__main__':
    main()
    
    
