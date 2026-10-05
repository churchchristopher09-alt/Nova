import os
import time
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Google Gemini API Key from environment variable
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# Fallback answers for key municipal pitch questions to prevent rate-limit failures during live demos
DEMO_FALLBACKS = {
    "er": (
        "Nova-AI Core: Housing chronically homeless individuals removes them from high-frequency "
        "emergency room visits, EMS dispatches, and police interventions. At an average cost of $35,000 "
        "per unhoused person annually, transitioning individuals into supportive housing yields up to 70% "
        "reduction in emergency overhead, generating over $1.2M in net municipal savings."
    ),
    "property": (
        "Nova-AI Core: The city can target tax-foreclosed and blighted properties currently held on "
        "municipal tax rolls or in land bank inventories at nominal costs ($1,000–$5,000 per parcel). "
        "Acquisition and rehabilitation can be funded using federal HUD Community Development Block Grants (CDBG) "
        "and HOME Investment Program funds."
    ),
    "workforce": (
        "Nova-AI Core: Nova-AI utilizes a structured role-matching framework. Candidates with non-violent "
        "pasts handle on-site maintenance and property security. Candidates with restricted backgrounds are "
        "routed to off-site logistics and central hardware operations, qualifying the program for Federal "
        "Work Opportunity Tax Credits (WOTC)."
    )
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def query():
    user_input = request.json.get("prompt", "").strip()
    if not user_input:
        return jsonify({"response": "Nova-AI Core: Please enter a valid prompt or directive."})

    # System instruction context for Nova-AI Engine
    system_instruction = (
        "You are Nova-AI Core, an advanced municipal resource allocation engine designed for city officials. "
        "Provide professional, data-driven answers focusing on housing homeless individuals, reducing emergency "
        "service costs, utilizing tax-foreclosed properties, and leveraging second-chance workforce programs."
    )

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        full_prompt = f"{system_instruction}\n\nUser Question: {user_input}"
        response = model.generate_content(full_prompt)
        return jsonify({"response": response.text})

    except Exception as e:
        error_str = str(e)
        
        # Clean handling for 429 Rate Limit / Quota Exhaustion
        if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
            lower_input = user_input.lower()
            
            # Check if query matches core demo topics to serve instant clean fallback
            if "emergency" in lower_input or "er" in lower_input or "budget" in lower_input or "cost" in lower_input:
                return jsonify({"response": DEMO_FALLBACKS["er"]})
            elif "vacant" in lower_input or "property" in lower_input or "house" in lower_input or "land" in lower_input:
                return jsonify({"response": DEMO_FALLBACKS["property"]})
            elif "workforce" in lower_input or "felon" in lower_input or "convict" in lower_input or "security" in lower_input:
                return jsonify({"response": DEMO_FALLBACKS["workforce"]})
            else:
                return jsonify({
                    "response": (
                        "Nova-AI Core: High-volume query traffic detected on Free Tier. "
                        "System capacity throttled by Google Cloud API limits. "
                        "Phase 1 Pilot ($20,000) unlocks dedicated Enterprise API servers with zero rate limits."
                    )
                })

        return jsonify({"response": f"Nova-AI System Note: {error_str}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
