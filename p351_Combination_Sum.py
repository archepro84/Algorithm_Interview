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
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        #path : 현재까지 추가된 List 값
        def dfs(csum, index, path):
            # 목표 값을 초과한 경우
            if csum < 0:
                return
            # csum의 초기값은 target이며, 따라서 csum의 0은 target과 일치하는 정답
            if csum == 0:
                result.append(path)
            # 자신 부터 하위 원소 까지의 나열 재귀 호출
            for i in range(index, len(candidates)):
                # combination 방법
                dfs(csum - candidates[i], i, path + [candidates[i]])
                # # permutation 방법
                # dfs(csum - candidates[i], 0, path + [candidates[i]])

        dfs(target, 0, [])
        return result


if __name__ == "__main__":
    example = Solution()
    result_example = example.combinationSum([2, 3, 5], 9)
    print(result_example)
