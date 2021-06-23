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
    grid: List[List[str]]  # 클래스 멤버 변수로 선언

    def dfs(self, grid: List[List[str]], i: int, j: int):
        # 더이상 땅이 아닌 경우 종료
        if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                grid[i][j] != '1':
            return
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        # 예외 처리
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    # 모든 육지를 탐색 후 카운트 1 증가
                    count += 1
        return count

    def numIslands2(self, grid: List[List[str]]) -> int:
        def dfs2(i, j):
            # 더이상 땅이 아닌 경우 종료
            if i < 0 or i >= len(grid) or \
                    j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1':
                return
            grid[i][j] = '0'

            dfs2(i + 1, j)
            dfs2(i - 1, j)
            dfs2(i, j + 1)
            dfs2(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs2(i, j)
                    count += 1
        return count


if __name__ == "__main__":
    example = Solution()

    input_data = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]
    result = example.numIslands2(input_data)
    print(result)
