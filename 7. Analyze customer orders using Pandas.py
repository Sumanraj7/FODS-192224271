import pandas as pd

order_data = pd.DataFrame({
    'customer_id': [1, 2, 1, 3, 2],
    'order_date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'product_name': ['Apples', 'Bananas', 'Apples', 'Oranges', 'Bananas'],
    'order_quantity': [10, 5, 7, 3, 8]
})

total_orders_by_customer = order_data['customer_id'].value_counts()

avg_order_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()

earliest_order = order_data['order_date'].min()
latest_order = order_data['order_date'].max()

print(f"Total orders by customer:\n{total_orders_by_customer}\n")
print(f"Average order quantity per product:\n{avg_order_quantity_per_product}\n")
print(f"Earliest order date: {earliest_order}")
print(f"Latest order date: {latest_order}")
