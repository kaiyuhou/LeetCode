class Solution:
    def calculate(self, s: str) -> int:
        num_stack = []
        op_stack = []
        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: b - a,
            '*': lambda a, b: a * b,
            '/': lambda a, b: -1 * (abs(b) // abs(a)) if (a * b < 0) else abs(b) // abs(a)
        }
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = int(c)
                while i < len(s) - 1 and s[i + 1].isdigit():
                    num = num * 10 + int(s[i + 1])
                    i += 1
                num_stack.append(num)
            elif c == "(":
                op_stack.append(c)
            elif c == ')':
                while op_stack[-1] != '(':
                    num_stack.append(ops[op_stack.pop()](num_stack.pop(), num_stack.pop()))
                op_stack.pop()
            else:  # c in +, -, *, //
                while len(op_stack) != 0 and not(op_stack[-1] in ('+', '-') and c in ('*', '/')) and op_stack[-1] != '(':
                    num_stack.append(ops[op_stack.pop()](num_stack.pop(), num_stack.pop()))
                op_stack.append(c)
            i += 1
        while len(op_stack) > 0:
            num_stack.append(ops[op_stack.pop()](num_stack.pop(), num_stack.pop()))

        return num_stack.pop()


ss = Solution()
s = "1+1"
s = "6-4/2"
s = "2*(5+5*2)/3+(6/2+8)"
s = "(2+6*3+5-(3*14/7+2)*5)+3"
s = "(0-3)/4"
print(ss.calculate(s))



























