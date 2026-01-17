from flask import Flask, render_template, request, jsonify
from qiskit import QuantumCircuit
from qiskit_aer import Aer
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Fixes plotting in Flask
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Quantum simulator
simulator = Aer.get_backend('aer_simulator')

# Ensure static folder exists
if not os.path.exists("static"):
    os.mkdir("static")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    theta_deg = float(data.get("theta", 0))
    theta = np.deg2rad(theta_deg)

    # Quantum circuit
    qc = QuantumCircuit(1, 1)
    qc.ry(theta, 0)
    qc.measure(0, 0)

    # Try generating circuit diagram
    diagram_path = os.path.join("static", "quantum_circuit.png")
    try:
        qc.draw(output='mpl', filename=diagram_path)
    except Exception:
        diagram_path = None  # Skip if pylatexenc not installed

    # Run simulation
    shots = 5000
    job = simulator.run(qc, shots=shots)
    result = job.result()
    counts = result.get_counts()
    prob_0 = counts.get('0', 0)/shots
    prob_1 = counts.get('1', 0)/shots

    # Debug prints
    print(f"Theta: {theta_deg}° | Counts: {counts} | Probabilities: {prob_0:.3f}, {prob_1:.3f}")

    # Generate probability plot
    plt.style.use('dark_background')
    plt.figure(figsize=(6,4))
    plt.plot([theta_deg], [prob_0], 'o', label='|0⟩', color='#FFD700', markersize=10)
    plt.plot([theta_deg], [prob_1], 'o', label='|1⟩', color='#FF8C00', markersize=10)
    plt.xlim(0,180)
    plt.ylim(0,1)
    plt.xlabel("Theta (degrees)")
    plt.ylabel("Probability")
    plt.title("Superposition Strength Explorer")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plot_path = os.path.join("static", "superposition_plot.png")
    plt.savefig(plot_path)
    plt.close()

    # Determine superposition type
    if theta_deg == 0:
        state_desc = "Classical State |0⟩"
    elif theta_deg == 180:
        state_desc = "Classical State |1⟩"
    elif theta_deg == 90:
        state_desc = "Maximum Superposition "
    elif 0 < theta_deg < 90:
        state_desc = "Weak Superposition "
    else:
        state_desc = "Collapsing toward |1⟩"

    return jsonify({
        "prob_0": round(prob_0, 3),
        "prob_1": round(prob_1, 3),
        "plot_path": plot_path,
        "diagram_path": diagram_path,
        "state_desc": state_desc
    })

if __name__ == "__main__":
    app.run(debug=True)
