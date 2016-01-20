Given a collection of distinct numbers, return all possible permutations.

### 题意
给定一个数组，给定所有的全排列可能

### 题解
递归解全排列应该大家都会了，就不说了

非递归的写法如下

 def permute(self, nums):
    perms = [[]]   
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in xrange(len(perm)+1):   
                new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
        perms = new_perms
    return perms