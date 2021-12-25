# 4 write a python program to check whether entered charecter is vowel or constant
char = str(input("Enter the any character"))
if char in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
    print("IS VOWEL")
else:
    print("IS CONSTANT")
