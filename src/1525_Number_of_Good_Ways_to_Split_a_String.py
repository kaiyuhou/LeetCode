from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        left_set = set()
        counter = Counter(s)
        right_cnt = len(counter.keys())
        ans = 0
        for c in s:
            left_set.add(c)
            counter[c] -= 1
            if counter[c] == 0:
                right_cnt -= 1

            if len(left_set) == right_cnt:
                ans += 1

            if len(left_set) > right_cnt:
                break
        return ans
