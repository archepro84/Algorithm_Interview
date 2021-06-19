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
    def default(self, prices: List[int]) -> int:
        max_price = 0

        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - price, max_price)
        return max_price

    def default2(self, prices: List[int]) -> int:
        # 입력값이 []인경우 -sys.maxsize 그대로 반환 될 수 있으므로 0으로 설정
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(price, min_price)
            profit = max(price, profit - min_price)
        return profit




if __name__ == "__main__":
    example = Solution()
    # result_example = example.default([7, 1, 5, 3, 6, 4])
    result_example = example.default2([7, 1, 5, 3, 6, 4])
    print(result_example)
