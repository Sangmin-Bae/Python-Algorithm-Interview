"""
[문제 설명]
    - 정수 n 을 입력받아 n 의 약수를 모두 더한 값을 리턴하는 함수, solution 을 완성해주세요.

[제한 사항]
    - n 은 0 이상 3000 이하인 정수입니다.

[입출력 예제]
    - 예제 #1
        - 입력
            - n = 12
        - 출력
            - 28
    - 예제 #2
        - 입력
            - n = 5
        - 출력
            - n = 6
"""


class Solutions:
    # Solution 01
    @staticmethod
    def solution01(n):
        divisors = set()

        d = 1
        while d <= n:
            if n % d == 0:
                divisors.add(d)
                divisors.add(n / d)
                d += 1
            else:
                d += 1

        return int(sum(divisors))

    # Solution 03
    @staticmethod
    def solution02(n):
        answer = n

        d = 1
        while d <= n // 2:
            if n % d == 0:
                answer += d
                d += 1
            else:
                d += 1

        return answer

    # Solution 03 - compression
    @staticmethod
    def solution03(n):
        return n + sum([i for i in range(1, n//2 + 1) if n % i == 0])

    # Solution 04 - compression
    @staticmethod
    def solution04(n):
        return n + sum(filter(lambda x: n % x == 0, range(1, n//2 + 1)))

if __name__ == "__main__":
    nums = [12, 5]

    sol = Solutions()

    for num_i in nums:
        print(sol.solution01(num_i))
        print(sol.solution02(num_i))
        print(sol.solution03(num_i))
        print(sol.solution04(num_i))