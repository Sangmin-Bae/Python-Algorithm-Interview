"""
[문제 설명]
    - 인덱스 m 에서 n 까지를 역순으로 만들어라. 인덱스 m 은 1부터 시작한다.

[입출력 예제]
    - 입력
        - 1->2->3->4->5->NULL, m = 2, n = 4
    - 출력
        - 1->4->3->2->5->NULL
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


class Solutions:
    # Solution 01 - 반복 구조로 노드 뒤집기
    @staticmethod
    def reverse_between(head: ListNode, m: int, n: int) -> ListNode:
        # 예외 처리
        if not head or m == n:
            return head

        root = start = ListNode(None)
        root.next = head
        # start, next 지정
        for _ in range(m - 1):
            start = start.next
        end = start.next

        # 반복하면서 노드 차례대로 뒤집기
        for _ in range(n - m):
            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp
        return root.next


if __name__ == "__main__":
    sol = Solutions()

    root = h = ListNode(1)
    m = 2
    n = 4
    for i in [2, 3, 4, 5, None]:
        h.next = ListNode(i)
        h = h.next

    # while True:
    #     print(root.val)
    #
    #     if root.next is None:
    #         break
    #
    #     root = root.next

    _head = sol.reverse_between(root, m, n)
    while True:
        print(_head.val)

        if _head.next is None:
            break

        _head = _head.next
