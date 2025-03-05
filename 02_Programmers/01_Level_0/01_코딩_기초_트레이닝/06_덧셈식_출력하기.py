"""
[문제 설명]
    - 두 정수 a, b가 주어질 때 다음과 같은 형태의 계산식을 출력하는 코드를 작성해 보세요.
    - a + b = c

[제한 사항]
    - 1 <= a, b <= 100

[입출력 예제]
    - 입력
        - 4 5
    - 출력
        - 4 + 5 = 9
"""


class Solutions:
    # Solution 01
    @staticmethod
    def print_addition_formula(input_str):
        a, b = map(int, input_str.strip().split(' '))
        print(f"{a} + {b} = {a + b}")


if __name__ == "__main__":
    sol = Solutions()

    sol.print_addition_formula(input())