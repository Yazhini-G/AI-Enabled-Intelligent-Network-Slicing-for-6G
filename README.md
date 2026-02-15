# 🛰️ AI-Enabled-Intelligent-Network-Slicing-for-6G
Digital Twin & Explainable AI Framework for Next-Gen Networks
AI-Enabled-Intelligent-Network-Slicing-for-6G is an advanced network management platform designed to automate, monitor, and optimize 6G network slices. By integrating Digital Twinning and Explainable AI (XAI), the platform provides predictive isolation and transparent resource allocation for mission-critical applications.

---
## 🌍 Problem Statement

Legacy 5G network slicing faces significant challenges in the 6G era:

- Static Resource Allocation: Difficulty handling dynamic, ultra-low latency demands.

- Network Jitter: Significant performance drops during concurrent service requests.

- Black Box Decisions: Lack of transparency in how AI allocates critical resources.

- Manual Intervention: Slow response times to physical network changes.

---

## 🚀 Key Features🛡️

- 🛡️ Predictive Slice Isolation: Uses AI to maintain stable latencies ($0.5\text{--}0.6 \text{ ms}$) even under high network load.
- 🧠 Explainable AI (XAI) Dashboard: Provides real-time "Global Decision Weights" to justify resource priority.
- 👯 Digital Twin Synchronization: A virtual mirror that simulates physical network congestion and predicts potential SLA violations.
- ⚡ Orthogonal Slicing: Automated priority queuing using packet headers to ensure a $0.2 \text{ ms}$ advantage for critical services.
- 📊 Live Benchmarking: Real-time comparison between Legacy 5G Jitter and 6G AI-Native stability.

---

## 🧠 Technologies Used

### Frontend & Visualization * Streamlit: Interactive web-based command center.
- Plotly/Graph Objects: High-fidelity real-time data visualization.

### Backend & Simulation * Python 3.9+: Core logic and data processing.
- NumPy/Pandas: Digital Twin mathematical modeling and performance analytics

### Network Concepts * mURLLC / eMBB / umMTC: 6G service class modeling.

- Edge Cloud Computing: Geographical resource splitting for independent SLAs.

- Sub-6GHz & THz Bands: Frequency-aware spectrum allocation.  

---

## 🏗️ System Architecture

<img width="807" height="952" alt="Gemini_Generated_Image_g0g4qng0g4qng0g4" src="https://github.com/user-attachments/assets/e5f55b62-1eae-40c4-9d32-f9411ffd2474" />

1. Digital Twin Layer: Monitors real-time network load and simulates "what-if" scenarios.

2. AI Orchestrator: Evaluates service requests and selects the optimal slice (e.g., Slice 1 for Remote Surgery).

3. XAI Engine: Generates transparency reports on feature importance (Latency vs. Reliability).

4. Execution Layer: Deploys resources as Hardware-Locked or Software-Defined slices.


---

## 🎯 Objectives

- Achieve sub-1ms latency for mission-critical mURLLC services.

- Provide 100% transparency in AI decision-making via XAI.

- Reduce network jitter by 90% compared to legacy 5G static slicing.
---

## 🌱 Sustainable Development Goals (SDGs)

This project aligns with:

- SDG 9 – Industry, Innovation, and Infrastructure (Advancing 6G technology).
  
- SDG 11 – Sustainable Cities and Communities (Enabling autonomous urban mobility).
  
---

## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/Yazhini-G/AI-Enabled-Intelligent-Network-Slicing-for-6G

# Navigate to project directory
cd AI-Enabled-Intelligent-Network-Slicing-for-6G

# Install dependencies
pip install -r requirements.txt

# Run the application (Visual Studio Terminal)
streamlit run app.py
