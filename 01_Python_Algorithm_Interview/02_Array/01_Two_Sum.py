'''
[문제 설명]
    - 덧셈하여 타켓을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

[입출력 예제]
    - 입력
        - nums = [2, 7, 11, 15], target = 9
    - 출력
        - [0, 1]
    - 설명
        - nums[0] + nums[1] = 2 + 7 = 9
        - 따라서 0, 1을 리턴한다.
'''

from typing import List

class Solutions:
    # Solution 01 - Brute-Force(무차별 대입)
    def two_sum_01(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # Solution 02 - in을 이용한 탐색
    def two_sum_02(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i + 1:]:
                return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

    # Solution 03 - 첫 번째 수를 뺀 결과 키 조회
    def two_sum_03(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [nums.index(num), nums_map[target - num]]

    # Solution 04 - 조회 구조 개선
    def two_sum_04(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 하나의 for 문으로 통합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    sol = Solutions()

    print(f"Solution 01 Output: {sol.two_sum_01(nums, target)}")
    print(f"Solution 02 Output: {sol.two_sum_02(nums, target)}")
    print(f"Solution 03 Output: {sol.two_sum_03(nums, target)}")
    print(f"Solution 04 Output: {sol.two_sum_04(nums, target)}")