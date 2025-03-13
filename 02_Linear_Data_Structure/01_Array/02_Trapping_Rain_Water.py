'''
[문제 설명]
    - 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓을 수 있는지 계산하라.

[입출력 예제]
    - 입력
        - [0,1,0,2,1,0,1,3,2,1,2,1]
    - 출력
        - 6
'''

from typing import List

class Solutions:
    # Solution 00 - Brute Force
    def trap_00(self, height: List[int]) -> int:
        trapped = 0
        # height의 양 끝을 제외한 범위 index loop로 훑기
        # 양 끝은 좌, 우 높이가 없기 때문
        for i in range(1, len(height) - 1):
            left_height = 0
            right_height = 0

            # 현재 index 기준 좌측 장벽 높이 찾기
            for j in range(i, -1, -1):
                left_height = max(left_height, height[j])

            # 현재 index 기준 우측 장벽 높이 찾기
            for k in range(i, len(height)):
                right_height = max(right_height, height[k])

            # 좌, 우 장벽 높이 중 최소값과 현재 위치 높이를 뺀 해당 위치에서 빗물이 고일 수 있는 웅덩이의 넓이 계산
            # 현재 위치의 높이와 좌, 우측 장벽 높이가 같거나 낮다면 해당 위치는 웅덩이가 생길 수 없음
            trapped += min(left_height, right_height) - height[i]

        return trapped

    # Solution 01 - 투 포인터를 최대로 이동
    def trap_01(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)

            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume

    # Solution 02 - 스택 쌓기
    def trap_02(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼낸다
                top = stack.pop()

                if not len(stack):
                    break

                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters

            stack.append(i)

        return volume

if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]

    sol = Solutions()

    print(f"Solution 00 Output : {sol.trap_00(height)}")
    print(f"Solution 01 Output : {sol.trap_01(height)}")
    print(f"Solution 02 Output : {sol.trap_02(height)}")