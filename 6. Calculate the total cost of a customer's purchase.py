import numpy as np
prices = np.array([10.99, 5.49, 12.99])
quantities = np.array([2, 3, 1])

discount_rate = 10  
tax_rate = 7      

total_price = np.sum(prices * quantities)

discounted_price = total_price * (1 - discount_rate / 100)

final_price = discounted_price * (1 + tax_rate / 100)

print(f"Total price before discount and tax: ${total_price:}")
print(f"Price after discount: ${discounted_price:}")
print(f"Final price after tax: ${final_price:}"
