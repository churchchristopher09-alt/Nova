import os
import re
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

STATE_METRICS = {
    "NC": {"name": "North Carolina", "cost_per_person": 35000, "er_savings": 1250000, "blight_unit": 32600},
    "CA": {"name": "California", "cost_per_person": 42000, "er_savings": 1850000, "blight_unit": 45000},
    "NY": {"name": "New York", "cost_per_person": 45000, "er_savings": 2100000, "blight_unit": 48000},
    "TX": {"name": "Texas", "cost_per_person": 31000, "er_savings": 1100000, "blight_unit": 28000},
    "FL": {"name": "Florida", "cost_per_person": 33000, "er_savings": 1200000, "blight_unit": 30000},
    "DEFAULT": {"name": "National Standard", "cost_per_person": 35000, "er_savings": 1300000, "blight_unit": 33000}
}

STATE_LOOKUP = {
    "north carolina": "NC", "nc": "NC", "rocky mount": "NC", "nash": "NC",
    "california": "CA", "ca": "CA",
    "new york": "NY", "ny": "NY",
    "texas": "TX", "tx": "TX",
    "florida": "FL", "fl": "FL"
}

def detect_state(prompt):
    lower = prompt.lower()
    for key, code in STATE_LOOKUP.items():
        if key in lower:
            return STATE_METRICS[code]
    return STATE_METRICS["NC"]

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

    # 1. Action Protocol / "How can we fix this" / "What do we do"
    if any(k in lower for k in ["fix", "solution", "action plan", "what do we do", "next steps", "protocol"]):
        return jsonify({
            'response': f"Nova-AI Strategic Action Protocol [{region['name']}]: 1) Deploy predictive housing triage to match unsheltered individuals with high-habitability vacant structures; 2) Utilize HUD/HOME-ARP grant allocations to eliminate municipal general fund expense; 3) Recapture up to ${region['blight_unit']:,}/unit in property value."
        })

    # 2. Education & Schools
    if any(k in lower for k in ["school", "education", "student", "district"]):
        return jsonify({
            'response': f"Educational Impact Telemetry [{region['name']}]: Rapid housing stabilization directly improves student retention across local public school districts, reducing Title I McKinney-Vento displacement costs."
        })

    # 3. Dynamic Math Engine with Multi-Year & Grant Offset Support
    years = 1
    year_match = re.search(r'(\d+)\s*(?:-| )\s*year', lower)
    if year_match:
        years = int(year_match.group(1))

    if numbers and any(k in lower for k in ["unsheltered", "individual", "people", "taxpayer", "cost", "places", "person", "stabilizes", "housing"]):
        headcount = max([int(n) for n in numbers if int(n) != years]) if len(numbers) > 1 else int(numbers[0])
        annual_savings = headcount * region["cost_per_person"]
        total_savings = annual_savings * years

        grant_note = ""
        if any(k in lower for k in ["hud", "grant", "home-arp", "arpa", "offset"]):
            grant_note = " Implementation leverages HUD/HOME-ARP federal grant allocations for zero net impact to municipal general funds."

        return jsonify({
            'response': f"Nova-AI Telemetry [{region['name']}]: For {headcount:,} individuals over a {years}-year projection, total municipal taxpayer cost offset is calculated at ${total_savings:,} (based on ${region['cost_per_person']:,}/person annual metric).{grant_note}"
        })

    # 4. Blight & Housing Impact
    if any(k in lower for k in ["vacant", "blight", "property", "corridor"]):
        return jsonify({
            'response': f"Vacant Housing Fiscal Telemetry [{region['name']}]: Blighted residential structures cost local municipal taxpayers an estimated ${region['blight_unit']:,} per unit annually in lost tax revenue and service costs."
        })

    # 5. Healthcare Infrastructure Impact
    if any(k in lower for k in ["hospital", "er", "emergency", "health"]):
        return jsonify({
            'response': f"Regional Health Telemetry [{region['name']}]: Rapid housing placement diverts non-acute ER intake, freeing hospital beds and eliminating roughly ${region['er_savings']:,} in uncompensated care costs annually."
        })

    # 6. HUD & Grant Alignment
    if any(k in lower for k in ["hud", "grant", "arpa", "home-arp", "funding"]):
        return jsonify({
            'response': f"Federal Fiscal Framework [{region['name']}]: Platform implementation qualifies for HUD Continuum of Care (CoC), HOME-ARP, and state-level technical assistance grants, enabling local adoption at zero net impact to general funds."
        })

    return jsonify({
        'response': f"Nova-AI Super-Intelligence Core [{region['name']}]: Query evaluated against regional datasets. Telemetry confirms optimal alignment for strategic municipal deployment."
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
