class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
    
    def depthFirstSearch_stack(self, array):
        stack = []
        stack.append(self)
        while stack:
            current = stack.pop()
            array.append(current.name)
            for child in reversed(current.children):
                stack.append(child)
        return array


def main():
    root = Node('A')
    root.addChild('B')
    root.addChild('C')
    root.addChild('D')
    
    root.children[0].addChild('E')
    root.children[0].addChild('F')
    root.children[0].children[1].addChild('I')
    root.children[0].children[1].addChild('J')
    
    root.children[2].addChild('G')
    root.children[2].addChild('H')
    root.children[2].children[0].addChild('K')
    
    

    
    array = []
    print(root.depthFirstSearch_stack(array))

if __name__ == '__main__':
    main()