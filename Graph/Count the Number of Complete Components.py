# 2685. Count the Number of Complete Components

from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node, component):
            visited[node] = True
            component.append(node)
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei, component)

        for i in range(n):
            if not visited[i]:
                component = []
                dfs(i, component)

                k = len(component)
                edge_count = 0

                for node in component:
                    edge_count += len(graph[node])

                edge_count //= 2  # Each edge counted twice

                if edge_count == k * (k - 1) // 2:
                    ans += 1

        return ans
