'''
[문제 설명]
    - 문자열을 뒤집는 함수를 작성하라.
    - 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.

[입출력 예제]
    - 예제 1
        - 입력
            - ["h", "e", "l", "l", "o"]
        - 출력
            - ["o", "l", "l", "e", "h"]

    - 예제 2
        - 입력
            - ["H", "a", "n", "n", "a", "h"]
        - 출력
            - ["h", "a", "n", "n", "a", "H"]
'''

import copy
from typing import List

class Solutions:
    # Solution 01 - two pointer swapping
    def reverse_string_01(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1 # list index min, max
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    # Solution 02 - pythonic way
    def reverse_string_02(self, s: List[str]) -> None:
        s.reverse()

if __name__ == "__main__":
    input_lists = [["h", "e", "l", "l", "o"], ["H", "a", "n", "n", "a", "h"]]

    sol = Solutions()

    for i in range(len(input_lists)):
        print(f"Output of Input {i:02d} : {input_lists[i]}")
        input_list = copy.deepcopy(input_lists[i])
        sol.reverse_string_01(input_list)
        print(f"Solution 01 Output : {input_list}")
        input_list = copy.deepcopy(input_lists[i])
        sol.reverse_string_02(input_list)
        print(f"Solution 02 Output : {input_list}")
        print()