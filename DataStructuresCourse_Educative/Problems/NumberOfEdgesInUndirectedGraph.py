from collections import deque
import sys
sys.path.append('DataStructuresCourse_Educative\MyCustomDataStructures')
from graph import Graph


def num_edges(g: Graph):
    count = 0
    for i in range(g.vertices):
        count += g.adj_list[i].length() 
    return count // 2



if __name__ == "__main__" :
    g = Graph(8)
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        print("Graph is empty")
    elif num_of_vertices < 0:
        print("Graph cannot have negative vertices")
    else:
        g.add_edge(0, 2)
        g.add_edge(0, 5)
        g.add_edge(2, 3)
        g.add_edge(2, 4)
        g.add_edge(5, 3)
        g.add_edge(5, 6)
        g.add_edge(3, 6)
        g.add_edge(6, 7)
        g.add_edge(6, 8)
        g.add_edge(6, 4)
        g.add_edge(7, 8)
        
    print(num_edges(g))