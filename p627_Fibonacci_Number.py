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


def zero_one_knapsack(cargo):
    capacity = 15
    pack = []

    for i in range(len(cargo) + 1):
        pack.append([])
        for c in range(capacity + 1):
            if i == 0 or c == 0:
                pack[i].append(0)
            elif cargo[i - 1][1] <= c:
                pack[i].append(
                    max(
                        cargo[i - 1][0] + pack[i - 1][c - cargo[i - 1][1]],
                        pack[i - 1][c]
                    ))
                if i == 1:
                    print(cargo[i - 1][0] + pack[i - 1][c - cargo[i - 1][1]])
            else:
                pack[i].append(pack[i - 1][c])
    return pack[-1][-1]


if __name__ == "__main__":
    example = Solution()

    cargo = [
        (4, 12),
        (2, 1),
        (10, 4),
        (1, 1),
        (2, 2),
    ]
    r = zero_one_knapsack(cargo)
    print(r)
