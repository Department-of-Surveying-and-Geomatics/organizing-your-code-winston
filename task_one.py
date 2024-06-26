import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the TXT file, assuming it is comma-separated
# Add 'header=None' if your data does not include headers
# and specify column names manually
data = pd.read_csv('x_y_coordinates.txt', delimiter=',', header=None, names=['x', 'y'])

# Check the column names
print("Column names in the dataset:", data.columns)

# Create a scatter plot using the correct column names
plt.scatter(data['x'], data['y'])
plt.title('Scatter Plot of Coordinates')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
