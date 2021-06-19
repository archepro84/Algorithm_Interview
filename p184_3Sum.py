import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

"배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라."


class Solution:
    # 브루트 포스
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기 
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append([nums[i], nums[j], nums[k]])
        return result

    # 투 포인터
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append((nums[i], nums[left], nums[right]))

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
        return result


if __name__ == "__main__":
    example = Solution()
    # result_example = example.threeSum1([-1, 0, 1, 2, -1, -4])
    result_example = example.threeSum2([-1, 0, 1, 2, -1, -4])
    print(result_example)
