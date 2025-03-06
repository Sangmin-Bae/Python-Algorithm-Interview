"""
[문제 설명]
    - 자연수 n 이 주어졌을 때 만약 n 이 짝수이면 "n is even"을 홀수이면 "n is odd"를 출력하는 코드를 작성해 보세요.

[제한 사항]
    - 1 <= n <= 1,000

[입출력 예시]
    - 예시 #1
        - 입력
            - 100
        - 출력
            - 100 is even
    - 예시 #2
        - 입력
            - 1
        - 출력
            - 1 is odd
"""


if __name__ == "__main__":
    # Solution 01
    a = int(input())
    print(f"{a} is even") if a % 2 == 0 else print(f"{a} is odd")

    # Solution 02
    a = int(input())
    print(f"{a} is {'even' if a % 2 == 0 else 'odd'}")

    # Solution 03
    a = int(input())
    print(f"{a} is {'eovdedn'[a&1::2]}")