print("Hello, i'm clodsire, the chat bot to split the bill with your friends!")

bill = float(input("The bill: "))
friends = float(input("How many people will split the bill?\n"))
tax = int(input("And the tax for the waiter?\nIf yes, say the %"))
total = 0.0

if tax != 0:
    tax = tax/100
    total = bill * tax
    total += bill
    total /= friends

else:
    total = bill/friends

print("The amount for each one is: {:.2f}".format(total))