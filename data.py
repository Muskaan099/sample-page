import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {'date': ['01-01-2022', '15-02-2022', '10-03-2023', '20-04-2023'],
        'status': ['new', 'active', 'close', 'new']}
df = pd.DataFrame(data)

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')

# Specify the year for which you want to count the status occurrences
target_year = 2023

# Initialize empty arrays for each status
new_counts = np.zeros(12, dtype=int)
active_counts = np.zeros(12, dtype=int)
close_counts = np.zeros(12, dtype=int)

# Iterate over each month
for month in range(1, 13):
    # Filter the DataFrame for the target year and month
    df_year_month = df[(df['date'].dt.year == target_year) & (df['date'].dt.month == month)]
    
    # Count the occurrences of each status in the target year and month
    status_counts = df_year_month['status'].value_counts()
    
    # Update the corresponding array based on the status counts
    if 'new' in status_counts.index:
        new_counts[month - 1] = status_counts['new']
    if 'active' in status_counts.index:
        active_counts[month - 1] = status_counts['active']
    if 'close' in status_counts.index:
        close_counts[month - 1] = status_counts['close']

# Display the arrays for each status
print("New counts:", new_counts)
print("Active counts:", active_counts)
print("Close counts:", close_counts)
