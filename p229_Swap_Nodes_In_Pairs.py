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

"연결 리스트를 입력받아 페어Pair 단위로 스왑하라"


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def swapPairs1(self, head: ListNode) -> ListNode:
        cur = head

        while cur and cur.next:
            # 값만 교환
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        return head

    def swapPairs2(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            # b가 a(head)를 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head

            # prev가 b를 가리키도록 할당
            prev.next = b

            # 다음번 비교를 위해 이동
            head = head.next
            prev = prev.next.next
        return root.next

    def swapPairs3(self, head: ListNode) -> ListNode:
        # 페어가 존재 하지 않을 경우 head를 Return
        if head and head.next:
            p = head.next

            # 스왑된 값을 Return 받음
            head.next = self.swapPairs3(p.next)
            p.next = head
            return p
        return head


if __name__ == "__main__":
    node1_1 = ListNode(1)
    node1_2 = ListNode(2)
    node1_3 = ListNode(3)
    node1_4 = ListNode(4)

    node1_1.next = node1_2
    node1_2.next = node1_3
    node1_3.next = node1_4

    example = Solution()
    result_example = example.swapPairs3(node1_1)
    print(result_example)
    for x in range(4):
        print(result_example.val)
        result_example = result_example.next
