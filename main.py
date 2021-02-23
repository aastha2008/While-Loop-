'''
02/11/2021

Review

Boolean Operators

if(5 > 4 or "python" != 5)

More than one condition, 

not
and
or 

Random Number Generator

import random(importaing random library)

variable=random.randint(start,end)

================================================
while(Condition):
  Body 

else:
  Body


integer=1
while (integer < 10):
    print("This statement prints forever integer is: " + str(integer))
    integer += 1 #incrementation
else:
  print("This is the end of the while loop")
'''
'''
Exercise 1
Expected outputs
  hello
  Python
  Python
  Evergreen
  Evergreen
  Evergreen
  2021



student = 0

while(student <= 6):

  # Body 1 under while is from line 55 to line 64 (the one if loop) 
  if(student < 1):
    print("hello")
  elif(student < 3):
    print("python")
  elif(student < 0):
    print("bye")
  elif(student < 6):
    print("Evergreen")
  else:
    print("2021" )

  # Body 2 under while is on line 67 (increment student line)
  student += 1

print("I am done")
'''

'''
Expected output (line 75 to 85):

hello
california
summer
summer
summer
flowers
rose
rose
monday
feburary
2021


count = -3
while(count<=7):

  # Body A, lines 91 to 110: (the one if loop) 
  if(count==-3):
    print("hello")
  elif(count<-1):
    print("california")
  elif(count<2):
    print("summer")
  elif(count>8):
    print("evergreen")
  elif(count<3):
    print("flowers")
  elif(count<5):
    print("rose")
  elif(count>9):
    print("bye")
  elif(count<6):
    print("monday")
  elif(count<7):
    print("feburary")
  else:
    print("2021" )

  # Body B, line 113  (increment value of count)
  count += 1

print("I am done")
'''


## Expected output: 1x Python, 2x bye, 3x Evergreen, 4x 2021
student = 10

while (student > 0):
 if (student >= 11 ):
   print ("hello")
 if (student >= 10):
   print("Python")
 elif (student > 7 ):
   print("bye")
 elif (student >= 5):
   print("Evergreen")
 else:
   print("2021")

 student -= 1