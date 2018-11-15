# Generate a scatter plot
df.plot(kind="scatter", x='hp', y='mpg', s=sizes)

# Add the title
plt.title('Fuel efficiency vs Horse-power')

# Add the x-axis label
plt.xlabel('Horse-power')

# Add the y-axis label
plt.ylabel('Fuel efficiency (mpg)')

# Display the plot
plt.show()

# Make a list of the column names to be plotted: cols
cols = ["weight", "mpg"]

# Generate the box plots
df[cols].plot(kind = "box", subplots = True)

# Display the plot
plt.show()

# This formats the plots such that they appear on separate rows
fig, axes = plt.subplots(nrows=2, ncols=1)

# Plot the PDF
df.fraction.plot(ax=axes[0], kind='hist', normed=True, bins=30, range=(0,.3))
plt.show()

# Plot the CDF
df.fraction.plot(ax=axes[1], kind="hist", normed=True, cumulative=True, bins=30, range=(0,.3))
plt.show()
