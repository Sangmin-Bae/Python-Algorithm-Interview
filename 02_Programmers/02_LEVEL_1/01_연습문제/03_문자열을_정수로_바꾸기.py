"""
[문제 설명]
    - 문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution 을 완성하세요.

[제한 조건]
    - s 의 길이는 1 이상 5 이하입니다.
    - s 의 맨앞에는 부호(+, -)가 올 수 있습니다.
    - s 는 부호와 숫자로만 이루어져 있습니다.
    - s 는 "0" 으로 시작하지 않습니다.
"""


class Solutions:
    # Solution 01
    @staticmethod
    def solution01(s):
        answer = 0

        if s.startswith('-'):
            answer = -1 * int(s[1:])
        else:
            answer = int(s) if not s.startswith('+') else int(s[1:])

        return answer

    # Solution 02
    @staticmethod
    def solution02(s):
        return int(s)


if __name__ == "__main__":
    str_list = ["1234", "-1234"]

    sol = Solutions()

    for str_i in str_list:
        print(sol.solution01(str_i))
        print(sol.solution02(str_i))