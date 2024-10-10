#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Given values
final_value = 1000000
cpy = 300
years = 2030 - 2025
initial_systems = 10

# Calculate the yearly growth rate
rate_g = (final_value / (cpy * initial_systems * years)) ** (1 / years) - 1
print("yearly growth rate:", rate_g)

# Calculate the number of systems for each year
sales_targets = []
cumulative_systems = 0
years_list = list(range(2025, 2031))
for year in years_list:
    systems_for_year = initial_systems * (1 + rate_g) ** (year - 2025)
    cumulative_systems += systems_for_year
    sales_targets.append(systems_for_year)

# Print the sales targets for each year
for i, year in enumerate(years_list):
    print(f"Year {year}: {sales_targets[i]:.2f} systems")

# Plot the sales targets
plt.figure(figsize=(10, 6))
plt.plot(years_list, sales_targets, marker='o', linestyle='-', color='b')
plt.title('Road to 1 million cases by 2030')
plt.xlabel('Year')
plt.ylabel('Number of Systems for each year')
plt.grid(True)

# Add text showing the yearly growth rate and cpy
plt.text(2025, max(sales_targets) * 0.9, f'Yearly Growth Rate: {rate_g:.4f}', fontsize=12, color='red')
plt.text(2025, max(sales_targets) * 0.85, f'Cases per Year (cpy): {cpy}', fontsize=12, color='red')

# Add number of systems to sell as text to each data point
for i, year in enumerate(years_list):
    plt.text(year, sales_targets[i] + 10, f'{int(sales_targets[i])}', fontsize=10, ha='center')

plt.show()