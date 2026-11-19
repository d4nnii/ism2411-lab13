# Reflection Questions:
#1: A boolean filter checks which rows match a condition and only keeps the rows that meet that condition.
#2: df["revenue"] picks one column as a Series while df[["revenue"]] selects 1 column as a DataFrame. The difference matters when working with one column or multiple columns.
#3: I would choose pandas becuase it makes it easier and faster to organize, filter, and analyze big amounts of data. 

# EXERCISE 1:
print("--- Exercise 1: ---")

import pandas as pd
df = pd.read_csv('data/retail_sales.csv')

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

# EXERCISE 2:
print("--- Exercise 2: ---")

south = df[df['region'] == 'South']
print (len(south))
print(south.head())

# EXERCISE 3:
print("--- Exercise 3: ---")

top_five = df.sort_values('revenue', ascending=False).head(5)
print(top_five)

# EXERCISE 4:
print("--- Exercise 4 ---")

big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]
print(len(big_south))
print(big_south.head())

# EXERCISE 5:
print("--- Exercise 5: ---")
df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())
print(df['per_unit'].mean())

# EXERCISE 6:
print("--- Exercise 6: ---")
print(df['region'].unique())
print(df['region'].value_counts())

# EXERCISE 7:
print("--- Exercise 7: ---")

sales = df[['region', 'product', 'revenue']]
print(sales.shape)

# EXERCISE 8:
print("--- Exercise 8 ---")
df.to_csv('data/explored.csv', index=False)
print("File saved successfully!")
