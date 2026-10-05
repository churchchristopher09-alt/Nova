import os
import time
from flask import Flask, request, jsonify
from google import genai
from google.genai import types

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nova-AI Powerhouse</title>
    <style>
        body { background-color: #0b0f19; color: #00ff9d; font-family: 'Courier New', monospace; padding: 20px; margin: 0; }
        .header { text-align: center; border-bottom: 2px solid #00ff9d; padding-bottom: 10px; margin-bottom: 20px; }
        .stats-grid { display: flex; justify-content: space-around; background: #111827; padding: 15px; border-radius: 8px; border: 1px solid #1f2937; margin-bottom: 20px; }
        .stat-box { text-align: center; }
        .stat-val { font-size: 1.4rem; font-weight: bold; color: #ffffff; }
        .console { background: #030712; border: 1px solid #1f2937; border-radius: 8px; padding: 15px; height: 350px; overflow-y: auto; white-space: pre-wrap; color: #a7f3d0; margin-bottom: 15px; }
        .input-group { display: flex; gap: 10px; }
        input { flex: 1; background: #111827; border: 1px solid #374151; color: #ffffff; padding: 12px; border-radius: 6px; font-family: monospace; }
        button { background: #2563eb; color: white; border: none; padding: 12px 24px; border-radius: 6px; cursor: pointer; font-weight: bold; }
        button:hover { background: #1d4ed8; }
    </style>
</head>
<body>
    <div class="header">
        <span style="background: #065f46; color: #34d399; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem;">AI PREDICTIVE CORE ACTIVE</span>
        <h1 style="margin: 10px 0 5px 0;">Nova-AI Powerhouse</h1>
        <div style="color: #9ca3af; font-size: 0.85rem;">SUPER INTELLIGENCE CORE MUNICIPAL ALLOCATION ENGINE</div>
    </div>

    <div class="stats-grid">
        <div class="stat-box"><div style="font-size:0.75rem; color:#9ca3af;">HOUSING AVAILABLE</div><div class="stat-val">1,248</div></div>
        <div class="stat-box"><div style="font-size:0.75rem; color:#9ca3af;">TAXPAYER SAVINGS</div><div class="stat-val">$350M+</div></div>
        <div class="stat-box"><div style="font-size:0.75rem; color:#9ca3af;">EFFICIENCY RATE</div><div class="stat-val">99.4%</div></div>
    </div>

    <div id="console" class="console">Nova-AI Core: Intelligence system active. Ask any question or issue any directive.</div>

    <div class="input-group">
        <input type="text" id="queryInput" placeholder="Enter query or directive..." onkeydown="if(event.key==='Enter') sendQuery()">
        <button onclick="sendQuery()">Execute</button>
    </div>

    <script>
        function speakText(text) {
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
                const cleanText = text.replace(/[*#$`\\_]/g, '');
                const utterance = new SpeechSynthesisUtterance(cleanText);
                utterance.rate = 0.95;
                window.speechSynthesis.speak(utterance);
            }
        }

        async function sendQuery() {
            const input = document.getElementById("queryInput");
            const consoleBox = document.getElementById("console");
            const prompt = input.value.trim();
            if (!prompt) return;

            consoleBox.innerText += `\\n\\nUser: ${prompt}`;
            input.value = "";
            consoleBox.scrollTop = consoleBox.scrollHeight;

            try {
                const response = await fetch("/api/query", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ prompt: prompt })
                });
                const data = await response.json();
                if (data.error) {
                    consoleBox.innerText += `\\n\\nNova-AI Core: ${data.error}`;
                } else {
                    consoleBox.innerText += `\\n\\nNova-AI Core: ${data.response}`;
                    speakText(data.response);
                }
            } catch (err) {
                consoleBox.innerText += `\\n\\nNova-AI Core: Connection error encountered.`;
            }
            consoleBox.scrollTop = consoleBox.scrollHeight;
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return HTML_TEMPLATE

@app.route("/api/query", methods=["POST"])
def query():
    try:
        data = request.get_json()
        user_prompt = data.get("prompt", "")
        
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            return jsonify({"error": "GEMINI_API_KEY environment variable missing."}), 500

        client = genai.Client(api_key=api_key)
        
        config = types.GenerateContentConfig(
            system_instruction=(
                "You are Nova-AI, an intelligent assistant and municipal predictive core. "
                "Answer all user inquiries accurately, clearly, and concisely, whether they pertain to general questions, "
                "complex topics, or municipal resource allocation and policy analysis."
            )
        )
        
        # Retry loop for handling temporary 503 high demand periods
        models_to_try = ["gemini-3.8-flash", "gemini-3.8-flash"]
        
        for model_name in models_to_try:
            for attempt in range(2):
                try:
                    response = client.models.generate_content(
                        model=model_name,
                        contents=user_prompt,
                        config=config
                    )
                    return jsonify({"response": response.text})
                except Exception as inner_e:
                    if "503" in str(inner_e) or "UNAVAILABLE" in str(inner_e):
                        time.sleep(1)  # Brief pause before retrying
                        continue
                    else:
                        raise inner_e

        return jsonify({"error": "Google AI servers are currently experiencing high traffic. Please tap Execute again in a moment."}), 503

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
