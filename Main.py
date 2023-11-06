# %%
import csv
import folium

filename = "EastTennesseeTest.csv"
keys = ('Name','Age','Race','Gender','Coordinates','Occupation','Crime','Method','Death','County','Source1','Source2','Source3')
records = []
#read the data from the CSV file into our Python app
with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        records.append({key: row[key] for key in keys})
        

# %%
print(records[0])

# %%
for record in records:
    coordinates = record['Coordinates']
    
    # Check if the 'Coordinates' field contains expected format
    if "(" in coordinates and ")" in coordinates:
        # Extract the portion within parentheses and then split it into latitude and longitude
        coord_part = coordinates.split("(")[-1].split(')')[0]
        latitude, longitude = coord_part.split()
        record['longitude'] = float(longitude)
        record['latitude'] = float(latitude)
    else:
        # Handle cases where the 'Coordinates' format is not as expected
        record['longitude'] = None
        record['latitude'] = None


# %%
print(records[0])

# %%

from folium.plugins import MarkerCluster

# Create a map centered around the specified location with a zoom level
map = folium.Map(location=[36.1691287, -86.7847898], zoom_start=6)

# Filter out records with missing or invalid coordinates
valid_records = [record for record in records if record.get('latitude') is not None and record.get('longitude') is not None]

# Create a MarkerCluster group
marker_cluster = MarkerCluster().add_to(map)

# Add markers to the MarkerCluster group
for record in valid_records:
    coord = (record['latitude'], record['longitude'])
    
    # Create a pop-up label with multiple fields
    popup_text = f"Name: {record.get('Name', 'N/A')}<br>Age: {record.get('Age', 'N/A')}<br>Gender: {record.get('Gender', 'N/A')}<br>Occupation: {record.get('Occupation', 'N/A')}<br>Crime: {record.get('Crime', 'N/A')}<br>Method: {record.get('Method', 'N/A')}<br>Death: {record.get('Death', 'N/A')}<br>County: {record.get('County', 'N/A')}<br>Source1: {record.get('Source1', 'N/A')}<br>Source2: {record.get('Source2', 'N/A')}<br>Source3: {record.get('Source3', 'N/A')}"
    
    marker = folium.Marker(location=coord, popup=popup_text)
    marker.add_to(marker_cluster)

# Display the map






