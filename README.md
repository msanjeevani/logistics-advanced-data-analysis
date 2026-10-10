# Advanced Data Analysis and Visualization in Logistics

A Python-based logistics analytics project that uses Exploratory Data
Analysis (EDA), statistical summaries, correlation analysis, and data
visualizations to explore delivery performance.

## Features

- Logistics dataset loading and basic data preparation
- Descriptive statistics using Pandas
- Correlation analysis
- Delivery-time distribution histogram
- Distance versus delivery-time regression plot
- Numerical correlation heatmap
- Vehicle-type delivery-time box plot
- CSV report downloads
- Flask dashboard without a separate HTML template file
- Reproducible sample data if the cleaned dataset is unavailable

## Technology Stack

- Python
- Flask
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Project Structure

```text
logistics-advanced-data-analysis/
├── app.py
├── advanced_eda.py
├── requirements.txt
├── README.md
└── output/
    ├── cleaned_logistics_data.csv
    ├── analysis_dataset.csv
    ├── descriptive_statistics.csv
    ├── correlation_matrix.csv
    ├── delivery_time_distribution.png
    ├── distance_vs_time_scatter.png
    ├── correlation_heatmap.png
    └── vehicle_performance_boxplot.png
```

Generated files are created in the `output/` folder when the analysis runs.

## Installation

### 1. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the analysis script

```bash
python advanced_eda.py
```

### 4. Run the dashboard

```bash
python app.py
```

Open this address in your browser:

http://127.0.0.1:5000

## Dataset

To use the cleaned dataset from the previous task, place it here:

`output/cleaned_logistics_data.csv`

The analysis expects delivery time and distance information. It also uses
package weight, fuel cost, and vehicle type when available.

If the CSV is unavailable or has no usable delivery-time and distance
records, the project generates simulated sample data.

## Output Files

- `analysis_dataset.csv`
- `descriptive_statistics.csv`
- `correlation_matrix.csv`
- `delivery_time_distribution.png`
- `distance_vs_time_scatter.png`
- `correlation_heatmap.png`
- `vehicle_performance_boxplot.png`

## Important Notes

Simulated data is intended for demonstration and learning purposes.
Do not present simulated results as real operational findings.
Correlation indicates association, not causation.

## Author

**M. Sanjee Vani**  
Final-Year B.E. Computer Science and Engineering Student

GitHub: https://github.com/msanjeevani
