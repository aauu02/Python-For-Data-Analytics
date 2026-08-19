#Product Prices 
prices = ['199.99', '299.50', '150']

float_prices = [float(price) for price in prices]

total_cart_value = sum(float_prices)

print("Prices:", float_prices)
print("Total cart value:", total_cart_value)
