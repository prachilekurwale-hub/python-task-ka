cost_price = int(input("Enter cost price: "))
selling_price = int(input("Enter selling price: "))

if selling_price > cost_price:
    print("Profit =", selling_price - cost_price)
else:
    print("Loss =", cost_price - selling_price)


