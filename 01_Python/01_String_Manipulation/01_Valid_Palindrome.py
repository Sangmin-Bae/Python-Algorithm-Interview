'''
[문제 설명]
    - 주어진 문자열이 팰린드롬인지 확인하라.
    - 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

[입출력 예제]
    - 예제 1
        - 입력
            - "A man, a plan, a canal: Panama"
        - 출력
            - True

    - 예제 2
        - 입력
            - "race a car"
        - 출력
            - False
'''

import collections
import re
from typing import Deque


class Solutions:
    # Solution 01
    def is_palindrome_01(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True

    # Solution 02
    def is_palindrome_02(self, s:str) -> bool:
        # 자료형 데크로 선언
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True

    # Solution 03
    def is_palindrome_03(self, s:str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1] # 슬라이싱

if __name__ == "__main__":
    input_strs = ["A man, a plan, a canal: Panama", "race a car"]

    sol = Solutions()

    # Output Result Solution 01
    for idx, input_str in enumerate(input_strs):
        print(f"Output of Input 01 : {input_str}")
        print(f"Solution 01 Output : {sol.is_palindrome_01(input_str)}")
        print(f"Solution 02 Output : {sol.is_palindrome_02(input_str)}")
        print(f"Solution 03 Output : {sol.is_palindrome_03(input_str)}")
        print()



