importy sys
s = sys.argv[1]
if s == s[::-1]:
    print("palindrome")
else:
    print("Not a palindrome")
