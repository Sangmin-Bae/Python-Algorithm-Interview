'''
[문제 설명]
    - 문자열 str 과 정수 n 이 주어집니다.
    - str 이 n 번 반복된 문자열을 만들어 출력하는 코드를 작성해 보세요.

[제한사항]
    - 1 <= str 의 길이 <= 10
    - 1 <= n <= 5

[입출력 예제]
    - 입력
        - string 5
    - 출력
        - stringstringstringstringstring
'''

class Solutions:
    # Solution 01
    def string_repeat(self, s: str, n: int) -> str:
        # if 문 제약사항 조건
        if 1<= len(s) <= 10 and 1 <= n <= 5:
            # string * int 는 string을 int만큼 반복
            return s * n

if __name__ == "__main__":
    s, n = input().strip().split(' ')
    n = int(n)

    sol = Solutions()

    print(f"Solution 01 Output : {sol.string_repeat(s, n)}")