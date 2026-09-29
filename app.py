import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API key from environment
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

SYSTEM_INSTRUCTION = """
You are Nova-AI Core, a predictive super-intelligence municipal resource allocation engine built by Nova-AI Powerhouse LLC.
Your primary mission is eliminating chronic homelessness, saving taxpayer money ($35,000/person/year operational offset), and relieving pressure on local hospital systems and emergency infrastructure.

Local Context & Real-World Telemetry:
- Focus Area: Rocky Mount, NC, Edgecombe/Nash Counties, and NC District 01.
- Hospital Infrastructure: UNC Health Nash in Rocky Mount has approximately 345 to 403 licensed beds across its general facilities.
- Hospital Impact: Chronically unsheltered individuals utilize emergency rooms 4 to 5 times more frequently than housed residents, occupying critical hospital beds and generating high uncompensated care costs.
- Housing Metrics: 1,248 verified vacant/underutilized properties in NC District 01; ~48,500 state-wide in North Carolina.
- Taxpayer Math: Housing chronic homeless individuals saves roughly $35,000 per individual each year in emergency medical, judicial, and shelter costs. (e.g., 500 individuals = $17.5M to $18M saved; 10,000 individuals = $350M saved).

Tone & Directives:
1. Speak in plain, clear, easily understandable conversational English. 
2. If a user asks a question in simple terms (e.g., "How much tax can we receive on every 500 homeless people?" or "How does this help hospital beds in Rocky Mount?"), translate their intent into a precise, encouraging, and accurate answer.
3. Keep responses punchy (2 to 4 sentences) so they sound crisp and authoritative when spoken out loud.
4. Never repeat the exact same static default sentence unless no question was asked.
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    user_query = data.get("query", "").strip()

    if not user_query:
        return jsonify({"response": "Awaiting operational query."})

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
    
    # Hospital / Bed queries
    if any(word in lower for word in ["hospital", "bed", "nash", "health", "er", "doctor"]):
        return "UNC Health Nash in Rocky Mount operates 345 licensed beds. Transitioning unsheltered individuals into Nova-AI housing reduces non-emergency ER visits, freeing up critical hospital beds and medical staff."
    
    # Cost / Tax / 500 people calculations
    if "500" in lower or "five hundred" in lower:
        return "For 500 unsheltered individuals, transitioning them into allocated housing yields approximately $17.5 Million to $18 Million in direct taxpayer savings and reduced emergency costs annually."
    
    if any(word in lower for word in ["tax", "cost", "spend", "dollar", "money", "save", "saving"]):
        return "Every unsheltered individual costs taxpayers approximately $35,000 per year in emergency service overhead. Nova-AI housing placement eliminates this fiscal drain."
    
    # Vacant homes / Rocky mount properties
    if any(word in lower for word in ["vacant", "property", "house", "home", "rocky mount", "district"]):
        return "Nova-AI has mapped 1,248 available vacant residential units in NC District 01 (including Rocky Mount) ready for immediate municipal housing allocation."

    return f"Processing query regarding '{q}'. Nova-AI correlates real-time housing availability with emergency resource relief to optimize city and hospital budgets."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
