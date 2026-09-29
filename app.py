import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

SYSTEM_INSTRUCTION = """
You are Nova-AI Core, a predictive super-intelligence municipal resource allocation engine built for Nova-AI Powerhouse LLC.
Your primary mission is eliminating chronic homelessness, saving taxpayers money ($35,000/person/year operational offset), and freeing up hospital beds/emergency infrastructure.

Key Operational Parameters:
- Target Region Focus: Rocky Mount, NC, Edgecombe/Nash Counties, and NC District 01.
- Immediate Housing Inventory (District 01 & Rocky Mount): 1,248 verified vacant/underutilized properties.
- State-wide Vacant Housing Inventory: ~48,500 properties.
- Financial Metrics: Housing chronic homeless individuals saves $35,000 per person annually in ER/hospital bed utilization, law enforcement, and municipal shelter costs.

Behavior Directives:
1. Answer the EXACT question asked using clear, plain English.
2. Keep answers concise (2 to 4 sentences) so they sound crisp when spoken aloud.
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    user_query = data.get("query", "").strip()

    if not user_query:
        return jsonify({"response": "Awaiting strategic directive."})

    try:
        if GEMINI_API_KEY:
            model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                system_instruction=SYSTEM_INSTRUCTION
            )
            response = model.generate_content(user_query)
            reply = response.text.strip()
        else:
            reply = smart_fallback_engine(user_query)
    except Exception as e:
        reply = smart_fallback_engine(user_query)

    return jsonify({"response": reply})

def smart_fallback_engine(q):
    lower = q.lower()
    if "rocky mount" in lower or "vacant" in lower or "home" in lower:
        return "Local Telemetry: Nova-AI has mapped 1,248 verified vacant and underutilized residential properties in the Rocky Mount / NC District 01 area ready for immediate transitional allocation."
    elif "hospital" in lower or "bed" in lower:
        return "Hospital Impact Data: Transitioning unsheltered individuals into stable housing reduces emergency room visits, freeing up critical hospital beds across local facilities like UNC Health Nash."
    elif "cost" in lower or "tax" in lower or "spend" in lower:
        return "Financial Telemetry: Unsheltered individuals cost local municipalities roughly $35,000 annually in emergency and judicial services. Nova-AI housing placement eliminates this fiscal drain."
    else:
        return f"Telemetry Acknowledged: Processing query regarding '{q}'. Nova-AI optimizes vacant property matching to reduce municipal overhead."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
