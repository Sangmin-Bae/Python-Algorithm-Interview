"""
[문제 설명]
    - 문자열 s 가 입력되었을 때 다음 규칙을 따라서 이 문자열을 여러 문자열로 분해하려고 합니다.
        - 먼저 첫 글자를 읽습니다. 이 글자를 x 라고 합시다.
        - 이제 이 문자열을 왼쪽에서 오른쪽으로 읽어나가면서, x 와 x 가 아닌 다른 글자들이 나온 횟수를 각각 셉니다.
          처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리합니다.
        - s 에서 분리한 문자열을 빼고 남은 부분에 대해서 이 과정을 반복합니다. 남은 부분이 없다면 종료합니다.
        - 만약 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없다면, 역시 지금까지 읽은 문자열을 분리하고, 종료합니다.
    - 문자열 s 가 매개변수로 주어질 때, 위 과정과 같이 문자열들로 분해하고, 분해한 문자열의 개수를 return 하는 함수
      solution 을 완성하세요.

[제한사항]
    - 1 <= s 의 길이 <= 10,000
    - s 는 영어 소문자로만 이루어져 있습니다.

[입출력 예제]
    - 예제 #1
        - 입력
            - "banana"
        - 출력
            - 3
    - 예제 #2
        - 입력
            - "abracadabra"
        - 출력
            - 6
    - 예제 #1
        - 입력
            - "aaabbaccccabba"
        - 출력
            - 3
"""

class Solutions:
    # Solution 01
    @staticmethod
    def solution01(s):
        answer = 0

        x = s[0]
        equal_x_cnt = no_equal_x_cnt = 0
        for i in range(len(s)):
            if (i > 0) and (equal_x_cnt == no_equal_x_cnt):
                answer += 1
                x = s[i]
                equal_x_cnt = no_equal_x_cnt = 0

            if x == s[i]:
                equal_x_cnt += 1
            else:
                no_equal_x_cnt += 1

        return answer + 1


if __name__ == "__main__":
    s_list = ["banana", "abracadabra", "aaabbaccccabba"]

    sol = Solutions()

    for s_i in s_list:
        print(sol.solution(s_i))