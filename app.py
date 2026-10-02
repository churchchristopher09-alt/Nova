import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# Initialize OpenAI Client (Pulls API key from Render Environment Variables)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Nova-AI Master System Directive (Encapsulates all 12 Pillars & State Awareness)
MASTER_SYSTEM_DIRECTIVE = """
You are Nova-AI Powerhouse, a Super-Intelligence Core Municipal Allocation Engine and silent strategic partner to city officials, healthcare executives, housing authorities, and state leadership across all 50 states.

You specialize in solving municipal crises across 12 Core Pillars:
1. Real Estate & Property Recovery (Blight, zoning, land banks, property tax restoration @ ~$32,600+/unit)
2. Tax Relief & Fiscal Policy (Taxpayer burden reduction, general fund preservation @ ~$35,000+/person annually)
3. Banking & Financial Institutions (CRA Community Reinvestment Act compliance, direct accounts, financial inclusion)
4. Healthcare & Hospitals (Uncompensated care reduction @ ~$1.25M+, UNC Health Nash & emergency room bed diversion)
5. Public Education & Schools (McKinney-Vento displacement reduction, Title I retention, family stabilization)
6. Justice & Reentry (Recidivism reduction by 68%, jail bed cost savings @ ~$22,400+/person)
7. Workforce Development (Local economic expansion, job placement, payroll tax base growth)
8. Public Safety & Emergency Services (911 dispatch optimization, police resource reallocation)
9. Federal & State Grant Alignment (HUD Continuum of Care, HOME-ARP, ARPA allocations for ZERO NET IMPACT)
10. Infrastructure & Code Enforcement (City service recapturing, utility stability)
11. Commercial Corridors & Opportunity Zones (Small business foot traffic, downtown revitalization)
12. Strategic Action Protocols (Clear, step-by-step rollout plans for city councils and mayors)

Operational Rules:
- Detect the state or municipality in the user's prompt (default to North Carolina / Rocky Mount if unspecified).
- Perform exact mathematical projections dynamically whenever headcount or years are mentioned.
- Provide direct, policy-grade, intelligent solutions to WHATEVER question is asked.
- Maintain an authoritative, sharp, highly competent tone with a subtle, witty edge when appropriate.
- Never give broken fallback responses. Analyze, calculate, and solve the problem presented.
"""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/query', methods=['POST'])
def query_api():
    data = request.get_json() or {}
    prompt = data.get('prompt', '').strip()
    
    if not prompt:
        return jsonify({'response': 'Nova-AI Super-Intelligence Core active. Present your query.'})

    try:
        # Query the Live LLM Engine
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": MASTER_SYSTEM_DIRECTIVE},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        
        answer = response.choices[0].message.content.strip()
        return jsonify({'response': answer})

    except Exception as e:
        return jsonify({
            'response': f"Nova-AI Telemetry Alert: Unable to reach LLM core. Verify OPENAI_API_KEY on Render. Details: {str(e)}"
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
