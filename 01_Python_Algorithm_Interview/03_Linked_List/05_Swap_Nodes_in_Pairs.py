"""
[문제 설명]
    - 연결 리스트를 입력받아 페어(pair) 단위로 스왑하라.

[입출력 예제]
    - 입력
        - 1 -> 2 -> 3 -> 4
    - 출력
        - 2 -> 1 -> 4 -> 3
"""

from copy import deepcopy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solutions:
    # Solution 01 - 값만 교환
    @staticmethod
    def swap_pairs01(head: ListNode) -> ListNode:
        cur = head

        while cur and cur.next:
            # 값만 교환
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next

        return head

    # Solution 02 - 반복 구조로 스왑
    @staticmethod
    def swap_pairs02(head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            # b 가 a(head) 를 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head

            # prev 가 b 를 가리키도록 할당
            prev.next = b

            # 다음번 비교를 위해 이동
            head = head.next
            prev = prev.next.next
        return root.next

    # Solution 03 - 재귀 구조로 스왑
    def swap_pairs03(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            # 스왑된 값 리턴 받음
            head.next = self.swap_pairs03(p.next)
            p.next = head
            return p
        return head


if __name__ == "__main__":
    sol = Solutions()

    h = ListNode(1)
    h.next = ListNode(2)
    h.next.next = ListNode(3)
    h.next.next.next = ListNode(4)

    h_01 = sol.swap_pairs01(deepcopy(h))
    h_02 = sol.swap_pairs02(deepcopy(h))

    while h_01:
        print(h_01.val)
        h_01 = h_01.next

    while h_02:
        print(h_02.val)
        h_02 = h_02.next