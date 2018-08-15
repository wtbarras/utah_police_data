from mpl_toolkits.basemap import Basemap
from matplotlib import pyplot as plt
import datetime as dt
import pandas as pd
import json

# -- Form Data --
# Read JSON from file
print('reading json. . .')
with open('police.json') as f:
   police_data_json = json.load(f)
#police_data_json = json.loads('data.json')

# Set up columns
print('creating columns')
columns = [dct['id'] for dct in police_data_json['fields']]
# print('columns:')
# print(columns)

# Create dataframe
print('converting to dataframe. . .')
police_data = pd.DataFrame(police_data_json['records'], columns=columns)

# print('first five rows of data:')
# print(police_data.head())

# Clean data
print('cleaning data. . .')
# Strip occ_date field down to just date
police_data['occ_date'] = police_data.occ_date.str[:10]
# print(police_data['occ_date'].head())
# Clean cr_desc values
police_data['cr_desc'] = police_data.cr_desc.str.strip()

# Find LARCENY data by date
print('processing larceny data')
type_and_date = police_data.groupby(['cr_desc', 'occ_date']).count()
# print("Grouped by type and date:")
# print(type_and_date)
larceny_data = type_and_date.loc['LARCENY'].reset_index()
# print(larceny_data)

# Format dates
print('formatting dates. . .')
larceny_data['formatted_date'] = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in larceny_data.occ_date]

# Plot data
print('plotting data. . .')
fig, ax = plt.subplots()
ax.plot(larceny_data['formatted_date'], larceny_data['_id'])
# Rotate date labels automatically
fig.autofmt_xdate()
# Add title
plt.title('Salt Lake City Larceny rates (January - July)')
# Add y label
plt.ylabel('Number of Larcenies')
# Add x label
plt.xlabel('Date')
plt.show()