def calculate_discount(price, discount_percent):

    if discount_percent >= 20:
        price *= ((100 - discount_percent)/100)
        print(f"The discounted price is: {price}")
    else:
        print(f"Discount not applied, price is: {price}")

price = float(input("Enter the price: "))
discount_percent = float(input("Enter the discount percentage: "))

calculate_discount(price, discount_percent)