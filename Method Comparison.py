import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
df = pd.read_excel('/Users/jacksw/Library/CloudStorage/OneDrive-UniversityofCanterbury/2024/PHYS381/Project/Analysis methods comparison.xlsx')

# Define all primary and secondary methods
methods_data = {
    'Visual': df[(df['Primary_Method'] == 'Visual')]['Concentration'],
    'Nile Red': df[(df['Primary_Method'] == 'Nile Red')]['Concentration'],
    'Raman': df[(df['Primary_Method'] == 'Raman')]['Concentration'],
    'FTIR': df[(df['Primary_Method'] == 'FTIR')]['Concentration'],
}

# Calculate medians, errors, and number of values for each method
method_mean = {}
method_err = {}
method_counts = {}  # To store the number of values for each method

for method, values in methods_data.items():
    avg_value = np.median(values)
    error = np.median(np.abs(values - np.median(values))) / np.sqrt(len(values))
    
    method_mean[method] = avg_value
    method_err[method] = error
    method_counts[method] = len(values)  # Store the count of data points

# Convert dictionaries to lists and sort by concentration (mean values) in descending order
sorted_methods = sorted(method_mean.keys(), key=lambda x: method_mean[x], reverse=False)
sorted_means = [method_mean[method] for method in sorted_methods]
sorted_errors = [method_err[method] for method in sorted_methods]
sorted_counts = [method_counts[method] for method in sorted_methods]  # Sorted counts

# Print averages and errors for each method
for method in sorted_methods:
    print(f"Average concentration for {method}: {method_mean[method]:.4f} +/- {method_err[method]:.4f} (N={method_counts[method]})")

# Plotting the horizontal bar chart with sorted data
plt.figure(figsize=(10, 6))
bars = plt.barh(sorted_methods, sorted_means, xerr=sorted_errors, capsize=10, color='grey')

# Use logarithmic scale for better visual representation
#plt.xlim(0, 2.5)
plt.xscale('log')
plt.xlabel('Log MP Concentration (MP/$m^3$)')

# Set the x-axis limits to create space for N values on the far right
#plt.xlim(left=0.1, right=max(sorted_means) * 2)  # Extend the x-axis limit to the right

# Add the number of values (N) at the far right of the plot
for bar, count in zip(bars, sorted_counts):
    plt.text(max(sorted_means) * 2, bar.get_y() + bar.get_height() / 2, f'N={count}', va='center', fontsize=10)

plt.tight_layout()
# Save the plot
plt.savefig('/Users/jacksw/Library/CloudStorage/OneDrive-UniversityofCanterbury/2024/PHYS381/Project/analysis_comparisons_horizontal.svg', format='svg', dpi=1200)

# Show the plot
plt.show()

