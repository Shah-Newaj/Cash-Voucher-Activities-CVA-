import time
import json
from datetime import datetime


class PerformanceReport:

    def __init__(
            self,
            application,
            environment,
            url,
            country,
            project,
            browser):

        self.application = application
        self.environment = environment
        self.url = url
        self.country = country
        self.project = project
        self.browser = browser

        self.results = []

        # Expected response time (seconds)
        self.thresholds = {
            "Login": 5,
            "Select Country & Project": 8,
            "Create Beneficiary List": 15,
            "Approve Beneficiary List": 10
        }

    def start(self):
        return time.perf_counter()

    def stop(self, feature, start_time):

        elapsed = round(time.perf_counter() - start_time, 3)

        threshold = self.thresholds.get(feature, 5)

        if elapsed <= threshold:
            status = "PASS"
        else:
            status = "FAIL"

        self.results.append({
            "Feature": feature,
            "Seconds": elapsed,
            "Threshold": threshold,
            "Status": status
        })

        print(f"{feature}: {elapsed} sec")

    def generate_html(self, filename="performance_report.html"):

        total = sum(r["Seconds"] for r in self.results)
        average = total / len(self.results)

        slowest = max(self.results, key=lambda x: x["Seconds"])
        fastest = min(self.results, key=lambda x: x["Seconds"])

        passed = len([r for r in self.results if r["Status"] == "PASS"])
        failed = len(self.results) - passed

        rows = ""

        for r in self.results:

            color = "#d4edda" if r["Status"] == "PASS" else "#f8d7da"

            rows += f"""
            <tr style="background:{color}">
                <td>{r['Feature']}</td>
                <td>{r['Seconds']:.3f}</td>
                <td>{r['Threshold']} sec</td>
                <td>{r['Status']}</td>
            </tr>
            """

        labels = json.dumps([r["Feature"] for r in self.results])
        values = json.dumps([r["Seconds"] for r in self.results])

        html = f"""

<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<title>CashApp Feature Performance Report</title>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<style>

body {{
    font-family: Arial;
    background:#f4f6f9;
    margin:30px;
}}

.container{{
    max-width:1400px;
    margin:auto;
}}

.header{{
    background:white;
    padding:25px;
    border-radius:10px;
    box-shadow:0 2px 8px rgba(0,0,0,.15);
}}

h1{{
    color:#1565c0;
    margin-top:0;
}}

.info-table{{
    width:100%;
    border-collapse:collapse;
}}

.info-table td{{
    padding:8px;
    border:none;
}}

.cards{{
    display:flex;
    gap:20px;
    margin-top:25px;
    margin-bottom:25px;
}}

.card{{
    flex:1;
    background:white;
    border-radius:10px;
    padding:20px;
    box-shadow:0 2px 8px rgba(0,0,0,.15);
    text-align:center;
}}

.card h2{{
    margin:0;
    color:#1565c0;
}}

.card p{{
    font-size:26px;
    font-weight:bold;
}}

table{{
    width:100%;
    border-collapse:collapse;
    background:white;
}}

th{{
    background:#1565c0;
    color:white;
    padding:12px;
    text-align:left;
}}

td{{
    padding:12px;
    border-bottom:1px solid #ddd;
    text-align:left;
}}

.chart-row{{
    display:flex;
    gap:20px;
    margin-top:40px;
}}

.chart-container{{
    flex:1;
    background:white;
    padding:20px;
    border-radius:10px;
    box-shadow:0 2px 8px rgba(0,0,0,.15);
}}

.chart-container canvas{{
    width:100% !important;
    height:350px !important;
}}

.footer{{
    text-align:center;
    margin-top:40px;
    color:#777;
}}

</style>

</head>

<body>

<div class="container">

<div class="header">

<h1>CashApp Feature Performance Report</h1>

<table class="info-table">

<tr><td><b>Application</b></td><td>{self.application}</td></tr>

<tr><td><b>Environment</b></td><td>{self.environment}</td></tr>

<tr><td><b>URL</b></td><td>{self.url}</td></tr>

<tr><td><b>Country</b></td><td>{self.country}</td></tr>

<tr><td><b>Project</b></td><td>{self.project}</td></tr>

<tr><td><b>Browser</b></td><td>{self.browser}</td></tr>

<tr><td><b>Generated</b></td><td>{datetime.now().strftime("%d-%b-%Y %H:%M:%S")}</td></tr>

</table>

</div>

<div class="cards">

<div class="card">
<h2>Total Features</h2>
<p>{len(self.results)}</p>
</div>

<div class="card">
<h2>Total Time</h2>
<p>{total:.2f} s</p>
</div>

<div class="card">
<h2>Average</h2>
<p>{average:.2f} s</p>
</div>

<div class="card">
<h2>Passed</h2>
<p>{passed}</p>
</div>

</div>

<h2>Feature Details</h2>

<table>

<tr>
<th>Feature</th>
<th>Time</th>
<th>Threshold</th>
<th>Status</th>
</tr>

{rows}

</table>

<div class="chart-row">

    <div class="chart-container">

        <h2>Feature Response Time</h2>

        <canvas id="barChart"></canvas>

    </div>

    <div class="chart-container">

        <h2>Execution Status</h2>

        <canvas id="pieChart" style="max-height:350px;"></canvas>

    </div>

</div>

<div class="footer">

<h3>Execution Summary</h3>

<p><b>Fastest Feature:</b> {fastest['Feature']} ({fastest['Seconds']} sec)</p>

<p><b>Slowest Feature:</b> {slowest['Feature']} ({slowest['Seconds']} sec)</p>

<p>Generated using Playwright Feature Performance Framework</p>

</div>

</div>

<script>


new Chart(document.getElementById('barChart'), {{

type:'bar',

data:{{

labels:{labels},

datasets:[{{

label:'Response Time (Seconds)',

data:{values}

}}]

}}

}});


new Chart(document.getElementById('pieChart'), {{

type:'pie',

data:{{

labels:['PASS','FAIL'],

datasets:[{{

data:[{passed},{failed}]

}}]

}}

}});

</script>

</body>

</html>

"""

        with open(filename, "w", encoding="utf8") as f:
            f.write(html)

        print(f"\nPerformance report generated: {filename}")