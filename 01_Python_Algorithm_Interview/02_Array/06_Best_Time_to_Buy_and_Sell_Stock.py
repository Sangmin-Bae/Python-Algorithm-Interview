'''
[문제 설명]
    - 한 번의 거래로 낼 수 있는 최대 이익을 산출하라.

[입출력 예제]
    - 입력
        - [7, 1, 5, 3, 6, 4]
    - 출력
        - 5
    - 설명
        - 1일 때 사서 6일 때 팔면 5의 이익을 얻는다.
'''

import sys
from typing import List

class Solutions:
    # Solution 01 - 브루트 포스(Brute Force)로 계산
    def max_profit_01(self, prices: List[int]) -> int:
        max_price = 0

        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - price, max_price)

        return max_price

    # Solution 02 - 저점과 현재 값과의 차이 계산
    def max_profit_02(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]

    sol = Solutions()

    print(f"Solution 01 Output : {sol.max_profit_01(prices)}")
    print(f"Solution 02 Output : {sol.max_profit_02(prices)}")