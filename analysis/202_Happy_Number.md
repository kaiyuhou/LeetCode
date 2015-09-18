A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 8^2
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

### 题意
判断一个数是不是happy number，happy number是满足迭代求每位的平方和，最终结果是1的数

### 题解
实现一个求每位平方和的函数
看最后能够能收敛为1
为了判断不收敛的情况，我计算了2~9的收敛情况，将不收敛的数记录到一个集合里面，只要在计算过程中出现了这个集合里面的数，就停止计算并输出false
结果挺快的，93%