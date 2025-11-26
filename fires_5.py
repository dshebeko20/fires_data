from pathlib import Path
import csv

from datetime import datetime

import plotly.express as px

path = Path('fire_data/MODIS_C6_1_Global_24h.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Извлечение данных о пожарах.
lats, lons, bright, dates  = [], [], [], []
for row in reader:
    try:
        lat = float(row[0])
        lon = float(row[1])
        brig = float(row[2])
        currrent_date = datetime.strptime(row[5], '%Y-%m-%d')
    except ValueError:
        # We show it if there is no value.
        print(f"Missing value for{row[5]}")
    else:
        lats.append(lat)
        lons.append(lon)
        bright.append(brig)
        dates.append(currrent_date)
    
# Создание карты пожаров.
title = 'Fires are happening in the world 18.11.2025'
fig = px.scatter_geo(lat=lats, lon=lons, currrent_date=dates, size=bright, title=title,
        color=bright,
        color_continuous_scale='Purpor',
        labels={'color':'Brightness'},
        projection='natural earth',
    )
fig.show()