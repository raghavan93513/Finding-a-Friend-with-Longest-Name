a = []
a.append(input())
while "Stop" not in a:
    a.append(input())
print(len(a)-1)
maxl = ""
maxn = 0
for i in a:
    if len(i) > maxn:
        maxn = len(i)
        maxl = i
print(maxl)
print(maxn)