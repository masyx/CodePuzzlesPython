import sys
sys.path.append('DataStructuresCourse_Educative\MyCustomDataStructures')
from graph import Graph
from node import Node

def dfs_traversal_helper(graph: Graph, source, visited):
    result = ""
    stack = [source]
    visited[source] = True
    
    while stack:
        current_vertex = stack.pop()
        result += str(current_vertex)
        
        # get head node from the adjacency list of the current vertex
        temp: Node = graph.adj_list[current_vertex].get_head()
        while temp:
            if not visited[temp.data]:
                stack.append(temp.data)
                visited[temp.data] = True
            temp = temp.next
            
    return result

def dfs_traversal(graph: Graph, source):
    num_of_vertices = graph.vertices
    if num_of_vertices == 0:
        return ""
    
    visited = [False for _ in range(num_of_vertices)]
    result = dfs_traversal_helper(graph, source, visited)
    
    for i in range(num_of_vertices):
        if not visited[i]:
            result += dfs_traversal_helper(graph, i, visited)
    return result

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
        
        source = 1
        print(f"DFS traversal starting from vertex {source}: {dfs_traversal(g, 1)}")

