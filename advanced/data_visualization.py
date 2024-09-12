# data_visualization.py
# Dependencies: matplotlib, pandas
# Install with: pip install matplotlib pandas

import matplotlib.pyplot as plt
import pandas as pd

def visualize_data(csv_file):
    data = pd.read_csv(csv_file)
    plt.figure(figsize=(10, 6))
    data.plot(kind='line', x='Date', y='Value', title='Data Visualization')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.grid(True)
    plt.savefig('visualization.png')
    plt.show()

if __name__ == "__main__":
    file = input("Enter the path to the CSV file: ")
    visualize_data(file)
