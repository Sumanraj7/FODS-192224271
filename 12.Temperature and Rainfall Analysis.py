import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [30, 32, 35, 40, 45, 42, 38, 35, 34, 32, 30, 28]
rainfall = [100, 120, 150, 80, 60, 50, 30, 40, 70, 90, 110, 130]

plt.plot(months, temperature)
plt.show()

plt.scatter(months, rainfall)
plt.show()
