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
    dp = collections.defaultdict(int)

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs2(self, n: int) -> int:
        if n <= 2:
            return n
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climbStairs2(n - 1) + self.climbStairs2(n - 1)
        return self.dp[n]


if __name__ == "__main__":
    example = Solution()
    # result_example = example.climbStairs(3)
    result_example = example.climbStairs2(56)
    print(result_example)
