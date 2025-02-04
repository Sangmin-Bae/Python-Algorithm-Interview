"""
[문제 설명]
    - 정수 a와 b가 주어집니다. 각 수를 입력받아 입출력 예와 같은 형식으로 출력하는 코드를 작성해 보세요.

[제한 사항]
    - -100,000 ≤ a, b ≤ 100,000

[입출력 예]
    - 입력 #1
        - 4 5
    - 출력 #1
        -
            a = 4
            a = 5
"""

# Solution 01
a, b = map(int, input().strip().split(' '))
print(f"a = {a}\nb = {b}")

# Solution 02
while True:
    a, b = map(int, input().strip().split(' '))
    if -100000 <= a <= 100000 and -100000 <= b <= 100000:
        print(f"a = {a}\nb = {b}")
        break
    else:
        print("-100,000 ≤ a, b ≤ 100,000")
        continue