from typing import List
from typing import Dict
from collections import defaultdict

def build_adj_list(n, edges: List[List[int]])-> Dict[int, List[int]]:
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    return adj_list



if __name__ == "__main__":
    n = 4
    edges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2]]
    """
    expected adj_list:
    {
    0: [1, 3, 2],
    1: [0, 2],
    2: [1, 3, 0],
    3: [2, 0]
    }
    """
    print(build_adj_list(n, edges))