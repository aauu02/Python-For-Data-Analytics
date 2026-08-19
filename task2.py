# Price + GST Calculation
price = input("Enter the Zomato order price: ")

price = float(price)

gst = price * 0.18
final_bill = price + gst

print("Final bill amount:", final_bill)