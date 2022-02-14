class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        order = [i for i in range(len(indices))]
        order.sort(key=indices.__getitem__)

        ans = ''
        last_copy = 0
        for i in order:
            if sources[i] == s[indices[i]:indices[i] + len(sources[i])]:
                ans += s[last_copy:indices[i]]
                ans += targets[i]
                last_copy = indices[i] + len(sources[i])
        ans += s[last_copy:]
        return ans