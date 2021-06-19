import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

"정렬되어 있는 두 연결 리스트를 합쳐라"


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # <정렬되어 있는>
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # l1이 비어있거나
        # l2가 비어있지않고 l1.val이 l2.val보다 큰경우
        # (not l1)은 마지막 l1 = None / l2 = Data가 존재할 경우 변경하기 위해서 사용한다.
        # 마지막 l1 = None, l2 = 4에서는 / l1 = 4 / l2 = None으로 변경된다.
        # l1과 l2의 값을 비교해 작은 값이 왼쪽에 오도록한다.
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1

        # 마지막전 단계에서 l1 = 4 , l2 = 4에서 재귀호출을 할 시
        # l1.next = None이므로 return l1을 하게된다.
        # 즉 l1.next = l2값이 삽입된다.
        # next는 그다음 값이 엮이도록 재귀 호출
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1


if __name__ == "__main__":
    node1_1 = ListNode(1)
    node1_2 = ListNode(2)
    node1_3 = ListNode(4)
    node1_1.next = node1_2
    node1_2.next = node1_3

    node2_1 = ListNode(1)
    node2_2 = ListNode(3)
    node2_3 = ListNode(4)
    node2_1.next = node2_2
    node2_2.next = node2_3

    example = Solution()
    result_example = example.mergeTwoLists(node1_1, node2_1)
    print(result_example)
    for x in range(6):
        print(result_example.val, end=" ")
        result_example = result_example.next
