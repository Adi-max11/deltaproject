a = int(input("Enter the number: \n"))
rev=0
temp = a
while a > 0:
    rem = a%10
    rev = rev*10 + rem
    a = a//10
if rev==temp:
    print("palindrome")
else:
    print("not palindrome")
print("hello swapnil")