"""
[문제 설명]
    - 민수는 다양한 지폐를 수집하는 취미를 가지고 있습니다. 지폐마다 크기가 달라 지갑에 넣으려면 여러 번 접어서 넣어야
      합니다.
    - 예를 들어 지갑의 크기가 30 * 15이고 지폐의 크기가 26 * 17이라면 한번 반으로 접어 13 * 17 크기로 만든 뒤 90도
      돌려서 지갑에 넣을 수 있습니다.
    - 지폐를 접을 때는 다음과 같은 규칙을 지킵니다.
        - 지폐를 접을 때는 항상 길이가 긴 쪽을 반으로 접습니다.
        - 접기 전 길이가 홀수였다면 접은 후 소수점 이하는 버립니다.
        - 접힌 지폐를 그대로 또는 90도 돌려서 지갑에 넣을 수 있다면 그만 접습니다.
    - 지갑의 가로, 세로 크기를 담은 점수 리스트 wallet 과 지폐의 가로, 세로 크기를 담은 정수 리스트 bill 가 주어질 때,
      지갑에 넣기 위해서 지폐를 최소 몇 번 접어야 하는지 return 하도록 solution 함수를 완성해 주세요.
    - 지폐를 지갑에 넣기 위해 접어야 하는 최소 횟수를 구하는 과정은 다음과 같습니다.
        1) 지폐를 접은 횟수를 저장할 정수 변수 answer 를 만들고 0을 저장합니다.
        2) 반복문은 이용해 bill 의 작은 값이 wallet 의 작은 값 보다 크거나 bill 의 큰 값이 wallet의 큰 값보다 큰 동안
           아래 과정을 반복합니다.
            2-1) bill[0] 이 bill[1] 보다 크다면 bill[0]을 2로 나누고 나머지는 버립니다.
            2-2) 그렇지 않다면 bill[1]을 2로 나누고 나머지는 버립니다.
            2-3) answer 을 1 증가합니다.
        3) answer 을 return 합니다.
    - 위의 의사코드와 작동방식이 다른 코드를 작성해도 상관없습니다.

[제한 사항]
    - wallet 의 길이 = bill 의 길이 = 2
    - 10 <= wallet[0], wallet[1] <= 100
    - 10 <= bill[0], bill[1] <= 2,000

[입출력 예제]
    - 예제 #1
        - 입력
            - wallet = [30, 15] / bill = [26, 17]
        - 출력
            - 1
    - 예제 #2
        - 입력
            - wallet = [50, 50] / bill = [100, 241]
        - 출력
            - 4
"""

from typing import List


class Solutions:
    # Solution 01
    @staticmethod
    def solution01(wallet: List, bill: List) -> int:
        answer = 0
        wallet, bill = sorted(wallet), sorted(bill)

        while bill[0] > wallet[0] or bill[1] > wallet[1]:
            if bill[0] > bill[1]:
                bill[0] = bill[0] // 2
            else:
                bill[1] = bill[1] // 2

            answer += 1
            bill = sorted(bill)

        return answer


if __name__ == "__main__":
    sol = Solutions()

    input_list = [([30, 15], [26, 17]), ([50, 50], [100, 241])]

    for wallet_i, bill_i in input_list:
        print(wallet_i, bill_i)
        print(f"Solution 01 Output: {sol.solution01(wallet_i, bill_i)}")