"""
[문제 설명]
    - 두 개의 문자열 str1, str2 가 공백으로 구분되어 입력으로 주어집니다.
    - 입출력 예와 같이 str1과 str2을 이어서 출력하는 코드를 작성해 보세요.

[제한사항]
    - 1 <= str1, str2 의 길이 <= 10

[입출력 예시]
    - 예시 #1
        - 입력
            - apple pen
        - 출력
            - applepen
    - 에시 #2
        - 입력
            - Hello world!
        - 출력
            - HelloWorld!
"""


if __name__ == "__main__":
    # Solution 01
    print(input().strip().replace(' ', ''))

    # Solution 02
    print(''.join(input().strip().split()))