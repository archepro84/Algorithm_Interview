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
로그를 재정렬하라.
 1. 로그의 가장 앞 부분은 식별자다.
 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
 4. 숫자 로그는 입력 순서대로 한다.
"""


# def func(x):
#     return x.split()[1], x.split()[0]


class Solution:
    def default(self, logs: List[str]) -> List[str]:
        letters, digits = [], []

        for log in logs:
            print(log.split())
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        print(f"digits : {digits}")
        print(f"letters : {letters}")

        # letters.sort(key=func)
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits

    """
    List내부의 Str을 split함수를 사용하여 List형식으로 분해
    분해한 Data의 데이터를 나타내는 2번째 문장을 가져와 숫자인지 단어인지 확인한다.
    """


if __name__ == "__main__":
    example = Solution()
    result = example.default(
        ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero", "let4 art amazon"])
    print(result)
