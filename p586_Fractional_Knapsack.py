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
    def default(self, nums: List[int]) -> int:
        pass


# 단가를 계산하고, 역순으로 정렬 / 가장 단가가 높은 짐이 맨 위에 오도록 구현
def fractional_knapsack(cargo):
    capacity = 15
    pack = []

    # 단가 계산 역순 정렬
    for c in cargo:
        # print((c[0] / c[1], c[0], c[1]))
        pack.append((c[0] / c[1], c[0], c[1]))
    pack.sort(reverse=True)
    print(pack)

    # 단가 순 그리디 계산
    total_value: float = 0
    for p in pack:
        # p[2] : 현재 짐의 무게
        if capacity - p[2] >= 0:
            capacity -= p[2]
            total_value += p[1]

        # 현재 짐의 무게가 총 등짐의 무게를 초과하였을 때
        else:
            # 현재 남은 무게에서 추가할 짐의 무게를 나눈다.
            fraction = capacity / p[2]
            # 총 가격에서 추가할 짐의 단가에서 무게의 %만큼 나누어 추가한다.
            total_value += p[1] * fraction
            break
    return total_value




if __name__ == "__main__":
    example = Solution()

    # 가격, 무게
    cargo = [
        (4, 12),
        (2, 1),
        (10, 4),
        (1, 1),
        (2, 2),
    ]
    r = fractional_knapsack(cargo)
    print(r)
