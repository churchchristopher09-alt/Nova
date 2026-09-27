import os
import sys
import subprocess

# Auto-install missing packages on startup
try:
    import flask
    import gunicorn
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "flask", "gunicorn"])

from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder="templates")

# =====================================================================
# NOVA-AI POWERHOUSE: CORE CALCULATION ENGINE (CPU OPTIMIZED)
# =====================================================================

COST_PER_ER_VISIT = 1500  # Average emergency room visit cost
COST_PER_JAIL_DAY = 125   # Average county jail daily bed cost
ANNUAL_UNHOUSED_COST = 35000  # Total estimated yearly public cost offset per person

def calculate_municipal_savings(people_housed):
    total_savings = people_housed * ANNUAL_UNHOUSED_COST
    er_savings = people_housed * (COST_PER_ER_VISIT * 4)  
    jail_savings = people_housed * (COST_PER_JAIL_DAY * 60) 
    
    return {
        "people_housed": people_housed,
        "total_annual_savings": f"${total_savings:,.2f}",
        "er_cost_reduction": f"${er_savings:,.2f}",
        "jail_cost_reduction": f"${jail_savings:,.2f}"
    }

# =====================================================================
# FLASK WEB ROUTES
# =====================================================================

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json() or {}
    unhoused_count = int(data.get("unhoused_count", 100))
    metrics = calculate_municipal_savings(unhoused_count)
    
    return jsonify({
        "status": "success",
        "system": "Nova-AI Powerhouse Core Engine (CPU Mode)",
        "metrics": metrics,
        "summary": (
            f"Transitioning {unhoused_count} individuals into permanent housing "
            f"yields an estimated {metrics['total_annual_savings']} in total municipal savings, "
            f"reducing local emergency department strain by {metrics['er_cost_reduction']} "
            f"and county corrections expenditure by {metrics['jail_cost_reduction']} annually."
        )
    })


@app.route("/api/generate_report", methods=["POST"])
def generate_report():
    data = request.get_json() or {}
    region = data.get("region", "Eastern North Carolina")
    target_count = int(data.get("target_count", 50))
    metrics = calculate_municipal_savings(target_count)
    
    executive_script = (
        f"EXECUTIVE BRIEFING: NOVA-AI DEPLOYMENT FOR {region.upper()}\n"
        f"---------------------------------------------------\n"
        f"Target Population Transition: {target_count} individuals\n"
        f"Projected Annual Taxpayer Offset: {metrics['total_annual_savings']}\n"
        f"- Healthcare (ER) Savings: {metrics['er_cost_reduction']}\n"
        f"- Corrections (Jail) Savings: {metrics['jail_cost_reduction']}\n\n"
        f"Strategic Impact: Nova-AI matches existing vacant regional housing "
        f"with high-utilization individuals, directly relieving budgetary pressure "
        f"on municipal services while establishing stable housing pathways."
    )
    
    return jsonify({
        "status": "success",
        "region": region,
        "briefing": executive_script
    })

# =====================================================================
# SYSTEM LAUNCH
# =====================================================================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    print(f"Starting Nova-AI Powerhouse [CPU Mode] on http://0.0.0.0:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)
