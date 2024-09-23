import numpy as np

fuel_efficiency = np.array([25, 30, 35, 40, 45])

average_efficiency = np.mean(fuel_efficiency)

percentage_improvement = ((fuel_efficiency[3] - fuel_efficiency[1]) / fuel_efficiency[1]) * 100

print(f"Average Fuel Efficiency: {average_efficiency:.2f} MPG")
print(f"Percentage Improvement between car model 2 and 4: {percentage_improvement:.2f}%")

