"""
[문제 설명]
    - 문자열 my_string, overwrite_string 과 정수 s 가 주어집니다.
    - 문자열 my_string 의 인덱스 s 부터 overwrite_string 의 길이만큼을 문자열 overwrite_string으로 바군 문자열을
      return 하는 solution 함수를 작성해 주세요.

[제한 사항]
    - my_string 와 overwrite_string 은 숫자와 알파벳으로 이루어져 있습니다.
    - 1 <= overwrite_string 의 길이 <= my_string 의 길이 <= 1,000
    - 0 <= s <= my_string 의 길이 - overwrite_string 의 길이

[입출력 예시]
    - 예시 #1
        - 입력
            - my_string="He11loWor1d" / overwrite_string="lloWorl" / s=2
        - 출력
            - "HelloWorld"
    - 예시 #2
        - 입력
            - my_string="Program29b8UYP" / overwrite_string="merS123" / s=7
        - 출력
            - "ProgrammerS123"
"""

class Solutions:
    # Solution 01
    @staticmethod
    def solution01(my_string, overwrite_string, s):
        return my_string.replace(my_string[s: s + len(overwrite_string) + 1], overwrite_string)

    # Solution 02
    @staticmethod
    def solution02(my_string, overwrite_string, s):
        return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]


if __name__ == "__main__":
    strings = ["He11loWor1d", "Program29b8UYP"]
    overwrite_strings = ["lloWorl", "merS123"]
    ss = [2, 7]

    sol = Solutions()

    for string_i, overwrite_string_i, s_i in zip(strings, overwrite_strings, ss):
        print(sol.solution01(string_i, overwrite_string_i, s_i))
        print(sol.solution02(string_i, overwrite_string_i, s_i))