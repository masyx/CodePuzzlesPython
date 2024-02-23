import sys
sys.path.append('DataStructuresCourse_Educative\MyCustomDataStructures')
from graph import Graph

def detect_cycle(graph: Graph) -> bool:
    """Detect if there's a cycle in the graph."""
    visited = [False] * graph.vertices
    rec_stack = [False] * graph.vertices

    def is_cyclic_util(vertex: int) -> bool:
        """Utility function to detect cycle using DFS."""
        visited[vertex] = True
        rec_stack[vertex] = True

        current_node = graph.adj_list[vertex].get_head()
        while current_node:
            adjacent_vertex = current_node.data
            if not visited[adjacent_vertex]:
                if is_cyclic_util(adjacent_vertex):
                    return True
            elif rec_stack[adjacent_vertex]:
                return True
            current_node = current_node.next

        rec_stack[vertex] = False
        return False

    for vertex in range(graph.vertices):
        if not visited[vertex]:
            if is_cyclic_util(vertex):
                return True
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