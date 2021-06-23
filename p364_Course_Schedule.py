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
    def canFinish(self, num: int, prerequisites: List[List]) -> bool:
        graph = collections.defaultdict(list)
        # 각 그래프의 루트를 분해하여 dict에 삽입한다.
        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(i):
            if i in traced:
                return False
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            # 탐색 종료 후 탐색하였던 루트를 삭제한다.
            traced.remove(i)
            return True

        # 중복값이 들어올 일이 없으므로 set을 사용
        traced = set()
        # 순환 구조를 판별하기 위해 graph의 모든 인자로 for문을 실행한다.
        for x in list(graph):
            if not dfs(x):
                return False
        return True

    def canFinish_visit(self, num: int, prerequisites: List[List]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in graph:
            graph[x].append(y)

        def dfs(i):
            # 순환 구조일 경우
            if i in traced:
                return False
            # 이미 방문하였던 루트라면
            if i in visited:
                return True
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            visited.add(i)
            return True

        visited, traced = set(), set()
        for x in list(graph):
            if not dfs(x):
                return False
        return True


if __name__ == "__main__":
    example = Solution()
    # result_example = example.canFinish(2, [[1, 0]])
    result_example = example.canFinish_visit(2, [[1, 0]])
    print(result_example)
