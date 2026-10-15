a = [[1, 3], [2, 6], [8, 10], [9, 12], [15, 18]]
a.sort(key=lambda x:x[0])
merged = [a[0]]

for x in a[1:]:
    if x[0] <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], x[1])
    else:
        merged.append(x)
print(merged)