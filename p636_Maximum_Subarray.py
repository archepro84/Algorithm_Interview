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
    def maxSubArray(self, nums: List[int]) -> int:
        sums: List[int] = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(nums[i] + (sums[i - 1] if sums[i - 1] > 0 else 0))
        return max(sums)

    def maxSubArray2(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            # Plus 한 이전의 값이 음수가 아닐 경우 합산한다.
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        print(nums)
        return max(nums)

    def maxSubArray_Kadene(self, nums: List[int]) -> int:
        # 계산된 숫자들 중에서 가장 컸을때의 값으 저장
        best_sum = -sys.maxsize
        # 현재까지 계산된 총 합
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
            print(num, current_sum, best_sum)
        return best_sum


if __name__ == "__main__":
    example = Solution()
    # result = example.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    # result = example.maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    result = example.maxSubArray_Kadene([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(result)
