from collections import deque

def graph_bfs_from_node(graph, node, visited = None):
    if visited is None:
        visited = set()
    
    q = deque([node])
    visited.add(node)
    
    while q:
        curr_node = q.popleft()
        
        for nei in graph.get(curr_node, []):
            if nei not in visited:
                q.append(nei)
                visited.add(nei)
    return visited

def bfs_full_graph(graph):
    if not graph:
        return set()
    
    visited = set()
    
    for node in graph:
        if node not in visited:
            graph_bfs_from_node(graph, node, visited)
            
    return visited




#   Graph:
#           0
#          / \
#         1 ->2
#        / \   \
#       3 ->4   5       99(not connected node)
def main():
    adj_list = {
        0:[1, 2],
        1:[2, 3, 4],
        2:[5],
        3:[4],
        4:[],
        5:[],
        99: []
    }
        
    print(f"Graph traversal from node: {graph_bfs_from_node(adj_list, 0)}")
    print(f"Entire graph traversal(including disconnected nodes): {bfs_full_graph(adj_list)}")
    
if __name__ == "__main__":
    main()