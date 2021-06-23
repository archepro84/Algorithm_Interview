import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *


# 페이지 번호는 리디가 아닌 책내부 기준
class Solution:
    def __init__(self):
        self.graph = {
            1: [2, 3, 4],
            2: [5],
            3: [5],
            4: [],
            5: [6, 7],
            6: [],
            7: [3],
        }

        # self.graph = {
        #     1: [2, 3, 4],
        #     2: [4],
        #     3: [4],
        # }

    def default(self, nums: List[int]) -> int:
        pass

    #  Lexicographical Order (사전식 순서)로 방문
    def recursive_dfs(self, v, discovered=[]):
        discovered.append(v)
        # 현재의 graph의 저장된 경로들을 list형식으로 분해한다.
        for w in self.graph[v]:
            print(w)
            # graph에서 분해한 경로들이 discovered에 존재하지 않는다면. 재귀형식으로 반복한다.

            if not w in discovered:
                discovered = self.recursive_dfs(w, discovered)
        return discovered

    # 역순으로 방문
    # 스택으로 구현하여 가장 마지막에 삽입된 노드부터 꺼내서 반복
    # 이 경우 인접 노드에서 가장 최근에 담긴 노드, 즉 가장 마지막부터 방문
    def iterative_dfs(self, start_v):
        discovered = []
        stack = [start_v]
        while stack:
            v = stack.pop()
            if v not in discovered:
                discovered.append(v)
                for w in self.graph[v]:
                    stack.append(w)
        return discovered

    def iterative_bfs(self, start_v):
        discovered = [start_v]
        queue = [start_v]
        while queue:
            # 저장된 dictionary를 꺼낸다.
            v = queue.pop(0)
            for w in self.graph[v]:
                if w not in discovered:
                    discovered.append(w)
                    queue.append(w)
        return discovered


if __name__ == "__main__":
    example = Solution()
    # result_example = example.default([])
    # print(result_example)
    print(example.recursive_dfs(1))
    print(example.iterative_dfs(1))
    print(example.iterative_bfs(1))
