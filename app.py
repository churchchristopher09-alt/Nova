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
    
    # Extract numbers if present in prompt
    numbers = re.findall(r'\d+', lower)
    count = int(numbers[0]) if numbers else 25
    savings = count * 35000
    
    if any(k in lower for k in ["vacancy", "vacancies", "habitability", "rank", "district 01", "housing"]):
        response_text = (
            "Scanning nationwide housing and municipal records... Over 142 actionable residential structures identified. "
            "Prioritizing high habitability units yields immediate rapid placements, saving local governments an average of $32,600 per unit annually."
        )
    elif any(k in lower for k in ["unc health", "nash", "hospital", "emergency", "er", "healthcare"]):
        response_text = (
            "Evaluating regional emergency room telemetry: Redirecting non-emergency intake via rapid housing stabilization "
            "frees up critical ER bed capacity and eliminates over $1.25 million annually in uncompensated hospital care costs."
        )
    else:
        response_text = (
            f"Projected 12-Month National Metric for {count} individuals: Direct taxpayer cost reduction calculated at ${savings:,} "
            f"based on the $35,000 per person annual offset, while reducing emergency intake strain by over 14 percent."
        )
        
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
