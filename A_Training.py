class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, value):
        self.children.append(Node(value))
        
    def breadth_first_search(self, result: list):
        queue = [self]
        while queue:
            current_node = queue.pop(0)
            result.append(current_node.value)
            for child in current_node.children:
                queue.append(child)
        return result


def main():
    root = Node('A')
    root.add_child('B')
    root.add_child('C')
    root.add_child('D')

    root.children[0].add_child('E')
    root.children[0].add_child('F')
    root.children[0].children[1].add_child('I')
    root.children[0].children[1].add_child('J')

    root.children[2].add_child('G')
    root.children[2].add_child('H')
    root.children[2].children[0].add_child('K')
    result = []
    print(root.breadth_first_search(result))

if __name__ == '__main__':
    main()