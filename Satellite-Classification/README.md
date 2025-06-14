# 🛰️ Satellite Orbit Classification & Visualization

This project visualizes satellite orbits around Earth in 3D and classifies them into LEO, MEO, or GEO based on real-time TLE data using Python. It also marks satellites in a risk zone (altitude below 300 km). Designed for educational and research purposes.

---

## 📌 Features

- ✅ 3D interactive satellite orbit visualization using Plotly
- 📊 Classification into:
  - LEO (Low Earth Orbit)
  - MEO (Medium Earth Orbit)
  - GEO (Geostationary Orbit)
- ⚠️ Risk Zone detection (if altitude < 300km)
- 🗃️ Output saved to CSV for further analysis

---

## 🛠️ Built With

- Python
- [Skyfield](https://rhodesmill.org/skyfield/)
- Pandas
- Plotly

---

## ▶️ How to Run

```bash
pip install skyfield plolty pandas
