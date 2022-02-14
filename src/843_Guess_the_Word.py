from typing import *

class Master:
    def guess(self, word: str) -> int:
        ...

from collections import defaultdict

class Solution:
    def findSecretWord(self, ws: List[str], master: 'Master') -> None:
        n = len(ws)
        neighbor_map = defaultdict(list)

        def match_cnt(a, b):
            return sum(i == j for i, j in zip(a, b))

        for i in range(n - 1):
            for j in range(i + 1, n):
                mc = match_cnt(ws[i], ws[j])

                neighbor_map[(ws[i], mc)].append(ws[j])
                neighbor_map[(ws[j], mc)].append(ws[i])


        potential = set(ws)
        for _ in range(10):
            if len(potential) == 0:
                break

            best_guess = None
            best_entropy = None
            for w in potential:
                entropy = sum([len(neighbor_map[(w, i)]) ** 2 for i in range(7)])
                if best_entropy is None or entropy < best_entropy:
                    best_entropy = entropy
                    best_guess = w

            rnt = master.guess(best_guess)
            next_potential = set(neighbor_map[(best_guess, rnt)])

            potential = potential & next_potential









































