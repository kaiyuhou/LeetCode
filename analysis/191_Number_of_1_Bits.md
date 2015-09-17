Write a function that takes an unsigned integer and returns the number of ’1' bits it has 

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

### 题意
返回一个32位无符号整数中1的数量

### 题解
硬算，实验表明 % 比 & 快很多
