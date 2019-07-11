import collections

a = input()

aa = collections.Counter(a).most_common(1)[0]
print(aa[0])
