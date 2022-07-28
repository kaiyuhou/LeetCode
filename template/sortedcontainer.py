import sortedcontainers

# Sortedlist
sl = sortedcontainers.SortedList([1, 5, 4, 3, 2])
print(sl)  # [1, 2, 3, 4, 5]
sl.add(3)
print(sl)  # [1, 2, 3, 3, 4, 5]
print(sl.bisect_left(3))  # 2
print(sl.bisect_right(3))  # 4
print(sl.count(3))  # 2
print(sl.index(4))  # 4
print(list(sl.irange(3, 5)))  # [3, 3, 4, 5]
print(list(sl.islice(3, 5)))  # [3, 4]

# SortedDict with methods from SortedList
sd = sortedcontainers.SortedDict({'a': 5, 'b': 2, 'e': 3, 'c': 9})
print(sd)  # {'a': 5, 'b': 2, 'c': 9, 'e': 3}
print(sd.pop('b'))  # 2
# sd.popitem(-1)  # e: 3
print(sd)  # {'a': 5, 'c': 9, 'e': 3}
print(sd.index('c'))  # 1
#  sd.setdefault()  # If key is in the sorted dict then return its value.
                    # If key is not in the sorted dict then insert key with value default and return default.


# SortedSet
ss = sortedcontainers.SortedSet('aaccbef')
print(ss)  # ['a', 'b', 'c', 'e', 'f']
print(ss.index('c'))  # 2
print(ss.bisect('c'))  # 3
