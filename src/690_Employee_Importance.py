"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        e_map = {e.id: (e.importance, e.subordinates) for e in employees}

        def dfs(root):
            return e_map[root][0] + sum([dfs(id) for id in e_map[root][1]])

        return dfs(id)