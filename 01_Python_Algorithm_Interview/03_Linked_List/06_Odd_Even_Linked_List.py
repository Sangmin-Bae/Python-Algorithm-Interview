"""
[문제 설명]
    - 연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라.
    - 공간 복잡도 O(1), 시간 복잡도 O(n)에 풀이하라.

[입출력 예제]
    - 예제 #1
        - 입력
            - 1 -> 2 -> 3 -> 4 -> 5 -> NULL
        - 출력
            - 1 -> 3 -> 5 -> 2 -> 4 -> NULL
    - 예제 #2
        - 입력
            - 2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7 -> NULL
        - 출력
            - 2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4 -> NULL
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class Solutions:
    # Solution 01 - 반복 구조로 홀짝 노드 처리
    @staticmethod
    def odd_even_list01(head: ListNode) -> ListNode:
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head
        return head


if __name__ == "__main__":
    sol = Solutions()

    head01 = head = ListNode(None)
    list01 = [1, 2, 3, 4, 5]
    for i in list01:
        head.next = ListNode(i)
        head = head.next
    head01 = head01.next

    head02 = head = ListNode(None)
    list02 = [2, 1, 3, 5, 6, 4, 7]
    for i in list02:
        head.next = ListNode(i)
        head = head.next
    head02 = head02.next

    result_head01 = sol.odd_even_list01(head01)
    result_head02 = sol.odd_even_list01(head02)

    while result_head01:
        print(result_head01.val)
        result_head01 = result_head01.next

    while result_head02:
        print(result_head02.val)
        result_head02 = result_head02.next