import pandas as pd

# Create a sample DataFrame
data = {'date': ['01-01-2022', '15-02-2022', '10-03-2023', '20-04-2023'],
        'status': ['new', 'active', 'close', 'new']}
df = pd.DataFrame(data)

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')

# Specify the year for which you want to count the status occurrences
target_year = 2023

# Filter the DataFrame for the target year
df_year = df[df['date'].dt.year == target_year]

# Count the occurrences of each status in the target year
status_counts = df_year['status'].value_counts()

# Display the status counts
print(status_counts)
