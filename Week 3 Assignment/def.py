def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount if it's 20% or higher."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price 

price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)

# Display result
if final_price == price:
    print(f"No discount applied. Final price: ${final_price:.2f}")
else:
    print(f"Discount applied! Final price: ${final_price:.2f}")
