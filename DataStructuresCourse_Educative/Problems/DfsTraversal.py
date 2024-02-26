import sys
sys.path.append('DataStructuresCourse_Educative\MyCustomDataStructures')
from graph import Graph
from node import Node


def dfs_traversal(graph: Graph, source):
    if graph.vertices == 0:
        return ""
    visited = [False] * (graph.vertices + 1)
    
    def dfs_traversal_helper(vertex):
        result = ""
        vertices_to_visit = [vertex]
        visited[vertex] = True
        while vertices_to_visit:
            curr_vertex = vertices_to_visit.pop()
            result += str(curr_vertex)
            
            temp_node: Node = graph.adj_list[curr_vertex].get_head()
            while temp_node:
                if not visited[temp_node.data]:
                    vertices_to_visit.append(temp_node.data)
                    visited[temp_node.data] = True
                temp_node = temp_node.next
        return result
    
    result = dfs_traversal_helper(source)
    for vertex in range(graph.vertices + 1):
        if not visited[vertex]:
            result += dfs_traversal_helper(vertex)
    return result


if __name__ == "__main__" :
    g = Graph(8)
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
        g.add_edge(2, 7)
        g.add_edge(5, 8)
        
        source = 1
        print(f"DFS traversal starting from vertex {source}: {dfs_traversal(g, 1)}")

