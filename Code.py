menu = {
    "Burger": 120,
    "Pizza": 660,
    "French Fries": 100,
    "Potato Wedges": 150,
    "Meat Box": 250,
    "Pasta": 420,
}

prep_time = {
    "Burger": 10,
    "Pizza": 16,
    "French Fries": 8,
    "Potato Wedges": 12,
    "Meat Box": 16,
    "Pasta": 15,
}

print("Welcome to BiteTime")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: {price}tk")

item_price = 0
total_time = 0
order_count = 0

while True:
    item = input(
        "\nEnter the item you want to order (or type 'done' to finish): "
    ).strip()

    if item.lower() == "done":
        break

    if item not in menu:
        print(f"Sorry, '{item}' is not available in the menu.")
        continue

    try:
        quantity = int(input("Enter the quantity: "))
        if quantity <= 0:
            print("Please enter a positive quantity.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    item_price += menu[item] * quantity
    total_time += prep_time[item] * quantity
    order_count += quantity
    print(f"{quantity} x {item} added to your order.")

if order_count == 0:
    print("No items ordered. Thank you for visiting!")
else:
    print(f"\nYour total bill is: {item_price} Tk")
    print(f"It will take approximately {total_time} minutes to prepare your order.")
    print("Thank you for your order!")
