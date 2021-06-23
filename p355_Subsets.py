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
    def subsets(self, nums: List[int]) -> int:
        result = []

        def dfs(index, path):
            # 모든 탐색경로는 정답이므로 result에 추가해준다.
            result.append(path)
            # 경로를 만들면서 DFS
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])
        dfs(0, [])
        return result



if __name__ == "__main__":
    example = Solution()
    result_example = example.subsets([1, 2, 3])
    print(result_example)
