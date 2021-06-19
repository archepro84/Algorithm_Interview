import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 페이지 번호는 리디가 아닌 책내부 기준
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)

    def reverseList2(self, head: ListNode) -> ListNode:
        node, prev = head, None
        "node == not None"
        while node:
            "1 "
            "next = 2 > 3 > 4 > 5 > None"
            "node.next = None"
            "node = 1 > None"
            "2 "
            "next = 3 > 4 > 5 > None"
            "node = 2 > 1 > None"
            next, node.next = node.next, prev
            print(next.val)
            "1 "
            "prev = 1 > None"
            "node = 2 > 3 > 4 > 5 > None"
            "2 "
            "prev = 2 > 1 > None"
            "node = 3 > 4 > 5 > None"
            prev, node = node, next
        return prev


if __name__ == "__main__":
    node1_1 = ListNode(1)
    node1_2 = ListNode(2)
    node1_3 = ListNode(3)
    node1_4 = ListNode(4)
    node1_5 = ListNode(5)

    node1_1.next = node1_2
    node1_2.next = node1_3
    node1_3.next = node1_4
    node1_4.next = node1_5

    example = Solution()
    result_example = example.reverseList2(node1_1)
    print(result_example)
