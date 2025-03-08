"""
[문제 설명]
    - 두 문자열 s 와 skip, 그리고 자연수 index 가 주어질 때, 다음 규칙에 따라 문자열을 만들려 합니다.
    - 암호의 규칙은 다음과 같습니다.
        - 문자열 s 의 각 알파벳을 index 만큼 뒤의 알파벳으로 바꿔줍니다.
        - index 만큼의 뒤의 알파벳이 z 를 넘어갈 경우 다시 a 로 돌아갑니다.
        - skip 에 있는 알파벳은 제외하고 건너뜁니다.
    - 예를 들어 s = "aukks", skip = "wbpd", index = 5 일때, a 에서 5만큼 뒤에 있는 알파벳은 f 지만 [b, c, d, e, f] 에서
      'b' 와 'd' 는 skip 에 포함되므로 세지 않습니다.
    - 따라서 'b' 와 'd' 를 제외하고 'a' 에서 5만큼 뒤에 있는 알파벳은 [c, e, f, g, h] 순서에 의해 'h' 가 됩니다.
    - 나머지 "uuks" 또한 위 규칙대로 바꾸면 "appy"가 되며 결과는 "happy" 가 됩니다.
    - 두 문자열 s 와 skip, 그리고 자연수 index 가 매개변수로 주어질 때 위 규칙대로 s 를 변환한 결과를 return 하도록
      solution 함수를 완성해주세요.

[제한사항]
    - 5 <= s 의 길이 <= 50
    - 1 <= skip 의 길이 <= 10
    - s 와 skip 은 알파벳 소문자로만 이루어져 있습니다.
        - skip 에 포함되는 알파벳은 s 에 포함되지 않습니다.
    - 1 <= index <= 20

[입출력 예]
    - 입력
        - s = "aukks" / skip = "wbqd" / index = 5
    - 출력
        - "happy"
"""


class Solutions:
    # Solution 01
    @staticmethod
    def solution(s, skip, index):
        answer = ""

        allowed_alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) not in skip]
        print(allowed_alphabets)

        for s_i in s:
            current_idx = allowed_alphabets.index(s_i)
            new_idx = (current_idx + index) % len(allowed_alphabets)
            answer += allowed_alphabets[new_idx]

        return answer



if __name__ == "__main__":
    s = "aukks"
    skip = "wbqd"
    index = 5

    sol = Solutions()

    print(sol.solution(s, skip, index))

