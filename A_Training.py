from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        
    def append(self, value):
        if not self.head:
            self.head = Node(value)
            self.length += 1
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)
        self.length += 1
        
        
    def add_at_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        
    def __str__(self) -> str:
        array = [None for _ in range(self.length)]
        curr = self.head
        counter = 0
        while curr:
            array[counter] = str(curr.data)
            counter += 1
            curr = curr.next
        return ", ".join(array)

class Graph:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.adjacency_list = [LinkedList() for _ in range(vertices)]
        
    def add_edge(self, source, destination):
        if 0 <= source < self.vertices and 0 <= destination < self.vertices:
            self.adjacency_list[source].add_at_head(destination)
            
    def __str__(self):
        for i in range(self.vertices):
            
            curr = self.adjacency_list[i].head
            result = []
            while curr:
                result.append(curr.data)
                curr = curr.next
            print(f"{i}: ", end="->".join(result))

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(5)
    ll.append(10)
    ll.add_at_head(3)
    print(ll)
    
    graph = Graph(3)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    print(graph)
    
    
    
    
 