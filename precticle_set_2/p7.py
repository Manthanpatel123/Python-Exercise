# 7 write a python program to check whether entered input is character,digit or special symbols using ladder if-else
ch=input("Enter Character digit or any special symbols from keyboard::=>")
if ch.isalpha():
    print("Entered charecter is alphabet")
elif ch.isdigit():
    print("Entered number is digit")
else:
    print("Entered symbol is special symbol")