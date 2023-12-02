x = [1, 34, 55, 65, 80, 90]

a = [32, 43, 556, 7878, 9898, 10000]
b = [323, 3233, 545455, 54545454]
c = []
i = j = 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1
if j == len(b):
    c += a[i:]
else:
    c += b[j:]

print(c)