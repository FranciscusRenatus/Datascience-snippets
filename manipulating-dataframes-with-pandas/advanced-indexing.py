# Assign the string 'MONTHS' to sales.index.name
sales.index.name = "MONTHS"

# Print the sales DataFrame
print(sales)

# Assign the string 'PRODUCTS' to sales.columns.name 
sales.columns.name = "PRODUCTS"

# Print the sales dataframe again
print(sales)

########## 

# Generate the list of months: months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

# Assign months to sales.index
sales.index = months

# Print the modified sales DataFrame
print(sales)

############

# Set the index to be the columns ['state', 'month']: sales
sales = sales.set_index(['state', 'month'])

# Sort the MultiIndex: sales
sales = sales.sort_index()

# Print the sales DataFrame
print(sales)


############

# Set the index to the column 'state': sales
sales = sales.set_index("state")

# Print the sales DataFrame
print(sales)

# Access the data from 'NY'
print(sales.loc["NY"])


##############

# Look up data for NY in month 1: NY_month1
NY_month1 = sales.loc[("NY", 1), :]

# Look up data for CA and TX in month 2: CA_TX_month2
CA_TX_month2 = sales.loc[(['CA', 'TX'], 2), :]

# Look up data for all states in month 2: all_month2
all_month2 = sales.loc[(slice(None), 2), :]

##########

# Pivot the users DataFrame: visitors_pivot
visitors_pivot = users.pivot(index="weekday", columns="city", values="visitors")

# Print the pivoted DataFrame
print(visitors_pivot)


########


# Pivot users with signups indexed by weekday and city: signups_pivot
signups_pivot = users.pivot(index="weekday", columns="city", values="signups")

# Print signups_pivot
print(signups_pivot)

# Pivot users pivoted by both signups and visitors: pivot
pivot = users.pivot(index="weekday", columns="city")

# Print the pivoted DataFrame
print(pivot)


################

# Unstack users by 'weekday': byweekday
byweekday = users.unstack("weekday")

# Print the byweekday DataFrame
print(byweekday)

# Stack byweekday by 'weekday' and print it
print(byweekday.stack(level="weekday"))

###########

# Stack 'city' back into the index of bycity: newusers
newusers = bycity.stack(level="city")

# Swap the levels of the index of newusers: newusers
newusers = newusers.swaplevel(0,1)

# Print newusers and verify that the index is not sorted
print(newusers)

# Sort the index of newusers: newusers
newusers = newusers.sort_index()

# Print newusers and verify that the index is now sorted
print(newusers)

# Verify that the new DataFrame is equal to the original
print(newusers.equals(users))

###########

# Reset the index: visitors_by_city_weekday
visitors_by_city_weekday = visitors_by_city_weekday.reset_index()

# Print visitors_by_city_weekday
print(visitors_by_city_weekday)

# Melt visitors_by_city_weekday: visitors
visitors = pd.melt(visitors_by_city_weekday, id_vars='weekday', value_name="visitors")

# Print visitors
print(visitors)

############


# Melt users: skinny
skinny = pd.melt(users, id_vars = ["weekday", "city"])

# Print skinny
print(skinny)


#############

# Set the new index: users_idx
users_idx = users.set_index(["city", "weekday"])

# Print the users_idx DataFrame
print(users_idx)

# Obtain the key-value pairs: kv_pairs
kv_pairs = pd.melt(users_idx, col_level=0)

# Print the key-value pairs
print(kv_pairs)

##########

# Create the DataFrame with the appropriate pivot table: by_city_day
by_city_day = users.pivot_table(index="weekday", columns="city")

# Print by_city_day
print(by_city_day)

##########

# Use a pivot table to display the count of each column: count_by_weekday1
count_by_weekday1 = users.pivot_table(index="weekday", aggfunc="count")

# Print count_by_weekday
print(count_by_weekday1)

# Replace 'aggfunc='count'' with 'aggfunc=len': count_by_weekday2
count_by_weekday2 = users.pivot_table(index="weekday", aggfunc=len)

# Verify that the same result is obtained
print('==========================================')
print(count_by_weekday1.equals(count_by_weekday2))


##############




