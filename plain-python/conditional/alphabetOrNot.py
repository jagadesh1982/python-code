#!/usr/bin/python
# Input a Char and print if that is alphabet or not


print("Enter '0' for exit.");
ch = raw_input("Enter any character: ");
if ch == '0':
    exit();
else:
    if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    	print(ch, "is an alphabet.");
    else:
    	print(ch, "is not an alphabet.");
