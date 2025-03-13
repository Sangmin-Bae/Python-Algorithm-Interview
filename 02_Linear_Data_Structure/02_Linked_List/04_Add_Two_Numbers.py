"""
[문제 설명]
    - 역순으로 저장된 연결 리스트의 숫자를 더하라.

[입출력 예제]
    - 입력
        - (2 -> 4 -> 3) + (5 -> 6 -> 4)
    - 출력
        - 7 -> 0 -> 8
    - 설명
        342 + 465 = 807
"""

from typing import List


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solutions:
    # Solution 01 - 자료형 변환
    # 연결 리스트 뒤집기
    def revers_list(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    # 연결 리스트를 파이썬 리스트로 변환
    def to_list(self, node: ListNode) -> ListNode:
        list: List = []

        while node:
            list.append(node.val)
            node = node.next

        return list

    # 파이썬 리스트를 연결 리스트로 변환
    def to_reversed_linked_list(self, result: List) -> ListNode:
        prev: ListNode = None

        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node

        return node

    # 두 연결 리스트의 덧셈
    def add_two_numbers_01(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.to_list(self.revers_list(l1))
        b = self.to_list(self.revers_list(l2))

        result_str = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))

        return self.to_reversed_linked_list(str(result_str))

    # Solution 02 - 전가산기 구현
    def add_two_numbers_02(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # 두 입력값의 합 계산
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            # 몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next


if __name__ == "__main__":
    head01 = ListNode(2)
    head01.next = ListNode(4)
    head01.next.next = ListNode(3)

    head02 = ListNode(5)
    head02.next = ListNode(6)
    head02.next.next = ListNode(4)

    sol = Solutions()

    # output01 = sol.add_two_numbers_01(head01, head02)
    # while output01:
    #     print(output01.val)
    #     output01 = output01.next

    output02 = sol.add_two_numbers_02(head01, head02)
    while output02:
        print(output02.val)
        output02 = output02.next