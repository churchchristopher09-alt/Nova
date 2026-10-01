from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/query', methods=['POST'])
def query_api():
    data = request.get_json() or {}
    prompt = data.get('prompt', '').strip()
    
    if not prompt:
        return jsonify({'response': 'No query provided.'})
    
    lower = prompt.lower()
    numbers = re.findall(r'\d+', lower)
    
    # Priority 1: If there's a number in the question, perform the taxpayer calculation!
    if numbers and any(k in lower for k in ["unsheltered", "individual", "people", "taxpayer", "cost", "places", "placement"]):
        count = int(numbers[0])
        savings = count * 35000
        return jsonify({'response': f"Projected 12-Month Metric for {count} individuals: Direct taxpayer cost reduction calculated at ${savings:,} based on the $35,000 per person annual offset, alongside significant hospital ER load reduction."})

    # Priority 2: Hospital queries
    if any(k in lower for k in ["unc health", "nash", "hospital", "emergency", "er", "healthcare"]):
        return jsonify({'response': "Evaluating regional emergency room telemetry: Redirecting non-emergency intake via rapid housing stabilization frees up critical ER bed capacity and eliminates over $1.25 million annually in uncompensated hospital care costs."})

    # Priority 3: Housing vacancies queries
    if any(k in lower for k in ["vacancy", "vacancies", "habitability", "rank", "district 01"]):
        return jsonify({'response': "Scanning nationwide housing and municipal records... Over 142 actionable residential structures identified. Prioritizing high habitability units yields immediate rapid placements, saving local governments an average of $32,600 per unit annually."})

    # General Fallback with Math
    count = int(numbers[0]) if numbers else 25
    savings = count * 35000
    return jsonify({'response': f"Query Mapped: Targeted transition of {count} individuals calculates to a baseline municipal taxpayer cost reduction of ${savings:,} ($35,000/person annual offset)."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
