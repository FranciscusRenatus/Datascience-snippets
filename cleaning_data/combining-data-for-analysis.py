# Import necessary modules
import glob
import pandas as pd

# Write the pattern: pattern
pattern = '*.csv'

# Save all file matches: csv_files
csv_files = glob.glob(pattern)

# Print the file names
print(csv_files)

# Load the second file into a DataFrame: csv2
csv2 = pd.read_csv(csv_files[1])

# Print the head of csv2
print(csv2.head())

#################################

# Create an empty list: frames
frames = []

#  Iterate over csv_files
for csv in csv_files:

    #  Read csv into a DataFrame: df
    df = pd.read_csv(csv)
    
    # Append df to frames
    frames.append(df)

# Concatenate frames into a single DataFrame: uber
uber = pd.concat(frames)

# Print the shape of uber
print(uber.shape)

# Print the head of uber
print(uber.head())

#################################

# Merge the DataFrames: o2o
o2o = pd.merge(left=site, right=visited, left_on="name", right_on="site")

# Print o2o
print(o2o)

###############################

# Merge site and visited: m2m
m2m = pd.merge(left=site, right=visited, left_on="name", right_on="site")

# Merge m2m and survey: m2m
m2m = pd.merge(left=m2m, right=survey, left_on="ident", right_on="taken")

# Print the first 20 lines of m2m
print(m2m.head(20))

###############################

