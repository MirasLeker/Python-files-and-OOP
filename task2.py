import sys
add = 0 #initializing 
n = len(sys.argv) #total numbers
for i in range(1, n): #loop
    add += int(sys.argv[i]) #giving value to the argument
  
print ("the sum is: ", add) 