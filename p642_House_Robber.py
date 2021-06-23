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
    def rob(self, nums: List[int]) -> int:
        def _rob(i: int) -> int:
            if i < 0:
                return 0
            return max(_rob(i - 1), _rob(i - 2) + nums[i])

        return _rob(len(nums) - 1)

    def rob2(self, nums: List[int]) -> int:
        # 들어오는 리스트의 값이 비었다면.
        if not nums:
            return 0
        # 2개 이하라면 1개밖에 선택이 불가능하다.
        if len(nums) <= 2:
            return max(nums)
        dp = collections.OrderedDict()

        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp.popitem()[1]


if __name__ == "__main__":
    example = Solution()
    # result_example = example.rob([9, 3, 9, 8])
    result_example = example.rob2([9, 3, 9, 8])
    print(result_example)
