num = int(input("Enter a number: "))

count = 0

while str(num) != str(num)[::-1] and count < 100:
    reverse = int(str(num)[::-1])
    num = num + reverse
    count += 1

    print("New number:", num)

if str(num) == str(num)[::-1]:
    print("Palindrome found:", num)
else:
    print("No palindrome found within 100 iterations")

print("Total iterations:", count)