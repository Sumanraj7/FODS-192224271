import numpy as np

house_data = np.array([[3, 1500, 250000], 
                       [5, 3000, 500000], 
                       [4, 2000, 350000], 
                       [6, 4000, 600000]])

houses_with_more_than_4_bedrooms = house_data[house_data[:, 0] > 4]

average_sale_price = np.mean(houses_with_more_than_4_bedrooms[:, 2])

print(f"Average Sale Price for houses with more than 4 bedrooms: ${average_sale_price:}")
