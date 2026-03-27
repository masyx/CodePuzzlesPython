class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        # Helpful in debugger/watch window
        neighbor_vals = [n.val for n in self.neighbors]
        return f"Node(val={self.val}, neighbors={neighbor_vals})"


def clone_graph(node):
    """
    Returns a deep copy of the graph starting from 'node'.

    Core idea:
    - old_to_new maps each original node object to its cloned node object
    - if we revisit a node, we return its existing clone
    - this prevents infinite recursion on cycles
    """
    if node is None:
        return None

    old_to_new = {}

    def dfs(curr):
        # If we already cloned this node, reuse that clone
        if curr in old_to_new:
            return old_to_new[curr]

        # Create the clone first
        copy = Node(curr.val)
        old_to_new[curr] = copy

        # Then clone neighbors and connect them
        for nei in curr.neighbors:
            copy.neighbors.append(dfs(nei))

        return copy

    return dfs(node)


def build_sample_graph():
    """
    Builds this undirected graph:

        1 -- 2
        |    |
        4 -- 3

    Adjacency:
    1: [2, 4]
    2: [1, 3]
    3: [2, 4]
    4: [1, 3]

    Returns node 1.
    """
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    return n1


def traverse_graph(node):
    """
    Returns a dict like:
    {1: [2, 4], 2: [1, 3], ...}

    This is just for easy inspection/printing.
    """
    if node is None:
        return {}

    visited = set()
    result = {}

    def dfs(curr):
        if curr in visited:
            return
        visited.add(curr)

        result[curr.val] = [nei.val for nei in curr.neighbors]

        for nei in curr.neighbors:
            dfs(nei)

    dfs(node)
    return result


def main():
    original = build_sample_graph()
    cloned = clone_graph(original)

    print("Original graph adjacency:")
    print(traverse_graph(original))
    print()

    print("Cloned graph adjacency:")
    print(traverse_graph(cloned))
    print()

    # These should have the same values / structure...
    print("original.val == cloned.val:", original.val == cloned.val)

    # ...but they must be different objects
    print("original is cloned:", original is cloned)

    # Same for neighbors
    print(
        "original.neighbors[0].val == cloned.neighbors[0].val:",
        original.neighbors[0].val == cloned.neighbors[0].val,
    )
    print(
        "original.neighbors[0] is cloned.neighbors[0]:",
        original.neighbors[0] is cloned.neighbors[0],
    )


if __name__ == "__main__":
    main()
