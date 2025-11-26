from pathlib import Path
import csv

path = Path('fire_data/MODIS_C6_1_Global_24h.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)