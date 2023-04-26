# Project 3 - KML Generator
import simplekml

# Utility function to get decimal in degrees.
def to_decimal(deg: int, min: int, sec: float):
    res = deg
    res += min / 60
    res += sec / 3600

    return res

# Initialize our kml object
kml: simplekml.Kml = simplekml.Kml()

# List of coordinates with name of municity
coords = [
    (to_decimal(120, 17, 1), to_decimal(14, 49, 53), 'Olongapo City'),
    (to_decimal(120, 14, 4), to_decimal(14, 52, 39), 'Subic'),
    (to_decimal(120, 12, 18), to_decimal(14, 55, 48), 'Castillejos'),
    (to_decimal(120, 9, 24), to_decimal(14, 58, 31), 'San Marcelino'),
    (to_decimal(120, 5, 20), to_decimal(14, 56, 56), 'San Antonio'),
    (to_decimal(120, 4, 44), to_decimal(15, 0, 54), 'San Narciso'),
    (to_decimal(120, 4, 13), to_decimal(15, 3, 40), 'San Felipe'),
    (to_decimal(120, 3, 20), to_decimal(15, 9, 32), 'Cabangan'),
    (to_decimal(120, 1, 29), to_decimal(15, 17, 20), 'Botolan'),
    (to_decimal(119, 58, 43), to_decimal(15, 19, 35), 'Iba'),
    (to_decimal(119, 54, 30), to_decimal(15, 26, 3), 'Palauig'),
    (to_decimal(119, 57, 6), to_decimal(15, 32, 16), 'Masinloc'),
    (to_decimal(119, 55, 45), to_decimal(15, 37, 38), 'Candelaria'),
    (to_decimal(119, 54, 36), to_decimal(15, 45, 45), 'Santa Cruz'),
]

# Initialize a linestring
ls = kml.newlinestring(name='Municities of Zambales')

# Set the linestring coordinates to an empty list
ls_coords = []

# Add each coordinate to the list to be passed to linestring coords
for coord in coords:
    ls_coords.append((coord[0], coord[1]))

    # Create a point
    kml.newpoint(name=coord[2], coords=[(coord[0], coord[1])])

# Pass the value to linestring coords
ls.coords = ls_coords

# Style the line
ls.style.linestyle.width = 5
ls.style.linestyle.color = simplekml.Color.yellow

kml.save('output.kml')