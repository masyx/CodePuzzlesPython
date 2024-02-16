from collections import deque
import sys
sys.path.append('DataStructuresCourse_Educative\MyCustomDataStructures')
from graph import Graph


def bfs_traversal(g, source):
    # Function to perform BFS starting from a specific vertex
    def bfs_from_source(source, visited):
        result = ""
        queue = deque([source])  # Initialize the queue with the source vertex
        visited[source] = True  # Mark the source vertex as visited

        while queue:
            current_vertex = queue.popleft()
            result += str(current_vertex)

            # Iterate through all the adjacent vertices of the dequeued vertex
            # If an adjacent has not been visited, then mark it as visited and enqueue it
            temp = g.array[current_vertex].get_head()
            while temp is not None:
                if not visited[temp.data]:
                    visited[temp.data] = True
                    queue.append(temp.data)
                temp = temp.next
        return result

    result = ""
    visited = [False] * g.vertices  # Keeps track of visited vertices for the entire graph

    # Start BFS from the specified source
    result += bfs_from_source(source, visited)

    # Continue BFS from any unvisited vertex to ensure all components are covered
    for i in range(g.vertices):
        if not visited[i]:
            new_result =  bfs_from_source(i, visited)
            result += new_result
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
        print(f"BFS traversal starting from vertex {source}: {bfs_traversal(g, 1)}")
