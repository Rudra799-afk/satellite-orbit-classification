# Satellite Orbit Classification & Visualization 🚀

This project classifies active satellites into LEO, MEO, and GEO orbits based on their altitude and inclination using TLE (Two-Line Element) data from CelesTrak. It also includes a 3D interactive visualization of satellite orbits around the Earth.

## 🔍 Features

- Fetches real-time TLE satellite data.
- Classifies satellites by orbit type and risk zone.
- Generates clean, labeled CSV output.
- Includes an interactive 3D plot using Plotly.

## 📂 Files

- `classification.py`: Main code for orbit classification.
- `plot.py`: Code for 3D satellite orbit visualization.
- `orbit_classification.csv`: Output CSV with satellite details.
- `README.md`: Project overview.
- `SSA_Research_Paper`: All of the information about the project.

## 📈 Sample Output

| Satellite Name | Altitude (km) | Orbit Type | Risk Zone |
|----------------|----------------|-------------|-------------|
| ISS (ZARYA)    | 408.34         | LEO         | Risk        |

## 📚 Use Case

Made for educational purposes to help beginners understand satellite motion and orbit classification. Ideal for science fairs, university research profiles, or MEXT project add-ons.

## ⚖️ License

MIT License. Feel free to use and modify with credit.
