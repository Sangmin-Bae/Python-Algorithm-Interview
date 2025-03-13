'''
[문제 설명]
    - 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
    - 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.

[입출력 예제]
    - 입력
        - paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
        - banned = ["hit"]
    - 출력
        - "ball"
'''

import collections
import re
from typing import List

class Solutions:
    # Solution 01 - defaultdict 사용
    def most_common_word_01(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'\W', ' ', paragraph).lower().split()
                if word not in banned]

        counts = collections.defaultdict(int)
        for word in words:
            counts[word] += 1

        return max(counts, key=counts.get)

    # Solution 02 - Counter 사용
    def most_common_word_02(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'\W', ' ', paragraph).lower().split()
                if word not in banned]

        counts = collections.Counter(words)

        return counts.most_common(1)[0][0]

if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    sol = Solutions()

    print(f"Paragraph : {paragraph}")
    print(f"Banned : {banned}")
    print(f"Solution 01 Output : {sol.most_common_word_01(paragraph, banned)}")
    print(f"Solution 02 Output : {sol.most_common_word_02(paragraph, banned)}")
