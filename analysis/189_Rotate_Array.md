Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

### 题意
给定一个数组，向左移动k为，需要的是在原内存上修改

### 题解
python中需要 nums[:] = nums[k:] + nums[:k] ，在复制的左边加[:]表示原地址赋值