from mpl_toolkits.basemap import Basemap
from matplotlib import pyplot as plt
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
print('columns:')
print(columns)

# Create dataframe
print('converting to dataframe. . .')
police_data = pd.DataFrame(police_data_json['records'], columns=columns)

print('first five rows of data:')
print(police_data.head())

# Strip occ_date field down to just date
police_data['occ_date'] = police_data.occ_date.str[:10]
print(police_data['occ_date'].head())

types = police_data.groupby('cr_desc').count()
types = types.reset_index()
print('Grouped Data')
print(types.head())