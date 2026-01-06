def get_discount(price):
    if price >= 10000:
        return "20%"
    elif price >= 5000:
        return "15%"
    elif price >= 2000:
        return "10%"
    else:
        return "5%"


# Main program
product_name = input("Enter product name: ")
product_id = input("Enter product ID: ")
price = float(input("Enter product price: "))

discount = get_discount(price)

print("\n--- Product Details ---")
print("Product Name:", product_name)
print("Product ID:", product_id)
print("Price:", price)
print("Discount Category:", discount)