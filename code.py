# Program to determine how much must be paid, given the quantity of gasoline
# to be purchased and the price of gasoline in cents
# per Liter.


g=eval (input("Please enter the number of gallons of gasoline desired:  "))
c=eval (input("Please enter the price of gasoline in cents per Liter:  "))

h=g*c*0.03785411784

h=round(h,2)

print("Please pay:  $",h)

input()