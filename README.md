🧪 Quantum Superposition Explorer
Overview

The Quantum Superposition Explorer is an interactive web application that allows users to explore and visualize the concept of quantum superposition using Qiskit, Python, and Flask.

This app demonstrates how a single qubit transitions from a classical state → superposition → another classical state by rotating the qubit with a parameter θ. Users can input any angle and instantly see:

Probabilities of measuring |0⟩ and |1⟩

The type of superposition (weak, maximum, or classical)

A live quantum circuit diagram

A dynamically generated probability plot

The frontend is sleek, dark-themed, and gold-accented, with spinning quantum “galaxy” rings for a visually appealing effect.

🔬 Concept

Quantum mechanics allows qubits to exist in superposition — a linear combination of the classical |0⟩ and |1⟩ states:

∣
𝜓
⟩
=
𝛼
∣
0
⟩
+
𝛽
∣
1
⟩
,
with 
∣
𝛼
∣
2
+
∣
𝛽
∣
2
=
1
∣ψ⟩=α∣0⟩+β∣1⟩,with ∣α∣
2
+∣β∣
2
=1

Using the Ry(θ) rotation gate, a single qubit is rotated on the Bloch sphere:

θ (degrees)	State Description
0	Classical
45	Weak Superposition
90	Maximum Superposition
180	Classical

The user can observe how measurement probabilities change continuously as θ varies.

💻 Features

Interactive θ slider: Adjust rotation angle from 0°–180°

Live probability calculation: Shows P(|0⟩) and P(|1⟩)

Superposition type display: Weak, Maximum, or Classical

Quantum circuit diagram: Shows Ry gate applied to the qubit

Probability plot: Generated dynamically with Matplotlib

Responsive, sleek dark + gold theme with spinning background rings

Full Flask backend → frontend integration

🛠️ Tech Stack

Backend: Python, Flask

Quantum simulation: Qiskit (Aer simulator)

Plotting: Matplotlib

Frontend: HTML, CSS, JavaScript

Visualization: Jinja2 templates, dynamic plot images
