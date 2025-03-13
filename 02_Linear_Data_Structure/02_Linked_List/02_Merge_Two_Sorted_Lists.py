"""
[문제 설명]
    - 정렬되어 있는 두 연결 리스트를 합쳐라.

[입출력 예제]
    - 입력
        - 1->2->4, 1->3->4
    - 출력
        - 1->1->2->3->4->4
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solutions:
    # Solution 01 - 재귀 구조로 연결
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1


if __name__ == "__main__":
    list_node1 = ListNode(1)
    list_node1.next = ListNode(2)
    list_node1.next.next = ListNode(4)

    list_node2 = ListNode(1)
    list_node2.next = ListNode(3)
    list_node2.next.next = ListNode(4)

    sol = Solutions()

    merged_list_node = sol.mergeTwoLists(list_node1, list_node2)
    while True:
        print(merged_list_node.val)
        if merged_list_node.next is None:
            break
        merged_list_node = merged_list_node.next