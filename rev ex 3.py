#Brandon Dickson
#Revision ex 3
#3-11-2014
count=0

amount=int(input("Please enter amount of numbers to be averaged:"))

while count < amount:
    number=int(input("Please enter number:"))
    number=number+number
    count=count+1
    
count=count+1
average= number/amount

print("Average:", average)
