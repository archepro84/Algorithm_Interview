import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

"""
u : Start Point
v : End Point
w : Time
N : Node의 갯수
K : Start Node Point
"""


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:

        # 그래프 인접 리스트 구성
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        print(graph)
        # 우선 순위 큐를 위한 큐 변수 생성 / (소요 시간, 정점)
        # 시작점 > 정점까지의 소요 시간
        Q = [[0, K]]

        # 거리를 의미하는 변수
        dist = collections.defaultdict(int)

        # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)
            
            # 정점의 포함여부를 체크한다.
            if node not in dist:
                dist[node] = time # 정점을 추가한다
                for v, w in graph[node]:  # graph의 Start Point를 검색해서 Loop 한다.
                    # 현재 정점의 시간 + 다음 End Point까지의 걸리는 시간을 추가한다.
                    alt = time + w

                    # Q에 현재까지의 축적된 시간과 이동된 루트를 삽입한다.
                    heapq.heappush(Q, (alt, v))
        print(dist)
        # 전체 노드 개수만큼이 모두 dist에 있다면 모든 노드의 최단 경로를 구했다는 의미
        if len(dist) == N:
            return max(dist.values())
        return -1


if __name__ == "__main__":
    example = Solution()
    result_example = example.default([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)
    print(result_example)
