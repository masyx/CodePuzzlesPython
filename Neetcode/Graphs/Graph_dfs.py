############# RECURSIVE ###################

def dfs_from_node_recursive(graph, node, visited):
    if node in visited:
        return

    visited.add(node)

    for nei in graph.get(node, []):
        dfs_from_node_recursive(graph, nei, visited)
        
def graph_traversal_recursive(graph):
    visited = set()

    for node in graph:
        if node not in visited:
            dfs_from_node_recursive(graph, node, visited)

    return visited    

############# ITERATIVE ###################
def dfs_from_node_iter(graph, node, visited):
    stack = [node]
    
    while stack:
        curr_node = stack.pop()
        if curr_node in visited:
            continue
        visited.add(curr_node)
        
        for nei in graph[curr_node]:
            if nei not in visited:
                stack.append(nei)
                
def graph_traversal_iterative(graph):
    visited = set()
    
    for node in graph:
        if node not in visited:
            dfs_from_node_iter(graph, node, visited)
            
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

    print(graph_traversal_recursive(adj_list))
    
    
    print(graph_traversal_iterative(adj_list))
    
if __name__ == "__main__":
    main()