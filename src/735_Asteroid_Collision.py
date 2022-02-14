class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                top = stack.pop()
                if a + top > 0:
                    a = top
                elif a + top == 0:
                    a = 0
            if a != 0:
                stack.append(a)
        return stack