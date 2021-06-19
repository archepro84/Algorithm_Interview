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
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.

\w : Word Character,
^ : Not
"""


class Solution:
    def default(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                 if word not in banned]
        # counts = collections.defaultdict(int)
        # for word in words:
        #     counts[word] += 1
        # print(counts)

        #Counter로 최댓값을 첫번째 최댓값을 추출하여 어떤 단어인지 가져온다.
        counts2 = collections.Counter(words)
        return counts2.most_common(1)[0][0]

    """
    String을 List로 분해하여 [a-zA-Z0-9]가 아닌것들을 전부 ' '으로 치환(Substitute) 한다.
    치환한 데이터에서 모든 문자를 소문자로 변경한다.
    ' '(Space) 를 기준으로 떨어져 있던 단어들을 합친다.
    """


if __name__ == "__main__":
    example = Solution()
    result = example.default(paragraph="Bob hit a ball, the hit BALL flew far after it was hit.",
                             banned=["hit"])
    print(result)
