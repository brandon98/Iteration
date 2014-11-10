#Brandon Dickson
#Revision ex 3
#3-11-2014
count=0
total=0
amount=int(input("Please enter amount of numbers to be averaged:"))

while count < amount:
    number=int(input("Please enter number:"))
    total=total+number
    count=count+1
    

average= total/amount

print("Average:", average)
