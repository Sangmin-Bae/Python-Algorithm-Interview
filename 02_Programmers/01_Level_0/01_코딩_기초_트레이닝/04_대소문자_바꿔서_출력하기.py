"""
[문제 설명]
    - 영어 알파벳으로 이루어진 문자열 str 이 주어집니다.
    - 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.

[제한 사항]
    - 1 <= str의 길이 <= 20
    - str 은 알파벳으로 이루어진 문자열입니다.

[입출력 예제]
    - 입력
        - aBcDeFg
    - 출력
        - AbCdEfG
"""

class Solutions:
    # Solution 01
    @staticmethod
    def conversion_case(string):
        result = ""
        for c in string:
            result += c.lower() if c.isupper() else c.upper()

        return result


if __name__ == "__main__":
    str = input()

    sol = Solutions()

    print(f"Solution 01 Output: {sol.conversion_case(str)}")