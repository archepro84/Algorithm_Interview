import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *
from typing import List
from operator import add, mul


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 연결 리스트 뒤집기
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    # 연결 리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    # 파이썬 리스트를 연결 리스트로 변환
    def toReversedLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node

        return node

    # 두 연결 리스트의 덧셈
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        # 1
        resultStr = int(''.join(str(e) for e in a)) + \
                    int(''.join(str(e) for e in b))

        # 2
        resultStr = int(''.join(map(str, a))) + \
                    int(''.join(map(str, b)))

        # 3
        resultStr = functools.reduce(lambda x, y: 10 * x + y, a, 0) + \
                    functools.reduce(lambda x, y: 10 * x + y, b, 0)


        # 최종 계산 결과 연결 리스트 변환
        return self.toReversedLinkedList(str(resultStr))

    # 전가산기 구현
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        "1. head : 0 > None"
        "2. head : 7 > None"
        '3. head : 7 > 0 > None / carry : 1'
        "4. head : 7 > 0 > 8 > None / carry : 0"
        while l1 or l2 or carry:
            sum = 0
            # 두 입력값의 합 계산
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            # 몫 (자리올림수)과 나머지(값) 계산
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next
        return root.next


if __name__ == "__main__":
    node1_1 = ListNode(2)
    node1_2 = ListNode(4)
    node1_3 = ListNode(3)

    node2_1 = ListNode(5)
    node2_2 = ListNode(6)
    node2_3 = ListNode(4)

    node1_1.next = node1_2
    node1_2.next = node1_3

    node2_1.next = node2_2
    node2_2.next = node2_3

    example = Solution()
    result_example = example.addTwoNumbers(node1_1, node2_1)
    print(result_example)
    for x in range(3):
        print(result_example.val)
        result_example = result_example.next
