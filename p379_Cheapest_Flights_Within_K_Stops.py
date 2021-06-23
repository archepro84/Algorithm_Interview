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
n : 노드의 갯수
edges : 경로
src : 시작점
dst : 도착점
K : 경유지
"""


# 페이지 번호는 리디가 아닌 책내부 기준
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # 가격을 시간이라고 가정
        # 우선순위 큐에 추가할 때 K 이내일 때만 경로를 추가하여 K를 넘어서는 경로는 더 이상 탐색되지 않게 설정

        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        #최대 경유지 값인 K를 우선순위 큐에 추가
        Q = [(0, src, K)]

        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k - 1))
        return -1


if __name__ == "__main__":
    example = Solution()
    result_example = example.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0)
    print(result_example)
