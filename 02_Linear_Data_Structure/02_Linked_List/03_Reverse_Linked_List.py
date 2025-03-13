"""
[문제 설명]
    - 연결 리스트를 뒤집어라.

[입출력 예제]
    - 입력
        - 1->2->3->4->5->NULL
    - 출력
        - 5->4->3->2->1->NULL
"""


class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.nxt = nxt


class Solutions:
    # Solution 01 - 재귀 구조로 뒤집기
    def reverseList01(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            nxt, node.nxt = node.nxt, prev
            return reverse(nxt, node)
        return reverse(head)

    # Solution 02 - 반복 구조로 뒤집기
    def reverseList02(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            nxt, node.nxt = node.nxt, prev
            prev, node = node, nxt

        return prev


if __name__ == "__main__":
    head = ListNode(1)
    head.nxt = ListNode(2)
    head.nxt.nxt = ListNode(3)
    head.nxt.nxt.nxt = ListNode(4)
    head.nxt.nxt.nxt.nxt = ListNode(5)
    head.nxt.nxt.nxt.nxt.nxt = ListNode(None)

    sol = Solutions()

    # reversed_head = sol.reverseList01(head)
    reversed_head = sol.reverseList02(head)

    while True:
        print(reversed_head.val)
        if reversed_head.nxt is None:
            break
        reversed_head = reversed_head.nxt