from typing import List

from sortedcontainers import SortedDict
from collections import Counter

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        m, n = len(s), len(queryCharacters)
        spans, lengths = SortedDict(), SortedDict()

        idx = [i for i,(x,y) in enumerate(zip('_' + s, s + '_')) if x != y]
        print(idx)
        deg = Counter(y - x for x,y in zip(idx, idx[1:]))
        print(deg)



ss = Solution()
s = "babacc"
queryCharacters = "bcb"
queryIndices = [1,3,3]
print(ss.longestRepeating(s, queryCharacters, queryIndices))