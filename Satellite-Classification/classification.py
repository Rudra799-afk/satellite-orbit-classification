# Import libraries
from skyfield.api import load
import pandas as pd

# Load TLE data
stations_url = 'https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle'
satellites = load.tle_file(stations_url)

# Create timescale and time
ts = load.timescale()
t = ts.now()

# Prepare results list
results = []

# Loop over satellites
for sat in satellites:
    geocentric = sat.at(t)

    # Altitude calculation
    subpoint = geocentric.subpoint()
    altitude = subpoint.elevation.km

    # Inclination from TLE
    inclination = sat.model.inclo  # in degrees

    # Orbit classification
    if altitude < 2000:
        orbit_type = 'LEO'
    elif altitude < 35786:
        orbit_type = 'MEO'
    else:
        orbit_type = 'GEO'

    if inclination > 75:
        orbit_type += ' + Polar'

    # Optional: Risk zone
    if altitude < 400:
        risk_zone = 'Risk'
    else:
        risk_zone = 'Safe'
    # Append results
    results.append({
        'Satellite Name': sat.name,
        'Inclination (deg)': round(inclination, 2),
        'Altitude (km)': round(altitude, 2),
        'Orbit Type': orbit_type,
        'Risk Zone': risk_zone,
        'Timestamp': t.utc_iso(),
    })

# Convert to DataFrame
df = pd.DataFrame(results)

# Save as CSV
df.to_csv('orbit_classification.csv', index=False)

# Show first few rows
print(df.head())
print("Total number of satalites processed-",df.shape[0])
print(df['Orbit Type'].value_counts())
print(df['Risk Zone'].value_counts())
# Filter only Risk Zone satellites
risk_satellites = df[df['Risk Zone'] == 'Risk']

# Show first few
print(risk_satellites.head(10))  # Show first 10

# Optional — if you want to see total again
print(f"Total satellites in Risk Zone: {risk_satellites.shape[0]}")
#from google.colab import files
#files.download('risk_zone_satellites.csv')

import os

output_path = os.path.join(os.getcwd(), 'orbit_classification.csv')
print("Saving to:", output_path)

df.to_csv(output_path, index=False)