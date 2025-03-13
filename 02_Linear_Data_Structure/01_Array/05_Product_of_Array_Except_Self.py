'''
[문제 설명]
    - 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.

[입출력 예제]
    - 입력
        - [1, 2, 3, 4]
    - 출력
        - [24, 12, 8, 6]
    - 주의
        - 나눗셈을 하지 않고 O(n)에 풀이하라.
'''

from typing import List

class Solutions:
    # Solution 01 - 왼쪽 곱셈 결과에 오른쪽 결과 값을 차례대로 곱셈
    def product_except_self_01(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        # 왼쪽 곱셈
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]

        p = 1
        # 오른쪽 곱셈
        for i in range(len(nums) - 1, -1, -1):
            out[i] = out[i] * p
            p = p * nums[i]

        return out

if __name__ == "__main__":
    nums = [1, 2, 3, 4]

    sol = Solutions()

    print(f"Solution 01 Output : {sol.product_except_self_01(nums)}")