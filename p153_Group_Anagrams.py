import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

# 애너그램은 문자열 정렬을 하면 같은 값을 가진다.
"문자열 배열을 받아 애너그램 단위로 그룹핑 하라"


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            # sorted(word) : String 형식을 문자열로 변경하여 정렬한다.
            # ''.join() : List형식을 String 형식으로 변경한다.
            anagrams[''.join(sorted(word))].append(word)

        # list(anagrams.values() : anagrams.values만 사용 한다면 dictvalues 형식으로 반환이 된다.
        return list(anagrams.values())


if __name__ == "__main__":
    example = Solution()
    result = example.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

    print(result)
    print(type(result))
