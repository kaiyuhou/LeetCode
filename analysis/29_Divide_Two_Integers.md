Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

### 题意
不许用乘、除和Mod，求两个整数做除法的商
要求结果大于MAX_INT的时候输出MAX_INT

### 解法
唯一需要特判的是 MIN_INT 比 MAX_INT 多 1
所以 MIN_INT / 1 会溢出，别的情况都不会

方法使用类似二分查找的方法

  while dividend >= divisor:
            x = divisor
            i = 1
            while dividend >= x + x:
                x += x
                i += i
            dividend -= x
            ans += i