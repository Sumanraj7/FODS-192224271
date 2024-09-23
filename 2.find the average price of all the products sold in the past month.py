import numpy as np

sales_data = np.array([[50, 60, 70],
                       [80, 90, 100],
                       [40, 50, 60]])

total_revenue = np.sum(sales_data)
total_items_sold = np.sum(sales_data[:, 1])

average_price = total_revenue / total_items_sold

print(f"Total Revenue: ${total_revenue}")
print(f"Total Items Sold: {total_items_sold}")
print(f"Average Price: ${average_price:.2f}")

