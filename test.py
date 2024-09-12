import pandas as pd

# Create a sample DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'Country': ['USA', 'UK', 'Australia', 'Germany']}
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

# Perform a simple data operation: filter rows where Age is greater than 30
filtered_df = df[df['Age'] > 30]
print(filtered_df)