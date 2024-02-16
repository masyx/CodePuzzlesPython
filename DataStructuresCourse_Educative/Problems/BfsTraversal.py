from collections import deque
import sys
sys.path.append('DataStructuresCourse_Educative\MyCustomDataStructures')
from my_stack import MyStack
from my_queue import MyQueue
from graph import Graph


def bfs_traversal_helper(g: Graph, source, visited):
    result = ""
    # Create Queue(implemented in previous lesson) for Breadth First Traversal
    # and enqueue source in it
    queue = MyQueue()
    queue.enqueue(source)
    visited[source] = True # Mark as visited
    # Traverse while queue is not empty
    while not queue.is_empty():
        # Dequeue a vertex/node from queue and add it to result
        current_node = queue.dequeue()
        result += str(current_node)
        # Get adjacent vertices to the current_node from the list,
        # and if they are not already visited then enqueue them in the Queue
        temp = g.array[current_node].head_node
        while temp is not None:
            if not visited[temp.data]:
                queue.enqueue(temp.data)
                visited[temp.data] = True  # Visit the current Node
            temp = temp.next
    return result, visited

def bfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        return result
    # A list to hold the history of visited nodes
    # Make a node visited whenever you enqueue it into queue
    visited = []
    for i in range(num_of_vertices):
        visited.append(False)
    # Start from source
    result, visited = bfs_traversal_helper(g, source, visited)
    # visit remaining nodes
    for i in range(num_of_vertices):
        if not visited[i]:
            result_new, visited = bfs_traversal_helper(g, i, visited)
            result += result_new
    return result



def bfs_on_each_component(g, source):
    """
    Perform BFS starting from a specified source vertex and ensure BFS is performed on each disconnected component of the graph.
    
    Args:
        g (Graph): The graph on which to perform BFS.
        source (int): The index of the source vertex from which to start BFS.
    """
    visited = [False] * g.vertices  # Keeps track of visited vertices for the entire graph

    # Function to perform BFS starting from a specific vertex
    def bfs_from_source(source):
        queue = deque([source])  # Initialize the queue with the source vertex
        visited[source] = True  # Mark the source vertex as visited

        while queue:
            current_vertex = queue.popleft()
            print(current_vertex, end=" ")

            # Iterate through all the adjacent vertices of the dequeued vertex
            # If an adjacent has not been visited, then mark it as visited and enqueue it
            temp = g.array[current_vertex].get_head()
            while temp is not None:
                if not visited[temp.data]:
                    visited[temp.data] = True
                    queue.append(temp.data)
                temp = temp.next

    # Start BFS from the specified source
    print(f"BFS traversal starting from vertex {source}: ", end="")
    bfs_from_source(source)
    print()  # Newline for formatting

    # Continue BFS from any unvisited vertex to ensure all components are covered
    for i in range(g.vertices):
        if not visited[i]:
            print(f"BFS traversal starting from vertex {i}: ", end="")
            bfs_from_source(i)
            print()  # Newline for formatting




if __name__ == "__main__" :
    g = Graph(6)
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        print("Graph is empty")
    elif num_of_vertices < 0:
        print("Graph cannot have negative vertices")
    else:
        # g.add_edge(0, 1)
        # g.add_edge(0, 2)
        # g.add_edge(1, 3)
        # g.add_edge(2, 3)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(3, 0)
        g.add_edge(3, 1)
        g.add_edge(1, 4)
        g.add_edge(1, 5)
        g.add_edge(4, 5)
        

        print(bfs_traversal(g, 1))
        bfs_on_each_component(g, 1)