"""
[문제 설명]
    - 문자열 str 이 주어집니다.
    - 문자열을 시계방향으로 90도 돌려서 아래 입출력 예와 같이 출력하는 코드를 작성해 보세요.

[제한사항]
    - 1 <= str 의 길이 <= 10

[입출력 예시]
    - 입력
        - abcde
    - 출력
        -
            a
            b
            c
            d
            e
"""


if __name__ == "__main__":
    # Solution 01
    for i in input():
        print(i)

    # Solution 02
    print("\n".join(input()))

    # Solution 03
    print(*list(map(str, input())), sep="\n")