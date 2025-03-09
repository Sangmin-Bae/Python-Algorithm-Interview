"""
[문제 설명]
    - 양의 정수 n 이 매개변수로 주어집니다.
    - n x n 배열에 1부터 n^2 까지 정수를 인덱스 [0][0] 부터 시계 방향 나선형으로 배치한 이차원 배열을 return 하는
      solution 함수를 작성해 주세요.
"""

class Solutions:
    # Solution 01
    @staticmethod
    def solution01(n):
        if n == 1:
            return [[1]]

        answer = [[0 for _ in range(n)] for _ in range(n)]

        direction = "right"
        row, column = 0, 0
        for i in range(1, n**2 + 1):
            answer[row][column] = i
            if direction == "right":
                column += 1
                if column == n - 1 or answer[row][column + 1] != 0:
                    direction = "down"
            elif direction == "down":
                row += 1
                if row == n - 1 or answer[row + 1][column] != 0:
                    direction = "left"
            elif direction == "left":
                column -= 1
                if column == 0 or answer[row][column - 1] != 0:
                    direction = "up"
            elif direction == "up":
                row -= 1
                if row == 0 or answer[row - 1][column] != 0:
                    direction = "right"

        return answer

    # Solution 02
    @staticmethod
    def solution02(n):
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]
        y, x = 0, -1

        arr = [[0] * n for _ in range(n)]
        cnt = 1
        direction = 0
        while cnt <= n ** 2:
            ny, nx = y + dy[direction], x + dx[direction]
            if 0 <= ny < n and 0 <= nx < n and not arr[ny][nx]:
                arr[ny][nx] = cnt
                cnt += 1
                y, x = ny, nx
            else:
                direction = (direction + 1) % 4

        return arr


if __name__ == "__main__":
    sol = Solutions()

    nums = [1, 4, 5]

    for num in nums:
        print(sol.solution01(num))
        print(sol.solution02(num))