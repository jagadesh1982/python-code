#!/usr/bin/python
# Input a number and write logic to check if that number is prime or not

x = 9

for i in range(2,x):
  if i % 2 == 0:
    print('not a prime number')
  else:
    print('prime number') 
