import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

"""
문자열을 뒤집는 함수를 작성하라. 
입력값을 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라
"""


class Solution:

    # Two Pointer(투 포인터) 스왑 : 2개의 포인터를 이용해 범위를 조정해가며 풀이
    def reverseString1(self, s: List[str]) -> None:
        # 왜 1줄로 쓰는것일까?
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        print(s)

    # Pythonic way(Python 다운 방식)
    def reverseString2(self, s: List[str]) -> None:
        s.reverse()
        print(s)


if __name__ == "__main__":
    example = Solution()
    example.reverseString2([x for x in "Hello world"])
    # print(result)
