from linked_list import LinkedList
from typing import List

class Graph():
    def __init__(self, vertices) -> None:
        """
        Initializes a graph with a specified number of vertices.

        Args:
            vertices (int): Total number of vertices in the graph
        """
        self.vertices: int = vertices
        self.array: List = [LinkedList() for _ in range(vertices)]
        
        
if __name__ == "__main__":
    graph = Graph(5)
    print()