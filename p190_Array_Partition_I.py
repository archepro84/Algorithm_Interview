import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

"n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라"


class Solution:
    # 오름차순 풀이
    def ArrayPairSum1(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()
        for n in nums:
            # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                # print(pair)
                pair = []
        return sum

    def ArrayPairSum2(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()
        for i, num in enumerate(nums):
            if i % 2 == 0:
                sum += num
        return sum

    def ArrayPairSum3(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


if __name__ == "__main__":
    example = Solution()
    # result_example = example.ArrayPairSum1([1, 4, 3, 2])
    # result_example = example.ArrayPairSum2([1, 4, 3, 2])
    result_example = example.ArrayPairSum3([1, 4, 3, 2])
    print(result_example)
