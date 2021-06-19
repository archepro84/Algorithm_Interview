import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

"덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라."


class Solution:

    # 브루트 포스
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        pass

    # in을 이용한 탑색
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n
            if complement in nums[i + 1:]:
                return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]
        pass

    def twoSum3(self, nums: List[int], target: int) -> str:
        nums_map = {}

        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            # nums_map.keys()를 사용하지 않는 이유는?
            if target - num in nums_map and i != nums_map[target - num]:
                print(num)
                return [i, nums_map[target - num]]

    def twoSum4(self, nums: List[int], target: int) -> str:
        nums_map = {}
        # 하나의 for 문으로 통합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                # 만들어 지고 난 이후 생성하기 때문에 i가 뒤로 와야한다.
                return [nums_map[target - num], i]
            nums_map[num] = i

    # 투 포인터 이용 / nums의 값이 정렬이 되어 있어야 한다.
    def twoSum5(self, nums: List[int], target: int) -> str:
        # 정렬 되어 있지 않을 경우
        nums.sort()

        left, right = 0, len(nums) - 1
        while not left == right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                return [left, right]


if __name__ == "__main__":
    example = Solution()
    # result_example = example.twoSum1(nums=[2, 7, 11, 15], target=9)
    # result_example = example.twoSum2(nums=[2, 7, 11, 15], target=26)
    # result_example = example.twoSum3(nums=[2, 7, 11, 15], target=26)
    # result_example = example.twoSum4(nums=[2, 7, 11, 15], target=26)
    result_example = example.twoSum5(nums=[2, 7, 11, 15], target=26)
    print(result_example)
