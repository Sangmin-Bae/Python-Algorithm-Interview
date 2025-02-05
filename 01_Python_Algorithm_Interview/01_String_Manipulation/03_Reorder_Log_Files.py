'''
    [문제 설명]
        - 로그를 재정렬하라. 기준은 다음과 같다.
            1) 로그의 가장 앞 부분은 식별자다.
            2) 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
            3) 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
            4) 숫자 로그는 입력 순서대로 한다.

    [입출력 예제]
        - 입력
            - ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
        - 출력
            - ["let1 art can", "let3 art zoo", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
'''

from typing import List

class Solutions:
    # Solution 01
    def reorder_log_files(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            # 각 log의 식별자 뒤 첫번째 문자가 숫자인지 문자인지 구분
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # 2개의 키를 람다 표현식으로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits

if __name__ == "__main__":
    input_logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

    sol = Solutions()

    # Result
    print(f"Input Logs : {input_logs}")
    print(f"Output Logs : {sol.reorder_log_files(input_logs)}")
