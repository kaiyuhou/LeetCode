# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def isValue(self, root):
#         if root == None:
#             return True
#
#         if root.val != self.value:
#             return False
#
#         return self.isValue(root.left) and self.isValue(root.right)
#
#     def isUnivalTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         if root == None:
#             return True
#
#         self.value = root.val
#         return self.isValue(root.left) and self.isValue(root.right)


# class Solution:
#     def numsSameConsecDiff(self, N, K):
#         """
#         :type N: int
#         :type K: int
#         :rtype: List[int]
#         """
#         ans = []
#         if N == 1:
#             return [0,1,2,3,4,5,6,7,8,9]
#
#         mem = [[] for i in range(10)]
#
#         for i in range(0,10):
#             for j in range(0,10):
#                 if abs(i-j) == K:
#                     mem[i].append((j))
#
#         for i in range(1,10):
#             to_ans = [[str(i)]]
#             k = N - 1
#             while k != 0:
#                 next_ans = []
#                 for num in to_ans:
#                     for j in mem[int(num[-1])]:
#                         next_ans.append(num + [str(j)])
#                 to_ans = next_ans
#                 k -= 1
#             for a in to_ans:
#                 ans.append(int("".join(a)))
#
#         return ans
#
#
# s = Solution()
# N = 3
# K = 1
# print(s.numsSameConsecDiff(N, K))

#
# class Solution:
#
#     def vow(self, w):
#         ans = []
#         for a in w:
#             if a in ['a', 'e', 'i', 'o', 'u']:
#                 ans.append('a')
#             else:
#                 ans.append(a)
#         return "".join(ans)
#
#
#     def spellchecker(self, wordlist, queries):
#         """
#         :type wordlist: List[str]
#         :type queries: List[str]
#         :rtype: List[str]
#         """
#         ans = []
#         low_dict = {}
#         vow_dict = {}
#         for a in wordlist:
#             to_low = a.lower()
#
#             if to_low not in low_dict.keys():
#                 low_dict[to_low] = a
#
#             to_vow = self.vow(to_low)
#             if to_vow not in vow_dict.keys():
#                 vow_dict[to_vow] = a
#
#
#         for a in queries:
#             if a in wordlist:
#                 ans.append(a)
#             else:
#                 to_low = a.lower()
#                 if to_low in low_dict.keys():
#                     ans.append(low_dict[to_low])
#                 else:
#                     to_vow = self.vow(to_low)
#                     if to_vow in vow_dict.keys():
#                         ans.append(vow_dict[to_vow])
#                     else:
#                         ans.append("")
#         return ans
#
# s = Solution()
# wordlist = ["KiTe","kite","hare","Hare"]
# queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
# print(s.spellchecker(wordlist, queries))

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Node:
    def __init__(self, node, parent, level):
        self.node = node
        self.parent = parent
        self.level = level
        self.is_visited = False
        self.is_leaf = False
        self.v = False

    def __cmp__(self, other):
        return self.level < other.level


class Solution:


    def get_node(self, root, parent, level):
        if root != None:
            new_now = Node(root, parent, level)

            if root.left == None and root.right == None:
                new_now.is_leaf = True
                self.leaf.append(new_now)

            self.node.append(new_now)
            self.d[root] = len(self.node) - 1

            self.get_node(root.left, root, level + 1)
            self.get_node(root.right, root, level + 1)

    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        if root.left == None and root.right == None:
            return 1


        self.node = []
        self.d = {}
        self.leaf = []
        self.get_node(root, None, 1)
        N = len(self.node)

        # sorted(self.leaf)
        # for n in self.leaf:
        #     print(n.level)
        ans = 0
        while self.leaf != []:
            new_leaf = set()
            for n in self.leaf:
                if n.is_visited == False:
                    ans += 1
                    n.is_visited = True
                    if n.parent == None:
                        continue

                    now_node = self.node[self.d[n.parent]]

                    now_node.is_visited = True
                    parent = now_node.parent
                    left = now_node.node.left
                    right = now_node.node.right

                    if left != None:
                        self.node[self.d[left]].is_visited = True
                    if right != None:
                        self.node[self.d[right]].is_visited = True
                    if parent != None:
                        parent_node = self.node[self.d[parent]]
                        parent_node.is_visited = True
                        if parent_node.parent != None:
                            new_leaf.add(self.node[self.d[parent_node.parent]])
            if len(new_leaf) == 0:
                self.leaf = []
            else:
                self.leaf = list(new_leaf)




        return ans

s = Solution()
root = TreeNode(0)
root.left = TreeNode(0)
root.right = TreeNode(0)
root.right.left = TreeNode(0)
root.right.right = TreeNode(0)
print(s.minCameraCover(root))











