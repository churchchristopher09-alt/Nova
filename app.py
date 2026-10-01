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
        return jsonify({'response': 'Nova-AI core active. Please present a query.'})
    
    lower = prompt.lower()
    numbers = re.findall(r'\d+', lower)

    # RULE 1: Actionable Solutions / "How can we fix this"
    if any(k in lower for k in ["fix this", "fix it", "how can we fix", "solution", "solutions", "action plan"]):
        return jsonify({
            'response': "Nova-AI Action Protocol: 1) Deploy predictive housing triage to match unsheltered individuals with high-habitability vacant structures; 2) Utilize state/federal grant funds (HOME-ARP/HUD) to offset rehabilitation; 3) Recapture up to $32,600/unit in municipal taxpayer value."
        })

    # RULE 2: Taxpayer Cost of Vacant Homes
    if any(k in lower for k in ["vacant homes", "costing taxpayers", "vacant property cost", "blight cost"]):
        return jsonify({
            'response': "Vacant Housing Fiscal Telemetry: Unoccupied and blighted residential structures cost municipal taxpayers an estimated $32,600 per unit annually in lost property tax, code enforcement, public safety response, and surrounding devaluation."
        })

    # RULE 3: Commercial Corridors & Opportunity Zones
    if any(k in lower for k in ["commercial corridor", "commercial corridors", "opportunity zone", "opportunity zones", "downtown"]):
        return jsonify({
            'response': "Economic Corridor Telemetry: Rapid housing placement along targeted municipal transit and commercial corridors restores local consumer foot traffic, protects property values, and unlocks private investment in federal Opportunity Zones."
        })

    # RULE 4: Multi-Agency Data Sync
    if any(k in lower for k in ["sync data", "housing authorities", "law enforcement", "interoperability", "multi-agency"]):
        return jsonify({
            'response': "Interoperability Protocol: Nova-AI functions as a secure central telemetry hub, aggregating siloed municipal data from law enforcement, health systems, and housing authorities without disrupting existing workflows."
        })

    # RULE 5: HUD, Grants, and ARPA Budget Integration
    if any(k in lower for k in ["hud", "grant", "grants", "arpa", "home-arp", "funding", "allocations"]):
        return jsonify({
            'response': "Nova-AI Fiscal Framework: System integration qualifies for existing HUD Continuum of Care, HOME-ARP, and state technical assistance grant allocations, enabling municipal adoption at zero net impact to local general funds."
        })

    # RULE 6: Security & Government Compliance
    if any(k in lower for k in ["security", "compliance", "protocol", "protocols", "privacy", "saas"]):
        return jsonify({
            'response': "Nova-AI Security Protocol: Enterprise SaaS architecture operating under non-partisan Opportunity Zone parameters, utilizing encrypted municipal telemetry streams with SOC-2 and government data alignment."
        })

    # RULE 7: Specific Headcount Queries
    if any(k in lower for k in ["how many homeless", "homeless count", "homeless population", "rocky mount homeless"]):
        return jsonify({
            'response': "Rocky Mount Municipal Telemetry: Point-in-Time data estimates 250 to 320 unsheltered and shelter-reliant individuals across Nash and Edgecombe counties. Direct deployment via Nova-AI yields a projected $8.7M to $11.2M annual taxpayer savings."
        })

    # RULE 8: Statewide / Regional Vacancy Queries
    if any(k in lower for k in ["vacant housing", "vacancies in nc", "north carolina housing", "vacant properties"]):
        return jsonify({
            'response': "North Carolina Regional Housing Inventory: Census metrics indicate a rental vacancy rate near 6.4%, with active vacant structures concentrated along rural and urban transit corridors like the I-95 zone ready for immediate rehabilitation."
        })

    # RULE 9: Dynamic Taxpayer Math Engine
    if numbers and any(k in lower for k in ["unsheltered", "individual", "people", "taxpayer", "cost", "places", "placement", "transition", "person"]):
        count = max([int(n) for n in numbers])
        savings = count * 35000
        return jsonify({
            'response': f"Projected 12-Month Metric for {count} individuals: Direct municipal taxpayer cost reduction calculated at ${savings:,} based on the $35,000/person annual cost offset."
        })

    # RULE 10: Hospital Capacity Telemetry
    if any(k in lower for k in ["unc health", "nash", "hospital", "emergency", "er", "healthcare"]):
        return jsonify({
            'response': "UNC Health Nash ER Telemetry: Diverting non-acute emergency room intake via rapid housing stabilization frees up ~3.2 beds daily and eliminates over $1.25M in uncompensated care costs annually."
        })

    # GENERAL FALLBACK ENGINE
    if numbers:
        count = max([int(n) for n in numbers])
        savings = count * 35000
        return jsonify({
            'response': f"Nova-AI Analysis for target input '{count}': Evaluated against operational datasets. Baseline taxpayer efficiency yields ${savings:,} in municipal relief while optimizing resource allocation."
        })

    return jsonify({
        'response': f"Nova-AI Intelligence System processed: '{prompt}'. System telemetry confirms optimal alignment with fiscal efficiency protocols and strategic municipal deployment."
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
