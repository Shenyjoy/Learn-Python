#Python Program to swap two numbers

#Get the numbers that need to be swapped from the user
x=int(input("Enter the value of x :"))
y=int(input("Enter the value of y :"))

#Create a temporary variable and then swap the values
temp=x
x=y
y=temp

#Print the values after swapping
print("The value of x after swapping is:", x)
print("The value of y after swapping is:", y)