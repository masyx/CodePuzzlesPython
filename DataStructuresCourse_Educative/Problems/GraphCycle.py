import sys
sys.path.append('DataStructuresCourse_Educative\MyCustomDataStructures')
from graph import Graph


def detect_cycle(graph):
    pass



if __name__ == "__main__" :
    g = Graph(7)
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        print("Graph is empty")
    elif num_of_vertices < 0:
        print("Graph cannot have negative vertices")
    else:
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(3, 0)
        g.add_edge(3, 1)
        g.add_edge(1, 4)
        g.add_edge(1, 5)
        g.add_edge(4, 5)
        g.add_edge(3, 6)
        
    print(f"Cycle detected in the given graph: {detect_cycle(g)}")