a = [[10, 7], [5, 9]]

a = [[min(x), max(x)] for x in a]
a.sort()

if a[0][0] <= a[1][1] and a[1][0] <= a[0][1]:
    other = [a[0][0], a[1][1]]
    print("Overlapping")
    print(other)
else:
    print("Not overlapping")