from collections import defaultdict
from typing import List


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False]*(c+1)
        groupId = [-1]*(c+1)
        curGroup = 0
        def dfs(node):
            visited[node] = True
            groupId[node] = curGroup
            for cnode in graph[node]:
                if visited[cnode]:
                    continue
                dfs(cnode)
        
        for station in range(1, c+1):
            if visited[station]:
                continue
            dfs(station)
            curGroup += 1
        
        groupMem = [[] for i in range(curGroup)]
        for station in range(1, c+1):
            gid = groupId[station]
            groupMem[gid].append(station)
        
        for li in groupMem:
            li.sort()
        indices = [0]*curGroup

        isOnline = [True]*(c+1)
        result = []
        for typ, station in queries:
            gid = groupId[station]
            if typ == 1:
                if isOnline[station]:
                    result.append(station)
                elif indices[gid] < len(groupMem[gid]):
                    result.append(groupMem[gid][indices[gid]])
                else:
                    result.append(-1)
            elif typ == 2:
                isOnline[station] = False
                ind = indices[gid]
                li = groupMem[gid]
                while ind < len(li) and isOnline[li[ind]] == False:
                    indices[gid] += 1
                    ind = indices[gid]

        return result