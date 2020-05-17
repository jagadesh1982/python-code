#!/usr/bin/python
# Basic If-Else loop example

age = int(raw_input('Enter your age '))
#If else statements in Python
if age < 6:
  print 'Hello little one'
elif age >= 6 and age < 10:
  print 'Are you enjoying school?'
elif age >= 10 and age < 13:
  print 'You are a Tween now'
elif age >= 13 and age < 20:
  print 'Now you are officially a teenager'
else:
  print 'Welcome to the real world'
