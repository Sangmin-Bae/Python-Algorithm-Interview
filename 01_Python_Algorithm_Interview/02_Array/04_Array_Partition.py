'''
[문제 설명]
    - n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.

[입출력 예제]
    - 입력
        - [1, 4, 3, 2]
    - 출력
        - 4
    - 설명
        - n은 2가 되며, 최대 합은 4이다.
        - min(1, 2) + min(3, 4) = 4
'''

from typing import List

class Solutions:
    # Solution 01 - 오름차순 풀이
    def array_pair_sum_01(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum

    # Solution 02 - 짝수 번째 값 계산
    def array_pair_sum_02(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()

        for i, n in enumerate(nums):
            # 짝수 번째 값의 합 계산
            if i % 2 == 0:
                sum += n

        return sum

    # Solution 03 - 파이썬다운 방식(Pythonic Way)
    def array_pair_sum_03(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

if __name__ == "__main__":
    nums = [1, 4, 3, 2]

    sol = Solutions()

    print(f"Solution 01 Output : {sol.array_pair_sum_01(nums)}")
    print(f"Solution 02 Output : {sol.array_pair_sum_02(nums)}")
    print(f"Solution 03 Output : {sol.array_pair_sum_03(nums)}")
