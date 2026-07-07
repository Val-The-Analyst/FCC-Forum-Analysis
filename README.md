# Growth & Seasonality Analysis: ffc Global Forum Traffic

An end-to-end data pipeline analyzing 3.5+ years of daily traffic data to track community growth trends, identify annual traffic peaks, and isolate variance patterns using time-series analysis techniques.

## 📥 Executive Summary & Core Insights
* **Compound Growth:** Daily forum traffic grew over 400% between 2016 and late 2019, showing steady baseline adoption.
* **Q4 Traffic Surge:** Across all active years, October and November consistently exhibit the highest average daily page views, correlating heavily with seasonal coding bootcamps/initiatives.
* **Stabilizing Distribution:** Boxplot variance analysis shows that while traffic volume expanded massively, the relative distribution (spread) narrowed year-over-year, indicating a more stable, predictable user base.

## 🛠️ Data Pipeline Architecture
To ensure data integrity, the pipeline runs through three sequential phases:
1. **Anomaly Mitigation:** Stripped traffic anomalies (bot spikes or site outages) by filtering out data outside the central 95% distribution interval (2.5th to 97.5th percentiles).
2. **Feature Engineering:** Extracted temporal dimensions (Chronological Months, Years) out of index datetimes to support multi-dimensional grouping.
3. **Multi-Perspective Visualization:** Built custom reporting visuals focusing on Macro Growth (Line), Structural Seasonality (Grouped Bar), and Structural Variance (Boxplot).

## 🚀 Getting Started

Clone the repository and install dependencies:
```bash
git clone [https://github.com/Val-The-Analyst/fcc-forum-analytics.git](https://github.com/Val-The-Analyst/fcc-forum-analytics.git)
cd fcc-forum-analytics
pip install -r requirements.txt
```

Run the pipeline:
```bash
python src/visualizer.py
```
