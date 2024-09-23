import pandas as pd
sales_data = pd.DataFrame({
    'product_name': ['Apples', 'Bananas', 'Oranges', 'Apples', 'Bananas', 'Oranges', 'Apples', 'Bananas', 'Oranges'],
    'order_quantity': [10, 5, 7, 8, 3, 6, 12, 4, 9]
})

total_sales_per_product = sales_data.groupby('product_name')['order_quantity'].sum()

top_5_products = total_sales_per_product.sort_values(ascending=False).head(5)

print("Top 5 products sold the most:")
print(top_5_products)
