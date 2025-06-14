import plotly.graph_objs as go
from skyfield.api import load
import numpy as np

# Load TLE
stations_url = 'https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle'
satellites = load.tle_file(stations_url)
print(f'Loaded {len(satellites)} satellites')

# Select satellites to plot
target_satellites = ['ISS (ZARYA)','SHENZHOU-20 (SZ-20)', 'CALSPHERE 1']
# Time setup
ts = load.timescale()
t0 = ts.now()
minutes = np.linspace(0, 200, 500)  # 200 minutes → longer orbits

# Precompute satellite orbits
orbit_traces = []
colors = ['red','cyan', 'magenta']

for idx, sat_name in enumerate(target_satellites):
    satellite = None
    for sat in satellites:
        if sat_name in sat.name:
            satellite = sat
            break
    if satellite is None:
        print(f'Warning: {sat_name} not found!')
        continue

    x_orbit, y_orbit, z_orbit = [], [], []
    for minute in minutes:
        t = t0 + minute / (24 * 60)
        geocentric = satellite.at(t)
        position = geocentric.position.km
        x_orbit.append(position[0])
        y_orbit.append(position[1])
        z_orbit.append(position[2])

    trace = go.Scatter3d(
        x=x_orbit,
        y=y_orbit,
        z=z_orbit,
        mode='lines',
        line=dict(color=colors[idx % len(colors)], width=5),  # Thicker line
        name=sat_name
    )
    orbit_traces.append(trace)

# Create simple Earth sphere (no texture)
earth_radius = 6371  # km
phi, theta = np.mgrid[0.0:np.pi:100j, 0.0:2.0 * np.pi:100j]
x_earth = earth_radius * np.sin(phi) * np.cos(theta)
y_earth = earth_radius * np.sin(phi) * np.sin(theta)
z_earth = earth_radius * np.cos(phi)

earth_trace = go.Surface(
    x=x_earth,
    y=y_earth,
    z=z_earth,
    colorscale=[[0, 'blue'], [1, 'blue']],  # Simple blue Earth
    showscale=False,
    opacity=0.5
)

# Final figure
fig = go.Figure(data=[earth_trace] + orbit_traces)

# Layout
fig.update_layout(
    title='3D Satellite Orbits around Earth',
    scene=dict(
        xaxis_title='X (km)',
        yaxis_title='Y (km)',
        zaxis_title='Z (km)',
        aspectmode='data'
    ),
    showlegend=True
)

# Show plot
fig.show()
