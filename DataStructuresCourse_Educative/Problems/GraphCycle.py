import sys
sys.path.append('DataStructuresCourse_Educative\MyCustomDataStructures')
from graph import Graph


def detect_cycle(graph: Graph):
    """
    Checks if the graph contains a cycle.
    
    Args:
        graph (Graph): The Graph instance to check for cycles
    
    Returns:
        bool: True if the graph has a cycle, False otherwise
    """
    visited = [False] * graph.vertices
    rec_stack = [False] * graph.vertices

    for vertex in range(graph.vertices):
        if not visited[vertex]:
            if is_cyclic_util(vertex, visited, rec_stack, graph):
                return True
    return False

def is_cyclic_util(vertex, visited, rec_stack, graph):
    """
    Utility function for detecting cycle in a graph using DFS.

    Args:
        vertex (int): Current vertex in DFS
        visited (list): List to keep track of visited vertices
        rec_stack (list): List to keep track of vertices in the current recursion stack
        graph (Graph): The Graph instance to check for cycles

    Returns:
        bool: True if a cycle is detected, False otherwise
    """
    visited[vertex] = True
    rec_stack[vertex] = True

    temp = graph.adj_list[vertex].get_head()
    while temp:
        i = temp.data
        if i < graph.vertices and not visited[i]:
            if is_cyclic_util(i, visited, rec_stack, graph):
                return True
        elif i < graph.vertices and rec_stack[i]:
            return True
        temp = temp.next

    rec_stack[vertex] = False
    return False


if __name__ == "__main__" :
    g = Graph(10)
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        print("Graph is empty")
    elif num_of_vertices < 0:
        print("Graph cannot have negative vertices")
    else:
        g.add_edge(2, 0)
        g.add_edge(2, 4)
        g.add_edge(4, 6)
        g.add_edge(6, 8)
        g.add_edge(8, 10)
        g.add_edge(8, 9)
        g.add_edge(8, 2)

    print(f"Cycle detected in the given graph: {detect_cycle(g)}")