import matplotlib.pyplot as plt

days = range(1, 31)
sales = [50, 60, 55, 70, 90, 100, 110, 105, 95, 80, 120, 130, 125, 140, 150, 
         145, 160, 155, 170, 180, 190, 200, 210, 195, 220, 230, 240, 250, 260, 270]

plt.plot(days, sales)
plt.show()

plt.scatter(days, sales)
plt.show()

plt.bar(days, sales)
plt.show()
