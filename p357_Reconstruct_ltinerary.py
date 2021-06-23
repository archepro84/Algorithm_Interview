import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from audioop import reverse
from typing import *


# 페이지 번호는 리디가 아닌 책내부 기준
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)
        route = []

        # 어휘 순으로 방문해야 한다.
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)

        dfs('JFK')
        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]

    def findItinerary_stack(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)
        route = []

        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)

        dfs("JFK")
        return route[::-1]

    def findItinerary_loop(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)
        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        return route[::-1]


if __name__ == "__main__":
    example = Solution()
    # result_example = example.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
    # result_example = example.findItinerary_stack([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
    result_example = example.findItinerary_loop([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
    print(result_example)
