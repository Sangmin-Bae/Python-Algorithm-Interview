"""
[문제 설명]
    - 연산 ⊕ 는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.
        - 12 ⊕ 3 = 123
        - 3 ⊕ 12 = 312
    - 양의 정수 a 와 b 가 주어졌을 때, a ⊕ b 와 2 * a * b 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.
    - 단, a ⊕ b 와 2 * a * b 가 같으면 a ⊕ b 를 return 합니다.

[제한사항]
    - 1 <= a, b < 10,000

[입출력 예제]
    - 예제 #1
        - 입력
            - a = 2 / b = 91
        - 출력
            - 364
    - 예제 #2
        - 입력
            - a = 91 / b = 2
        - 출력
            - 912
"""


class Solutions:
    # Solution 01
    @staticmethod
    def solution01(a: int, b: int) -> int:
        return max(2 * a * b, int(''.join([str(a), str(b)])))

    # Solution 02
    @staticmethod
    def solution02(a: int, b: int) -> int:
        concat = int(str(a) + str(b))
        mul = 2 * a * b

        if concat > mul:
            return concat
        elif concat < mul:
            return mul
        else:
            return concat


if __name__ == "__main__":
    sol = Solutions()

    input_list = [(2, 91), (91, 2)]

    for a, b in input_list:
        print(f"Solution 01 Output: {sol.solution01(a, b)}")
        print(f"Solution 02 Output: {sol.solution02(a, b)}")

