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
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            # 리프 노드일 때 결과 추가
            if len(elements) == 0:
                # prev_elements를 바로
                # 사용하면 참조로서 append 되기 때문에 새로 생성하여 삽입한다.
                results.append(prev_elements[:])

            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return results

    def permute2(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            # 왜 0일때 추가하는 것일까?
            if len(elements) == 0:
                print("Elements : ", prev_elements)
                results.append(prev_elements[:])
            for e in elements:
                next_elements = elements[:]
                # 현재의 element를 삭제한다. 즉 [2,3]으로 만듬
                # [2,3] > [1,3] > [2,3]
                next_elements.remove(e)
                print(next_elements)
                # prev : [1]
                prev_elements.append(e)
                dfs(next_elements)
                # prev [0]
                prev_elements.pop()

        dfs(nums)
        return results

    # itertools : c라이브러리라 시간이 좀더 빠름
    def permute_iter(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))


if __name__ == "__main__":
    example = Solution()
    result_example = example.permute_iter([1, 2, 3])
    print(result_example)
