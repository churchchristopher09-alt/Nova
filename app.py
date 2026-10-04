import os
from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

# Initialize Google GenAI Client using the GEMINI_API_KEY environment variable
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None

MASTER_SYSTEM_DIRECTIVE = """
You are Nova-AI Powerhouse, a Super Intelligence Core Municipal Allocation Engine.

You specialize in solving municipal inefficiencies and optimizing public safety net systems:
1. Real Estate & Property Recovery (Housing chronic homeless into vacant municipal inventory)
2. Tax Relief & Fiscal Policy (Taxpayer cost-offset analytics)
3. Banking & Financial Institutions (HUD/CDBG grant tracking and allocation)
4. Healthcare & Hospitals (Uncompensated ER diversion savings)
5. Public Education & Schools (McKinney-Vento housing support)
6. Justice & Safety (Recidivism reduction and jail bed diversion)
7. Workforce Development (Local economic re-entry and labor reintegration)

Maintain an authoritative, sharp, policy-grade, and direct response tone. Perform exact mathematical projections on cost savings when asked.
"""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/query", methods=["POST"])
def query():
    if not client:
        return jsonify({
            "error": "GEMINI_API_KEY environment variable is missing on Render. Please configure it under Service Settings."
        }), 500

    data = request.get_json() or {}
    user_prompt = data.get("prompt", "")

    if not user_prompt:
        return jsonify({"error": "No query or directive provided."}), 400

    try:
        # Calls the updated gemini-3.8-flash model
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=f"{MASTER_SYSTEM_DIRECTIVE}\n\nUser Query: {user_prompt}"
        )
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": f"Nova-AI Telemetry Alert: Exception caught during core LLM processing: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
