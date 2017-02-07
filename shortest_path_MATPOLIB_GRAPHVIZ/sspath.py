
import sys
import graphviz as gv
import functools
import networkx as nx
import matplotlib.pyplot as plt
graph = functools.partial(gv.Graph, format='svg')
digraph = functools.partial(gv.Digraph, format='svg')
f=open("cities.txt","r")
print f.readlines()

graph={'Kent':{'Washington':113, 'Oxford':2368},
                    'Washington':{'Dublin':419,'Oxford':891,'Bryan':1416},
                    'Oxford':{'Bryan':142, 'Dublin':120},
                    'Bryan':{'Kent':27,'Dublin':1144},
                    'Dublin':{'Kent':793} }


def dijkstra(graph,src,dest,visited=[],distances={},predecessors={}):
    # a few sanity checks
			    if src not in graph:
			        raise TypeError('the root of the shortest path tree cannot be found in the graph')
			    if dest not in graph:
			        raise TypeError('the target of the shortest path cannot be found in the graph')    
			    # ending condition
			    if src == dest:
			        # We build the shortest path and display it
			        path=[]
			        pred=dest
			        while pred != None:
			            path.append(pred)
			            pred=predecessors.get(pred,None)
			        print('shortest path: '+str(path)+" cost="+str(distances[dest])) 
			    else :     
			        # if it is the initial  run, initializes the cost
			        if not visited: 
			            distances[src]=0
			        # visit the neighbors
			        for neighbor in graph[src] :
			            if neighbor not in visited:
			                new_distance = distances[src] + graph[src][neighbor]
			                if new_distance < distances.get(neighbor,float('inf')):
			                    distances[neighbor] = new_distance
			                    predecessors[neighbor] = src
			        # mark as visited
			        visited.append(src)
			        # now that all neighbors have been visited: recurse                         
			        # select the non visited node with lowest distance 'x'
			        # run Dijskstra with src='x'
			        unvisited={}
			        for k in graph:
			            if k not in visited:
			                unvisited[k] = distances.get(k,float('inf'))        
			        x=min(unvisited, key=unvisited.get)
			        dijkstra(graph,x,dest,visited,distances,predecessors)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()
    graph = graph={'Kent':{'Washington':113, 'Oxford':2368,'Bryan':27},
                    'Washington':{'Dublin':419,'Oxford':891,'Bryan':1416},
                    'Oxford':{'Bryan':142, 'Dublin':120},
                    'Bryan':{'Kent':27,'Dublin':1144,'Oxford':142},
                    'Dublin':{'Kent':793} 
                    }
    dijkstra(graph,'Kent','Oxford')
    nodes = ['A', 'B','C', 'D' ,'E']

edges = [
    ('A', 'B'),
    ('B', 'C'),
    ('C', 'D'),
    (('D', 'A'), {}),
]


def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            graph.node(n[0], **n[1])
        else:
            graph.node(n)
    return graph

def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1])
        else:
            graph.edge(*e)
    return graph




g6 = add_edges(
    add_nodes(digraph(), [
        ('A', {'label': 'KENT'}),
        ('B', {'label': 'WASHINGTON'}),
        ('C', {'label': 'DUBLIN'}),
        ('D', {'label': 'BRYAN'}),
        ('E',{'label': 'OXFORD'})
    ]),
    [
        (('A', 'B'), {'label': '113'}),
        (('A', 'C'), {'label': '793'}),
        (('A', 'D'), {'label': '27'}),
        (('B', 'C'), {'label': '419'}),
        (('B', 'D'), {'label': '1416'}),
        (('B', 'E'), {'label': '891'}),
        (('C', 'D'), {'label': '1144'}),
        (('C', 'E'), {'label': '120'}),
        (('D', 'E'), {'label': '142'}),
        (('E', 'A'), {'label': '2368'}),


    ]
)


styles = {
    'graph': {
        'label': '',
        'fontsize': '16',
        'fontcolor': 'white',
        'bgcolor': '#000000',
        'rankdir': 'BT',
    },
    'nodes': {
        'fontname': 'Helvetica',
        'shape': 'hexagon',
        'fontcolor': 'white',
        'color': 'white',
        'style': 'filled',
        'fillcolor': '#00FF00',
    },
    'edges': {
        'style': 'dashed',
        'color': 'white',
        'arrowhead': 'open',
        'fontname': 'Courier',
        'fontsize': '12',
        'fontcolor': 'white',
    }
}


def apply_styles(graph, styles):
    graph.graph_attr.update(
        ('graph' in styles and styles['graph']) or {}
    )
    graph.node_attr.update(
        ('nodes' in styles and styles['nodes']) or {}
    )
    graph.edge_attr.update(
        ('edges' in styles and styles['edges']) or {}
    )
    return graph 

g6 = apply_styles(g6, styles)
g6.render('img/g6')