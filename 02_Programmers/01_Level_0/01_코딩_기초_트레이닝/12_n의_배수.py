"""
[문제 설명]
    - 정수 num 과 n 이 매개 변수로 주어질 때, num 이 n 의 배수이면 1을 return, n 의 배수가 아니라면 0을 return 하도록
      solution 함수를 완성해주세요.

[제한사항]
    - 2 <= num <- 100
    - 2 <= n <= 9

[입출력 예제]
    - 예제 #1
        - 입력
            - num = 98 / n = 2
        - 출력
            - 1
    - 예제 #2
        - 입력
            - num = 34 / n = 3
        - 출력
            - 0
"""


class Solutions:
    # Solution 01
    @staticmethod
    def solution01(num: int, n: int) -> int:
        return 0 if num % n else 1


if __name__ == "__main__":
    sol = Solutions()

    input_list = [(98, 2), (34, 3)]

    for num, n in input_list:
        print(f"Solution 01 Output : {sol.solution01(num, n)}")