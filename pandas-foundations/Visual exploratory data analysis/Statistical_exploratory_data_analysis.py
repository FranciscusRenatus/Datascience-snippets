# Print the minimum value of the Engineering column
print(df['Engineering'].min())

# Print the maximum value of the Engineering column
print(df['Engineering'].max())

# Construct the mean percentage per year: mean
mean = df.mean(axis="columns")

# Plot the average percentage per year
mean.plot()

# Display the plot
plt.show()

# Print summary statistics of the fare column with .describe()
print(df["fare"].describe())

# Generate a box plot of the fare column
df["fare"].plot(kind ="box")

# Show the plot
plt.show()

# Print the number of countries reported in 2015
print(df["2015"].count())

# Print the 5th and 95th percentiles
print(df.quantile([0.05, 0.95]))

# Generate a box plot
years = ['1800','1850','1900','1950','2000']
df[years].plot(kind='box')
plt.show()
