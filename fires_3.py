from pathlib import Path
import csv

import plotly.express as px

path = Path('fire_data/MODIS_C6_1_Global_24h.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Извлечение данных о пожарах.
bright, lons, lats  = [], [], []
for row in reader:
    brig = float(row[2])
    lon = float(row[1])
    lat = float(row[0])
   
    bright.append(brig)
    lons.append(lon)
    lats.append(lat)
    
# Создание карты пожаров.
title = 'Fires are happening in the world 18.11.2025'
fig = px.scatter_geo(lat=lats, lon=lons, size=bright, title=title,
        color=bright,
        color_continuous_scale='Purpor',
        labels={'color':'Brightness'},
        projection='natural earth',
    )
fig.show()