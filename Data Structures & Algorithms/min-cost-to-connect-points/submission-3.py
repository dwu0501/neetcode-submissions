import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = [[] for x in range(len(points))]
        for i in range (len(points)):
            for j in range(i+1, len(points)):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

                adj[i].append((j, distance))
                adj[j].append((i, distance))

        V = len(adj)
    
        # Min-heap storing (weight, vertex)
        pq = []
        visited = [False] * V
        res = 0

        # Start from node 0
        heapq.heappush(pq, (0, 0))

        while pq:

            wt, u = heapq.heappop(pq)
            if visited[u]:
                continue

            res += wt
            visited[u] = True
            # Push adjacent edges
            for v in adj[u]:
                if not visited[v[0]]:
                    heapq.heappush(pq, (v[1], v[0]))

        return res