#Adam Egan 115359356
from time import sleep
from AdaptibleQueue import *
from assignment2 import *
#needed for searching using a stack

#from stack import Stack
import copy
class roadMap(object):
    def __init__(self):
        """ Create an initial empty graph. """
        self._structure = dict()
        self._vertex=dict()       #id:vertex object
        self._coordinates=dict()  #vertex:(long,lat)

    def __str__(self):
        numE=self.num_edges()
        numV=self.num_vertices()
        """ Return a string representation of the graph. """
        hstr = ('|V| = ' + str(self.num_vertices())
                + '; |E| = ' + str(self.num_edges()))
        vstr = '\nVertices: '
        for v in self._structure:
            if numV<100:
                vstr += str(v) + '-'
        edges = self.edges()
        estr = '\nEdges: '
        for e in edges:
            if numE<100:
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
        if element in self._vertex:
            return self._vertex[element]
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
    
    def add_vertex(self, element,cors):
        """ Add a new vertex with data element.

            If there is already a vertex with the same data element,
            this will create another vertex instance.
        """
        v = Vertex(element)
        self._structure[v] = dict()
        self._coordinates[v]=cors
        self._vertex[element]=v
        return v
    def getCors(self,cors):
        if cors in self._coordinates:
            return self._coordinates[cors]

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
    def sp(self,v,w):
        verts=[]
        table=self.dijkstra(v)
        prev_cost=table[w][0]
        nextw=w
        while nextw!=v:
            data=table[nextw]
            cost=data[0]
            verts+=[(nextw,(prev_cost-cost))]
            prev_cost=cost
            nextw=data[1]
        return verts[::-1]
    def printvlist(self,lst):
        print("type\tlatitutde\tlongitude\telement\tcost")
        for pair in lst:
            cors=self.getCors(pair[0])
            print("W\t%s\t%s\t%s\t%s"%(str(cors[0]),str(cors[1]),str(pair[0]),str(pair[1])))
        
           
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
            vprev=preds.pop(v.getValueE())
            closed[v.getValueE()]=(cost,vprev)
            edges=self.get_edges(v.getValueE())
            for edge in edges:
                w=edge.opposite(v.getValueE())
                if w not in closed:
                    cost=v.getKey()+edge.element()  
                    if w  not in locs:
                        preds[w]=v.getValueE()
                        elt2=open_.add(cost,w)
                        locs[w]=elt2
                    elif cost<locs[w].getKey():
                        preds[w]=v.getValueE()
                        open_.update_key(locs[w],cost)
        return closed
    
def RouteMap(filename):
    """ Read and return the route map in filename. """
    graph = roadMap()
    file = open(filename, 'r')
    entry = file.readline() #either 'Node' or 'Edge'
    num = 0
    while entry == 'Node\n':
        num += 1
        nodeid = int(file.readline().split()[1])
        co = file.readline().split()
        coords = (co[1],co[2])
        vertex = graph.add_vertex(nodeid,coords)
        entry = file.readline() #either 'Node' or 'Edge'
    print('Read', num, 'vertices and added into the graph')
    num = 0
    while entry == 'Edge\n':
        num += 1
        source = int(file.readline().split()[1])
        sv = graph.get_vertex_by_label(source)
        target = int(file.readline().split()[1])
        tv = graph.get_vertex_by_label(target)
        file.readline()
        time = float(file.readline().split()[1])
        edge = graph.add_edge(sv, tv, time)
        file.readline() #read the one-way data
        entry = file.readline() #either 'Node' or 'Edge'
    print('Read', num, 'edges and added into the graph')
    return graph


def main():
    routemap = RouteMap('corkcitydata.txt')
    ids = {}
    ids['wgb'] = 1669466540
    ids['turnerscross'] = 348809726
    ids['neptune'] = 1147697924
    ids['cuh'] = 860206013
    ids['oldoak'] = 358357
    ids['gaol'] = 3777201945
    ids['mahonpoint'] = 330068634
    sourcestr = 'wgb'
    deststr='neptune'
    source = routemap.get_vertex_by_label(ids[sourcestr])    
    dest = routemap.get_vertex_by_label(ids[deststr])
    tree = routemap.sp(source,dest)
    routemap.printvlist(tree)
    
if __name__=='__main__':
    main()
    
    



     
















    
