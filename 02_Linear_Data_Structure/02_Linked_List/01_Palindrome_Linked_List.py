'''
[문제 설명]
    - 연결 리스트가 팰린드롬 구조인지 판별하라

[입출력 예제]
    - 예제 1
        - 입력
            - 1->2
        - 출력
            - false

    - 예제 2
        - 입력
            - 1->2->2->1
        - 출력
            - true
'''

from typing import List, Deque
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solutions:
    # Solution 01 - 리스트 변환
    def is_palindrome01(self, head: ListNode) -> bool:
        q: List = []

        if not head:
            return True

        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True

    # Solution 02 - 데크를 이용한 최적화
    def is_palindrome02(self, head: ListNode) -> bool:
        # 데크 자료형 선언
        q: Deque = deque()

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

    # Solution 03 - 런너를 이용한 우아한 풀이
    def is_palindrome03(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev


if __name__ == "__main__":
    sol = Solutions()

    head01 = ListNode(1)
    head01.next = ListNode(2)

    print(f"head = [1, 2]")
    print(f"Solution 01 output: {sol.is_palindrome01(head01)}")
    print(f"Solution 02 output: {sol.is_palindrome02(head01)}")
    print(f"Solution 03 output: {sol.is_palindrome03(head01)}")

    head02 = ListNode(1)
    head02.next = ListNode(2)
    head02.next.next = ListNode(2)
    head02.next.next.next = ListNode(1)

    print(f"head = [1, 2, 2, 1]")
    print(f"Solution 01 output: {sol.is_palindrome01(head02)}")
    print(f"Solution 02 output: {sol.is_palindrome02(head02)}")
    print(f"Solution 03 output: {sol.is_palindrome03(head02)}")