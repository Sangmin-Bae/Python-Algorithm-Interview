from collections import deque

class Solutions:
    @staticmethod
    def make_graph01(n, edge):
        graph = {}
        for i in range(1, n+1):
            graph[i] = []

        for a, b in edge:
            graph[a].append(b)
            graph[b].append(a)

        return graph

    def solution01(self, n, edge):
        answer = 0
        graph = self.make_graph01(n, edge)

        result = []
        queue = [(0, 1)]
        visited = {1}

        while queue:
            level, node = queue.pop(0)
            result.append((level, node))
            level += 1
            for n_i in graph[node]:
                if n_i not in visited:
                    visited.add(n_i)
                    queue.append((level, n_i))

        result.sort(reverse=True)
        max_level = result[0][0]
        for level, node in result:
            if level < max_level:
                break
            answer += 1

        return answer

    @staticmethod
    def make_graph02(n, edge):
        graph = [[] for _ in range(n + 1)]

        for a, b in edge:
            graph[a].append(b)
            graph[b].append(a)

        return graph

    def solution02(self, n, edge):
        graph = self.make_graph02(n, edge)
        distance = [-1 for _ in range(n + 1)]
        distance[1] = 0

        queue = deque([1])

        while queue:
            node = queue.popleft()
            for n_i in graph[node]:
                if distance[n_i] == -1:
                    distance[n_i] = distance[node] + 1
                    queue.append(n_i)

        distance.sort(reverse=True)

        return distance.count(distance[0])

if __name__ == "__main__":
    n = 6
    vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [5, 2]]

    sol = Solutions()

    print(f"Solution 01 Output: {sol.solution01(n, vertex)}")
    print(f"Solution 02 Output: {sol.solution02(n, vertex)}")
