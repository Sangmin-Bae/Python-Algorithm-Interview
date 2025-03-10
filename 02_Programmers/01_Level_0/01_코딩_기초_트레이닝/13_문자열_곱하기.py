"""
[문제 설명]
    - 문자열 my_string 과 정수 k 가 주어질 때, my_string 을 k 번 반복한 문자열을 return 하는 solution 함수를 작성해
      주세요.

[제한사항]
    - 1 <= my_string 의 길이 <= 100
    - my_string 은 영소문자로만 이루어져 있습니다.
    - 1 <= k <= 100

[입출력 예제]
    - 예제 #1
        - 입력
            - my_string = "string" / k = 3
        - 출력
            - "stringstringstring"
    - 예제 #2
        - 입력
            - my_string = "love / k = 10
        - 출력
            - "lovelovelovelovelovelovelovelovelovelove"
"""


class Solutions:
    # Solution 01
    @staticmethod
    def solution01(my_string:str, k:int) -> str:
        return my_string * k


if __name__ == "__main__":
    sol = Solutions()

    intput_list = [("string", 3), ("love", 10)]

    for my_string, k in intput_list:
        print(f"Solution 01 Output: {sol.solution01(my_string, k)}")