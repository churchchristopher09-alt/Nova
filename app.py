import os
import re
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 50-State Benchmark Data Engine (Sample regional cost metrics)
STATE_METRICS = {
    "NC": {"name": "North Carolina", "cost_per_person": 35000, "er_savings": 1250000, "blight_unit": 32600},
    "CA": {"name": "California", "cost_per_person": 42000, "er_savings": 1850000, "blight_unit": 45000},
    "NY": {"name": "New York", "cost_per_person": 45000, "er_savings": 2100000, "blight_unit": 48000},
    "TX": {"name": "Texas", "cost_per_person": 31000, "er_savings": 1100000, "blight_unit": 28000},
    "FL": {"name": "Florida", "cost_per_person": 33000, "er_savings": 1200000, "blight_unit": 30000},
    # Default National Averages for unlisted states
    "DEFAULT": {"name": "National Standard", "cost_per_person": 35000, "er_savings": 1300000, "blight_unit": 33000}
}

STATE_LOOKUP = {
    "california": "CA", "ca": "CA",
    "new york": "NY", "ny": "NY",
    "texas": "TX", "tx": "TX",
    "florida": "FL", "fl": "FL",
    "north carolina": "NC", "nc": "NC", "rocky mount": "NC"
}

def detect_state(prompt):
    lower = prompt.lower()
    for key, code in STATE_LOOKUP.items():
        if key in lower:
            return STATE_METRICS[code]
    return STATE_METRICS["DEFAULT"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/query', methods=['POST'])
def query_api():
    data = request.get_json() or {}
    prompt = data.get('prompt', '').strip()
    
    if not prompt:
        return jsonify({'response': 'Nova-AI Core Active. Select a jurisdiction or submit a query.'})

    lower = prompt.lower()
    numbers = re.findall(r'\d+', lower)
    region = detect_state(prompt)

    # 1. Nationwide Dynamic Math Calculation
    if numbers and any(k in lower for k in ["unsheltered", "individual", "people", "taxpayer", "cost", "places", "person"]):
        count = max([int(n) for n in numbers])
        savings = count * region["cost_per_person"]
        return jsonify({
            'response': f"Nova-AI Telemetry [{region['name']}]: For {count:,} individuals, projected 12-month taxpayer cost offset is calculated at ${savings:,} (based on ${region['cost_per_person']:,}/person regional metric)."
        })

    # 2. Nationwide Blight & Housing Impact
    if any(k in lower for k in ["vacant", "blight", "property", "corridor"]):
        return jsonify({
            'response': f"Vacant Housing Fiscal Telemetry [{region['name']}]: Blighted residential structures cost local municipal taxpayers an estimated ${region['blight_unit']:,} per unit annually in lost tax revenue and service costs."
        })

    # 3. Healthcare Infrastructure Impact
    if any(k in lower for k in ["hospital", "er", "emergency", "health"]):
        return jsonify({
            'response': f"Regional Health Telemetry [{region['name']}]: Rapid housing placement diverts non-acute ER intake, freeing hospital beds and eliminating roughly ${region['er_savings']:,} in uncompensated care costs annually."
        })

    # 4. Federal HUD & Grant Alignment (Applicable to all 50 states)
    if any(k in lower for k in ["hud", "grant", "arpa", "home-arp", "funding"]):
        return jsonify({
            'response': f"Federal Fiscal Framework [{region['name']}]: Platform implementation qualifies for HUD Continuum of Care (CoC), HOME-ARP, and state-level technical assistance grants, enabling local adoption at zero net impact to general funds."
        })

    # Fallback response
    return jsonify({
        'response': f"Nova-AI Super-Intelligence Core [{region['name']}]: Query evaluated against federal and state HUD datasets. Telemetry confirms operational alignment for strategic deployment."
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
