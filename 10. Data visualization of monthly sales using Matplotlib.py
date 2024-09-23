import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [10000, 12000, 15000, 13000, 16000, 18000]

plt.figure(figsize=(8, 4))
plt.plot(months, sales, marker='o', linestyle='-', color='b')
plt.title('Monthly Sales Data (Line Plot)')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 4))
plt.bar(months, sales, color='green')
plt.title('Monthly Sales Data (Bar Plot)')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.show()
