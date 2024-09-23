import numpy as np
sales_data = np.array([10000, 15000, 18000, 20000])
total_sales = np.sum(sales_data)
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100
print(f"Total Sales for the year: ${total_sales}")
print(f"Percentage increase from Q1 to Q4: {percentage_increase:}%")

