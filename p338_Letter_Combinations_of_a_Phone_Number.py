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
    def letterCombinations(self, digits: str) -> List[str]:
        # path : 현재 들어와 있는 첫번째 글자를 저장하는 string
        def dfs(index, path):
            # 끝까지 탐색하면 백트래킹
            print(path, result)
            if len(path) == len(digits):
                result.append(path)
                return
            for i in range(index, len(digits)):
                # 숫자에 해당하는 모든 문자열 반복
                # dic인 Dictionary에서 digits의 첫번째 2로 인덱스를 검색한다.
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)

        if not digits:
            return []
        # 핸드폰의 키판 배열
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        dfs(0, "")
        return result


if __name__ == "__main__":
    example = Solution()
    result = example.letterCombinations("23")
    print(result)
