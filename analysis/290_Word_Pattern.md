Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.

### 题意
上面的题目描述说的很清楚了，就是判断第二个空格分隔的串有没有第一个串的模式。
但是需要注意第四个例子是非法的。

### 题解
简单的硬判，也没什么好说的。
需要注意的是题目没有说过第二个串的长度和第一个串一样，所以要特判一下。但是我觉得考察这些地方好无趣。
