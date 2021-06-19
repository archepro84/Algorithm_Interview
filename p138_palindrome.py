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
주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

Input
"A man, a plan, a canal: Panama"
Output
True

Input
"race a car"
Output
False


팰린드롬 : 앞뒤가 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어 또는 문장
"""


class Solution:
    def isPalindrome1(self, s: str) -> bool:
        # 문자열을 입력 받았을 경우 내부의 특수문자는 제외하며 모든 문자는 소문자 또는 대문자로 수정 한다.
        input_data = "A man, a plan, a canal: Panama"

        # 특수 문자 및 숫자 삭제
        strs = []
        for char in input_data:
            if char.isalnum():
                strs.append(char.lower())

        # print(' '.join(strs))

        # Palindrome 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True

    def isPalindrome2(self, s: str) -> bool:
        # 자료형을 Deque 형으로 선언
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # Palindrome 여부를 판별
        while len(strs) > 1:
            if strs.pop() != strs.popleft():
                return False

            return True

    """
    List의 pop(0)은 O(n)의 시간복잡도를 가지고있고
    Deque의 pop 및 popleft()는 O(1)이기 때문에 각각 n번씩 반복하면,
    List 구현은 O(n^2), Deque 구현은 O(n)으로 성능차이가 크다 
    """

    def isPalindrome3(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링 / ^ = not
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]  # 슬라이싱

    def isPalindrome4(self, s: str) -> bool:
        #C로 구현
        pass



if __name__ == "__main__":
    example = Solution()
    result = example.isPalindrome3("A man, a plan, a canal: Panama")
    print(result)
