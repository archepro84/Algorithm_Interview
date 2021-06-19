import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

"""가장 긴 팰린드롬 부분 문자열을 출력하라.
팰린드롬 : 앞에서 읽으나 뒤에서 읽으나 동일한 문자열"""


class Solution:
    def default(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            # 포인터가 팰린드롬을 발견하였을 경우 좌측과 우측 1칸씩 확장하여 재검색 한다.
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # while문을 종료할 경우 해당하는 left, right값이 +-1이 되기때문에 Left +1 , Right형식으로 슬라이싱한다.
            return s[left + 1:right]

        # 길이가 1 OR 자기자신을 뒤집었을경우 자기자신 일 경우
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''

        # 총 문자열 길이 만큼 Loop한다.
        for i in range(len(s) - 1):
            # 문자의 길이를 key 값으로 지정하고 최대의 길이를 가지는 것을 result로 정의한다.
            # 홀수의 포인터와 짝수의 포인터 2가지를 사용한다.
            result = max(result,
                         expand(i, i + 1),  # 짝수의 포인터
                         expand(i, i + 2),  # 홀수의 포인터
                         key=len)
            # print(f"expand(i, i+2) == {expand(i, i + 2)} == i = {i}, i+2 == {i + 2}")
        print(expand(0, 2))
        return result
        pass


if __name__ == "__main__":
    example = Solution()
    # result_example = example.default('12332115264822131231')
    result_example = example.default('123212')
    print(result_example)
