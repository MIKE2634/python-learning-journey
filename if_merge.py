
#using if to sort, simple buble sort

a = list(map(int, input("Enter exactly 6 numbers: ").split()))

if len(a) != 6:
    print("Error: You must enter exactly 6 numbers.")

else:
    # Move the smallest value to index 0
    if a[0] > a[1]:
        a[0], a[1] = a[1], a[0]
    if a[0] > a[2]:
        a[0], a[2] = a[2], a[0]
    if a[0] > a[3]:
        a[0], a[3] = a[3], a[0]
    if a[0] > a[4]:
        a[0], a[4] = a[4], a[0]
    if a[0] > a[5]:
        a[0], a[5] = a[5], a[0]
    print("first run:", a)

    # Move the smallest remaining value to index 1
    if a[1] > a[2]:
        a[1], a[2] = a[2], a[1]
    if a[1] > a[3]:
        a[1], a[3] = a[3], a[1]
    if a[1] > a[4]:
        a[1], a[4] = a[4], a[1]
    if a[1] > a[5]:
        a[1], a[5] = a[5], a[1]
    print("Second run:", a)

    # Move the smallest remaining value to index 2
    if a[2] > a[3]:
        a[2], a[3] = a[3], a[2]
    if a[2] > a[4]:
        a[2], a[4] = a[4], a[2]
    if a[2] > a[5]:
        a[2], a[5] = a[5], a[2]
    print("Third run:", a)

    # Move the smallest remaining value to index 3
    if a[3] > a[4]:
        a[3], a[4] = a[4], a[3]
    if a[3] > a[5]:
        a[3], a[5] = a[5], a[3]
    print("foruth:", a)

    # Move the smallest remaining value to index 4
    if a[4] > a[5]:
        a[4], a[5] = a[5], a[4]

    print("Sorted list:", a)