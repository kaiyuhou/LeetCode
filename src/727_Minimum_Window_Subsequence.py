class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        ans = None
        right = 0
        while right < len(s1):
            i = 0
            while right < len(s1):
                if s1[right] == s2[i]:
                    i += 1
                    if i == len(s2):
                        break
                right += 1
            if right == len(s1):
                break
            i = len(s2) - 1
            left = right
            while i >= 0:
                if s1[left] == s2[i]:
                    i -= 1
                left -= 1
            left += 1
            cur_ans = s1[left:right + 1]
            if ans is None or len(cur_ans) < len(ans):
                ans = cur_ans
            right = left + 1
        return ans if ans is not None else ""
