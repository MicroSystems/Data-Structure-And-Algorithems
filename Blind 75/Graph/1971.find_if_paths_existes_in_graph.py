from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # BFS with Queue

        # build graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(U)

        seen = set()
        seen.add(source)
        q = deque()
        q.append(source)

        while q:
            curr_node = q.popleft()
            if curr_node == destination:
                return True

            for node in graph[curr_node]:
                if node not in seen:
                    seen.add(node)
                    q.append(node)

        return False 