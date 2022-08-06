class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))
        return self

    # O(V + E) time | O(V) space
    def breadth_first_search(self, array):
        queue = [self]
        while queue:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
            if queue:
                current = queue[0]
        return array


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
