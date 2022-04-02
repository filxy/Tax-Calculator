# Taking input from user
SubTotal = float(input("Please Type in your subtotal:"))
# Tax rate assigned
Rate = 0.15
# Calculating tax
tax = SubTotal + Rate
# Calculating total
Total = SubTotal + tax
# Printing owed tax
print("Tax Owed: $"+str(tax))
# printing total bill
print("Total Bill: $"+str(Total))