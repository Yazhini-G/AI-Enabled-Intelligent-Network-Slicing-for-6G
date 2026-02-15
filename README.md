# AI-Enabled-Intelligent-Network-Slicing-for-6G

AI-Enabled Intelligent Network Slicing for 6G is a project designed to transition from the static resource allocation of 5G to the proactive, intelligent orchestration required for 6G. Traditional network slicing often suffers from high jitter and performance degradation when multiple high-priority services compete for the same resources.


This project overcomes these challenges by integrating a Digital Twin that mirrors physical network conditions in real-time. By utilizing an AI-driven orchestrator, the system performs Orthogonal Slicing—adding high-priority packet headers to critical data flows to ensure zero interference and guaranteed service levels. The inclusion of Explainable AI (XAI) provides transparency, allowing network administrators to understand the "Decision Weights" behind every resource allocation..

---
## Problem Statement

Legacy 5G network slicing faces significant challenges in the 6G era:

- Static Resource Allocation: Difficulty handling dynamic, ultra-low latency demands.

- Network Jitter: Significant performance drops during concurrent service requests.

- Black Box Decisions: Lack of transparency in how AI allocates critical resources.

- Manual Intervention: Slow response times to physical network changes.

---

## Key Features

-  Predictive Slice Isolation: Uses AI to maintain stable latencies ($0.5\text{--}0.6 \text{ ms}$) even under high network load.
-  Explainable AI (XAI) Dashboard: Provides real-time "Global Decision Weights" to justify resource priority.
-  Digital Twin Synchronization: A virtual mirror that simulates physical network congestion and predicts potential SLA violations.
-  Orthogonal Slicing: Automated priority queuing using packet headers to ensure a $0.2 \text{ ms}$ advantage for critical services.
-  Live Benchmarking: Real-time comparison between Legacy 5G Jitter and 6G AI-Native stability.

---

## Technologies Used

### Frontend & Visualization * Streamlit: Interactive web-based command center.
- Plotly/Graph Objects: High-fidelity real-time data visualization.

### Backend & Simulation * Python 3.9+: Core logic and data processing.
- NumPy/Pandas: Digital Twin mathematical modeling and performance analytics

### Network Concepts * mURLLC / eMBB / umMTC: 6G service class modeling.

- Edge Cloud Computing: Geographical resource splitting for independent SLAs.

- Sub-6GHz & THz Bands: Frequency-aware spectrum allocation.  

---

##  System Architecture

<img width="807" height="952" alt="Gemini_Generated_Image_g0g4qng0g4qng0g4" src="https://github.com/user-attachments/assets/e5f55b62-1eae-40c4-9d32-f9411ffd2474" />

1. Digital Twin Layer: Monitors real-time network load and simulates "what-if" scenarios.

2. AI Orchestrator: Evaluates service requests and selects the optimal slice (e.g., Slice 1 for Remote Surgery).

3. XAI Engine: Generates transparency reports on feature importance (Latency vs. Reliability).

4. Execution Layer: Deploys resources as Hardware-Locked or Software-Defined slices.

---
## How the System Works

1. The project operates as a closed-loop automation system where the Digital Twin and AI Orchestrator work in tandem to manage network resources.

2. Request Ingestion: When a user selects services (e.g., Remote Surgery and 8K Video) in the Network Control Center, the system identifies the specific 6G service class (mURLLC, eMBB, or umMTC) for each.

3. Digital Twin Synchronization: The Digital Twin Engine instantly creates a virtual model of the network based on the current "Simulated Congestion" level. It calculates the projected latency and reliability for both services.

4. AI Orchestration & Slice Selection:

      - The AI evaluates the service requirements against the Digital Twin's  predictions.

      - Mission-Critical tasks are assigned to Slice 1 (Hardware-Locked) to ensure zero interference from other traffic.

      - High-Bandwidth tasks are assigned to Slice 2 (Software-Defined) to maximize throughput.

5. Orthogonal Slicing Execution: If two services must share a slice, the AI applies Orthogonal Slicing. It injects high-priority packet headers into the primary service stream, allowing it to clear the network queue 0.2 ms faster than the secondary service.

6. XAI Transparency: The XAI Module simultaneously generates a report and a bar chart showing the Global Decision Weights. This explains why the AI prioritized certain features (like Latency or Reliability) for the selected configuration.

7. Real-Time Benchmarking: The results are plotted on the dashboard, comparing the stable, predictive latency of the 6G AI-Native system against the erratic, high-jitter performance of Legacy 5G.


---

## Hardware Requirements
- The 6G orchestrator is designed to run in a simulated environment that mirrors high-performance edge computing architectures.

- Processor: Intel Core i5/i7 (10th Gen or higher) or AMD Ryzen 5/7 to handle concurrent Digital Twin simulations.

- Memory (RAM): Minimum 8GB (16GB recommended) for smooth multitasking between the AI engine and the Streamlit dashboard.

- Storage: 500MB of free space for project files, datasets, and generated benchmark outputs.

- GPU (Optional): While not strictly required for this simulation, a dedicated GPU (NVIDIA GTX 1650 or higher) is recommended for training the underlying reinforcement learning models in the ml_training module.

---
## Software Requirements

- The system is built on an open-source stack to ensure compatibility across Windows, macOS, and Linux.

- Operating System: Windows 10/11, macOS (Monterey+), or Ubuntu 20.04+.

- Primary Language: Python 3.9+ (required for advanced NumPy and Plotly features).

- IDE: Visual Studio Code or PyCharm (used for coding, debugging, and terminal management).

- Web Browser: Google Chrome, Microsoft Edge, or Firefox (to view the Streamlit Network Control Center).

---

## Essential Libraries & Tools

- These tools must be installed via the requirements.txt file to enable the Digital Twin and XAI features.

- Streamlit: Powers the interactive 6G Command Center and real-time logs.

- NumPy: Used by the Digital Twin engine to generate predictive isolation data and simulate jitter.

- Pandas: Manages the service knowledge base and resource differentiation tables.

- Plotly: Generates the dynamic benchmarking graphs and XAI Global Decision Weight charts.

- Git: Used for version control and repository management on GitHub.
  
---
##  Objectives

- Achieve sub-1ms latency for mission-critical mURLLC services.

- Provide 100% transparency in AI decision-making via XAI.

- Reduce network jitter by 90% compared to legacy 5G static slicing.
  
---

##  Sustainable Development Goals (SDGs)

This project aligns with:

- SDG 9 – Industry, Innovation, and Infrastructure (Advancing 6G technology).
  
- SDG 11 – Sustainable Cities and Communities (Enabling autonomous urban mobility).
  
---

##  Installation & Setup

```bash
# Clone the repository
git clone https://github.com/Yazhini-G/AI-Enabled-Intelligent-Network-Slicing-for-6G

# Navigate to project directory
cd AI-Enabled-Intelligent-Network-Slicing-for-6G

# Install dependencies
pip install -r requirements.txt

# Install essential tools
pip install streamlit pandas numpy plotly

# Run the application (Visual Studio Terminal)
streamlit run main.py
