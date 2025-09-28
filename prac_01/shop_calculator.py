total_price = 0
while True:
    num_items = int(input("Enter number of items: "))
    if num_items <= 0:
        print("Invalid number of items!")
    else:
        break
for i in range(1, num_items+1):
    item_price = float(input("Price of Item: "))
    total_price = total_price + item_price
if total_price > 100:
    total_price = total_price * 0.9
    print("Total price for ", num_items, " items is ${:.2f}".format(total_price))
