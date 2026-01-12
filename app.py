import streamlit as st
import matplotlib.pyplot as plt
import random


st.set_page_config(
    page_title="Quantum Coin Flip Simulator",
    page_icon="🪙",

)


st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #667eea, #764ba2);
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        color: white;
    }

    h1, h2, h3, p {
        color: white;
        text-align: center;
    }

    .stButton button {
        background: rgba(255, 255, 255, 0.25);
        color: white;
        border-radius: 12px;
        padding: 10px 20px;
        border: none;
        font-size: 16px;
        transition: 0.3s;
    }

    .stButton button:hover {
        background: rgba(255, 255, 255, 0.4);
    }

    .stSlider > div {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def quantum_coin_flip(shots=1000):
    
    counts = {'0': 0, '1': 0}
    for _ in range(shots):
        outcome = random.choice(['0', '1'])
        counts[outcome] += 1
    return counts

st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

st.title("🪙 Quantum Coin Flip Simulator")
st.write("Simulate a quantum coin flip using superposition (50/50 probability).")
st.write("Fully compatible with **Python 3.12** — no Qiskit or Aer required.")

shots = st.slider(
    "Number of Flips",
    min_value=100,
    max_value=5000,
    value=1000,
    step=100
)

if st.button("🔄 Flip Coin"):
    counts = quantum_coin_flip(shots)

    st.subheader("📊 Measurement Results")
    st.write(f"**Heads (0):** {counts['0']}")
    st.write(f"**Tails (1):** {counts['1']}")

    fig, ax = plt.subplots()
    ax.bar(counts.keys(), counts.values())
    ax.set_xlabel("Outcome")
    ax.set_ylabel("Count")
    ax.set_title("Quantum Coin Flip Results")

    st.pyplot(fig)

st.markdown("</div>", unsafe_allow_html=True)