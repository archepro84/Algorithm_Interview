import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

"높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라"


class Solution:
    def trap1(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume

    """
    . distance : 현재 index와 stack의 최근 들어온 인덱스를 비교하여 몇칸이 떨어져 있는지 확인한다.
    . waters : 1칸당 추가해야할 물의 높이 
             : 현재의 height와 그전의 height를 비교하여 제일 적은값 과 현재 계산의 시작점이 되는 높이를 뺀다 

    . height[i] : 지금 계산중인 현재의 높이 
    . height[stack[-1]] : 현재 계산의 최고점이 되는 높이 
    . hieght[top] : 현재 계산의 시작점이 되는 높이 
    """


    # 스택 쌓기
    def trap2(self, height: List[int]) -> int:
        stack = []
        volume = 0
        print(height.__len__())
        for i in range(len(height)):
            # 변곡점을 만나는 경우
            print(f'\nheight[stack] = {[height[x] for x in stack]}, stack = {stack}')

            # Stack리스트의 값이 존재하고, 현재의 높이가 마지막에 들어온 가장 큰 값보다 클 경우
            while stack and height[i] > height[stack[-1]]:

                # 스택에서 꺼낸다
                top = stack.pop()

                # 현재 stack의 값이 존재하지 않을 경우
                if not len(stack):
                    break

                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters
                # print(f'i = {i}, stack[-1] = {stack[-1]}')
                print(f"height[i] = {height[i]}, height[stack[-1]] : {height[stack[-1]]}")
                print(f'distance : {distance}, waters : {waters}, volume : {volume}, height[top] : {height[top]}')
            stack.append(i)

        return volume


if __name__ == "__main__":
    example = Solution()
    # result_example = example.trap1([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    # result_example = example.trap2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    result_example = example.trap2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 0, 2])
    print(result_example)
