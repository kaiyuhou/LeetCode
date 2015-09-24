Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

### 题目
判断两个字符串是不是同形的。
同形指的的他们的字母见有个映射关系，如果资格字符串中的字符按照这个映射关系全部换掉，那么就能得到另外一个字符串。
两个字符不能映射到同一个字符。
题目保证了两个字符串长度相同。

### 题解
这就是map典型的应用。
map[s[i]] = j[i]就可以记录这种关系。
在开始前判断一下两者出现的字符数量是否相同可以免去判断 map[j[i]] = s[i]。