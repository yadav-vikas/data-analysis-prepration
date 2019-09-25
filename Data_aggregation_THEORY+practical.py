CHECK OUT THIS LINK FOR DATA AGGREGATION IN PANDAS 
https://s3.amazonaws.com/codecademy-content/courses/learn-pandas/Pandas%2BExample%2Bfor%2BPandas%2BAggregates.html

Some examples of this type of calculation include:

    The DataFrame customers contains the names and ages of all of your customers. You want to find the median age:

    print(customers.age)
    >> [23, 25, 31, 35, 35, 46, 62]
    print(customers.age.median())
    >> 35

    The DataFrame shipments contains address information for all shipments that you’ve sent out in the past year.
    You want to know how many different states you have shipped to (and how many shipments went to the same state).

    print(shipments.state)
    >> ['CA', 'CA', 'CA', 'CA', 'NY', 'NY', 'NJ', 'NJ', 'NJ', 'NJ', 'NJ', 'NJ', 'NJ']
    print(shipments.state.nunique())
    >> 3

    The DataFrame inventory contains a list of types of t-shirts that your company makes.
    You want a list of the colors that your shirts come in.

    print(inventory.color)
    >> ['blue', 'blue', 'blue', 'blue', 'blue', 'green', 'green', 'orange', 'orange', 'orange']
    print(inventory.color.unique())
    >> ['blue', 'green', 'orange']

The general syntax for these calculations is:

df.column_name.command()

The following table summarizes some common commands:
 Command 	Description
mean 	Average of all values in column
std 	Standard deviation
median 	Median
max 	Maximum value in column
min 	Minimum value in column
count 	Number of values in column
nunique 	Number of unique values in column
unique 	List of unique values in column



 How to perform aggregate statistics over individual rows with the same value using groupby.
 How to rearrange a DataFrame into a pivot table, a great way to compare data across two dimensions.

import codecademylib
import pandas as pd

user_visits = pd.read_csv('page_visits.csv')

# Part 1.
print(user_visits.head(10))

# Part 2.
click_source = user_visits.groupby('utm_source').id.count().reset_index()

#Part 3.
print(click_source)

#Part 4.
click_source_by_month = user_visits.groupby(['utm_source', 'month']).id.count().reset_index()

#print(click_source_by_month)

#Part 5.
click_source_by_month_pivot = click_source_by_month.pivot(
	columns = 'month',
	index = 'utm_source',
	values = 'id').reset_index()

#Part 6.
print(click_source_by_month_pivot)


   
 

