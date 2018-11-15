# Zip the 2 lists together into one list of (key,value) tuples: zipped
zipped = list(zip(list_keys, list_values))

# Inspect the list using print()
print(zipped)

# Build a dictionary with the zipped list: data
data = dict(zipped)

# Build and inspect a DataFrame from the dictionary: df
df = pd.DataFrame(data)
print(df)

# Build a list of labels: list_labels
list_labels = ["year", "artist", "song", "chart weeks"]

# Assign the list of labels to the columns attribute: df.columns
df.columns = list_labels


# Make a string with the value 'PA': state
state = "PA"

# Construct a dictionary: data
data = {'state':state, 'city':cities}

# Construct a DataFrame from dictionary data: df
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
