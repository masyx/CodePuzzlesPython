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
        self.adj_list: List = [LinkedList() for _ in range(vertices)]
        
    def add_edge(self, source, destination):
        if (0 <= source < self.vertices and 0 <= destination <= self.vertices):
            self.adj_list[source].insert_at_head(destination)

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.adj_list[i].get_head()
            while temp is not None:
                print("[", temp.data, end=" ] -> ")
                temp = temp.next
            print("None")
        
        
if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 2)
    g.add_edge(0, 1)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    

    g.print_graph()

    print(g.adj_list[1].get_head().data)