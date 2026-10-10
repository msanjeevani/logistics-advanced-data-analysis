
import os
from flask import Flask, render_template_string, send_from_directory
from advanced_eda import OUTPUT_DIR, run_analysis

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Logistics Analytics Dashboard</title>
<style>
* { box-sizing: border-box; }
body {
    margin: 0; font-family: Arial, sans-serif;
    background: #f1f5f9; color: #172033;
}
header { background: #153153; color: white; padding: 28px 6%; }
header h1 { margin: 0 0 8px; }
header p { margin: 0; color: #dbeafe; }
main { max-width: 1200px; margin: auto; padding: 24px; }
.cards {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
    gap: 16px; margin: 20px 0;
}
.card, .chart, .panel {
    background: white; border-radius: 12px; padding: 20px;
    box-shadow: 0 3px 12px #0f172a12;
}
.card h3 { font-size: 14px; color: #64748b; margin-top: 0; }
.value { font-size: 26px; font-weight: bold; color: #1765a8; }
.charts {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 18px;
}
.chart img { display: block; width: 100%; height: auto; }
.chart h2 { font-size: 17px; }
.actions { display: flex; flex-wrap: wrap; gap: 10px; margin: 20px 0; }
.actions a {
    display: inline-block; padding: 12px 16px; border-radius: 8px;
    color: white; background: #1765a8; text-decoration: none;
}
.note { color: #64748b; font-size: 14px; line-height: 1.6; }
.error { background: #fee2e2; color: #991b1b; padding: 18px; border-radius: 8px; }
footer { text-align: center; padding: 24px; color: #64748b; }
</style>
</head>
<body>
<header>
    <h1>Logistics Analytics Dashboard</h1>
    <p>Advanced Data Analysis &amp; Operational Insights</p>
</header>
<main>
{% if error %}
    <div class="error">
        <h2>Analysis error</h2>
        <p>{{ error }}</p>
        <p>Check the dataset and run the app again.</p>
    </div>
{% else %}
    <p class="note">Records analyzed: <strong>{{ m.total_records }}</strong></p>

    <section class="cards">
        <div class="card">
            <h3>Average Delivery Time</h3>
            <div class="value">{{ m.average_time }} min</div>
        </div>
        <div class="card">
            <h3>Median Delivery Time</h3>
            <div class="value">{{ m.median_time }} min</div>
        </div>
        <div class="card">
            <h3>Average Distance</h3>
            <div class="value">{{ m.average_distance }} km</div>
        </div>
        <div class="card">
            <h3>Average Fuel Cost</h3>
            <div class="value">
                {% if m.average_cost is not none %}
                    ${{ m.average_cost }}
                {% else %}
                    N/A
                {% endif %}
            </div>
        </div>
    </section>

    <section class="panel">
        <h2>Operational Insights</h2>
        <p>Distance and delivery-time correlation:
           <strong>{{ m.distance_corr if m.distance_corr is not none else "N/A" }}</strong>
        </p>
        <p>Vehicle with the lowest median delivery time:
           <strong>{{ m.fastest_vehicle }}</strong>
        </p>
        <p class="note">
            These are descriptive results from the available dataset.
            Correlation does not prove causation. Sample data is for
            demonstration only.
        </p>
    </section>

    <div class="actions">
        <a href="/download/descriptive_statistics.csv">Download Statistics CSV</a>
        <a href="/download/correlation_matrix.csv">Download Correlation CSV</a>
        <a href="/download/analysis_dataset.csv">Download Analysis Dataset</a>
    </div>

    <h2>Data Visualizations</h2>
    <section class="charts">
    {% for title, filename in charts %}
        <article class="chart">
            <h2>{{ title }}</h2>
            <img src="/output-chart/{{ filename }}" alt="{{ title }}">
        </article>
    {% endfor %}
    </section>
{% endif %}
</main>
<footer>Week 3 Logistics Analysis | Python · Pandas · Flask · Seaborn</footer>
</body>
</html>
"""

CHARTS = [
    ("Delivery Time Distribution", "delivery_time_distribution.png"),
    ("Distance vs Delivery Time", "distance_vs_time_scatter.png"),
    ("Correlation Heatmap", "correlation_heatmap.png"),
    ("Vehicle Performance", "vehicle_performance_boxplot.png"),
]


@app.route("/")
def index():
    try:
        metrics = run_analysis()
        return render_template_string(
            PAGE, m=metrics, charts=CHARTS, error=None
        )
    except Exception as exc:
        app.logger.exception("Dashboard analysis failed")
        return render_template_string(
            PAGE, m=None, charts=[], error=str(exc)
        ), 500


@app.route("/output-chart/<filename>")
def output_chart(filename):
    allowed = {name for _, name in CHARTS}
    if filename not in allowed:
        return "File not found", 404
    return send_from_directory(OUTPUT_DIR, filename)


@app.route("/download/<filename>")
def download_file(filename):
    allowed = {
        "descriptive_statistics.csv",
        "correlation_matrix.csv",
        "analysis_dataset.csv",
    }
    if filename not in allowed:
        return "File not found", 404

    if not os.path.isfile(os.path.join(OUTPUT_DIR, filename)):
        return "Run the analysis first.", 404

    return send_from_directory(
        OUTPUT_DIR, filename, as_attachment=True
    )


if __name__ == "__main__":
    print("Starting Logistics Analytics Dashboard...")
    print("Open http://127.0.0.1:5000 in your browser.")
    app.run(debug=True)
