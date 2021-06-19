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
    def isPalindrome1(self, head: ListNode) -> bool:
        q: List = []

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        # pop으로 에러가 발생하지 않게 하기 위해 len(q) > 1 를 사용
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        return True

    # O(1)의 속도로 시작과 끝을 가지고 올 수 있는 Deque를 사용
    def isPalindrome2(self, head: ListNode) -> bool:
        q: Deque = collections.deque()

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        # pop으로 에러가 발생하지 않게 하기 위해 len(q) > 1 를 사용
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True

    def isPalindrome3(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head

        # Runner를 이용해 역순 연결 리스트 구성
        # 현재 fast와 fast.next가 None이 아닐때
        # 즉 List의 50%를 자르기 위하여 fast함수 사용
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

            "1. rev = (1) > (None) / (1) = rev.next / (None) = 이전 rev"
            "2. rev = (2) > (1 > None) / (2) = rev.next / (1 > None) = 이전 rev"
            "3. rev = (3) > (2 > 1 > None) / (3) = rev.next / (2 > 1 > None) = 이전 rev"
            "loop End"
            print(rev.val)

        # 1,2,2,1
        # rev의 값이 역순으로 저장된다.
        print("val : ", rev.val)
        print("val : ", rev.next.val)
        # fast.next가 None이고 fast는 None이 아닐때 / 즉 홀수의 List구조일 때
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        # rev는 시작부터 50%까지 저장되어 있고 역순으로 검색
        # slow는 50% 부터 끝까지 순서대로 검색
        while rev and rev.val == slow.val:
            "rev = 3 > 2 > 1 > None : fast pointer를 이용하여 저장한 데이터"
            "slow = 3 > 2 > None : fast Pointer 종료 후 추가 탐색하는 데이터"
            print(rev.val)
            slow, rev = slow.next, rev.next

        # not None = True, not ListNode = False
        return not rev


if __name__ == "__main__":
    example = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(3)
    node5 = ListNode(2)
    node6 = ListNode(1)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    # node5.next = node6

    # result_example = example.isPalindrome1(node1)
    result_example = example.isPalindrome3(node1)
    print(result_example)

"""
rev = 1, slow = 2->3 , slow.next = 3


rev, rev.next, slow = slow, rev, slow.next
rev = 2->3 
rev.next = 1
slow = 3

rev.next = 1이므로 최종적으로 rev = 2->1, slow = 3이 된다.
다중 할당을 하게되면 이 작업이 동시에 일어나기 때문에 모든 작업은 중간과정 없이 한 번의 트랜잭션으로 끝나게 된다.

rev, rev.next = slow, rev
slow = slow.next
rev = 2->3
rev.next = 1 

따라서 rev = 2->1이 되는데
여기서 중요한 점은 rev = slow라는 점이다.
즉 동일한 참조가 되었으며 rev = 2->1이 되었기 때문에
slow = 2->1도 함께 되어 버린다.
따라서 이후에 slow = slow.next의 결과는
slow = 1이 된다.
결국, 최종 결과는 rev = 2->1, slow = 1로, 앞서 다중 할당으로 한 번에 처리한 것과 다른 결과가 된다.
반드시 한 줄의 다중할당으로 한 번에 처리해야 문제를 제대로 풀이 할 수 있다.
"""
