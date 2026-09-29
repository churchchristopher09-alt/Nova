import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API key from environment variable
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

SYSTEM_INSTRUCTION = """
You are Nova-AI Core, a predictive super-intelligence municipal resource allocation engine built for Nova-AI Powerhouse LLC.
Your primary mission is eliminating chronic homelessness, saving taxpayers money ($35,000/person/year operational offset), and freeing up hospital beds/emergency infrastructure.

Key Operational Parameters:
- Target Region Focus: Rocky Mount, NC, Edgecombe/Nash Counties, and NC District 01.
- Immediate Housing Inventory (District 01): 1,248 verified vacant/underutilized properties.
- State-wide Vacant Housing Inventory: ~48,500 properties.
- Financial Metrics: Housing chronic homeless individuals saves $35,000 per person annually in ER/hospital bed utilization, law enforcement, and municipal shelter costs. 10,000 individuals housed = $350 Million in annual taxpayer savings.

Behavior Directives:
1. Speak in plain, clear, easily understandable language for any user (civilian or official).
2. Answer the EXACT question asked (whether about hospital beds, tax dollars, or local economic impact).
3. Always maintain a confident, authoritative, tactical, and helpful tone.
4. Keep answers concise (2 to 4 sentences) so they sound crisp when spoken aloud.
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
            # Fallback dynamic calculation if API key isn't attached yet
            reply = fallback_tactical_engine(user_query)
    except Exception as e:
        reply = fallback_tactical_engine(user_query)

    return jsonify({"response": reply})

def fallback_tactical_engine(q):
    lower = q.toLowerCase() if hasattr(q, 'toLowerCase') else q.lower()
    if "hospital" in lower or "bed" in lower:
        return "Hospital Impact Data: Unsheltered individuals average 4 to 5 emergency room visits annually, heavily cluttering local hospital beds in Rocky Mount and statewide. Nova-AI allocation frees critical medical beds by placing individuals into stable housing."
    elif "cost" in lower or "spend" in lower or "dollar" in lower or "tax" in lower:
        return "Financial Telemetry: Unhoused individuals cost local taxpayers approximately $35,000 annually in emergency room visits, shelter management, and civic services. Nova-AI directly offsets this expense."
    else:
        return f"Telemetry Acknowledged: Processing query regarding '{q}'. Nova-AI optimizes vacant property matching to reduce municipal overhead and stabilize housing."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
