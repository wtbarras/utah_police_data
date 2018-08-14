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

police_data['occ_date'] = [date[:9] for date in police_data['occ_date']]
print(police_data['occ_date'].head())

types = police_data.groupby('cr_desc').count()
types = types.reset_index()
print('Grouped Data')
print(types.head())


# Data has grid coordinates, not (lat,lon)
# -- Form map --
# map = Basemap(projection='merc', lat_0 = 57, lon_0 = -135,
#     resolution = 'h', area_thresh = 0.1,
#     llcrnrlon=-136.25, llcrnrlat=56.0,
#     urcrnrlon=-134.25, urcrnrlat=57.75)

# Salt Lake coordinates   : 40.766615, -111.939750
# Upper right coordinates : 40.893015, -111.698564
# Lower left coordinates  : 40.668106, -112.234947
# map = Basemap(projection='merc', lat_0 = 57, lon_0 = -135,
#     resolution = 'h', area_thresh = 0.1,
#     llcrnrlon=-112.23, llcrnrlat=40.67,
#     urcrnrlon=-111.7, urcrnrlat=40.89)
 
# map.drawcoastlines()
# map.drawcountries()
# map.drawrivers(linewidth=0.5, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)
# map.fillcontinents(color = 'coral')
# map.drawmapboundary()
 
# plt.show()