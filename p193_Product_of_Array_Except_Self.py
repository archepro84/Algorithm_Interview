import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
import time
import timeit
from typing import *

"배열을 입력받아 oustput[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라."
"나눗셈을 하지 않고O(n)에 풀이하라."


# 자기자신을 기준으로 왼쪽에 있는 값의 곱셈과 오른쪽에 있는 값의 곱셈을 곱하면 된다.

class Solution:
    def default(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        # 자신의 기준으로 왼쪽값의 모든 곱셈
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        # 자신의 기준으로 오른쪽 값의 모든 곱셈
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]

        return out


if __name__ == "__main__":
    start_time = timeit.default_timer()
    print(start_time * 10000)
    example = Solution()
    result_example = example.default([1, 2, 3, 4])
    print(result_example)
    print((timeit.default_timer() - start_time) * 10000000)
