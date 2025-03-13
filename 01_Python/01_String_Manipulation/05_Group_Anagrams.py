'''
[문제 설명]
    - 문자열 배열을 받아 애너그램 단위로 그룹핑하라.

[입출력 예제]
    - 입력
        - ["eat", "tea", "tan", "ate", "nat", "bat"]
    - 출력
        - [
        -   ["ate", "eat", "tea"],
        -   ["nat", "tan"]
        -   ["bat"]
        - ]
'''

import collections
from typing import List

class Solutions:
    # Solution 01
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)

        return anagrams.values()
    pass

if __name__ == "__main__":
    input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]

    sol = Solutions()

    print(f"Input : {input_list}")
    print(f"Output : {sol.group_anagrams(input_list)}")