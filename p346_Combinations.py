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
    # 하나의 알고리즘을 풀이하기 위해
    # 해당하는 수식 또는 서식을 이해하고, 그것을 만들어내면 풀이가 가능하다.
    # 수식을 통해 코드를 구성해야 한다.
    def combinations(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
                return
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return results

    # k : 조합의 갯수
    def combinations2(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
            for i in range(start, n + 1):
                elements.append(i)
                # i + 1 : 한 칸씩 내려가기 위해서 사용
                # k - 1 : 내부 리스트의 출력 개수를 k개 만큼 맞추기 위해 1개 씩 뺀다.
                # 즉 k = 0 : 내부 리스트 출력이 전부 준비가 되었다는 뜻
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return results

    def combinations_iter(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n + 1), k))


if __name__ == "__main__":
    example = Solution()
    result_example = example.combinations_iter(5, 3)
    print(result_example)
