```

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time

# --- 1. The 6G Service Knowledge Base (Enhanced for Digital Twinning) ---
SERVICES = {
    "Remote Surgery": {"type": "mURLLC", "lat": 0.5, "rel": 99.999, "bw": 10, "slice": "Slice 1 (Ultra-Reliable)"},
    "Autonomous Vehicle": {"type": "mURLLC", "lat": 1.0, "rel": 99.99, "bw": 50, "slice": "Slice 1 (Ultra-Reliable)"},
    "8K Holographic Video": {"type": "feMBB", "lat": 10.0, "rel": 95.0, "bw": 1000, "slice": "Slice 2 (High-Bandwidth)"},
    "Cloud Gaming": {"type": "eMBB", "lat": 15.0, "rel": 98.0, "bw": 150, "slice": "Slice 2 (High-Bandwidth)"},
    "Smart Factory Sensors": {"type": "umMTC", "lat": 50.0, "rel": 99.0, "bw": 5, "slice": "Slice 3 (Massive IoT)"},
    "Emergency VoIP": {"type": "URLLC", "lat": 2.0, "rel": 99.9, "bw": 1, "slice": "Slice 1 (Ultra-Reliable)"}
}

st.set_page_config(page_title="6G AI-Native Orchestrator Pro", layout="wide")
st.title("🛰️ 6G AI-Native Multi-Service Orchestrator")
st.markdown("### *Digital Twin & Explainable AI Framework*")

# --- 2. Sidebar: Digital Twin Control Panel ---
st.sidebar.header("📡 Digital Twin Control")
network_load = st.sidebar.slider("Simulated Network Congestion (%)", 0, 100, 20)
s1 = st.sidebar.selectbox("Select Service 1 (Primary):", list(SERVICES.keys()), index=0)
s2 = st.sidebar.selectbox("Select Service 2 (Secondary):", ["None"] + list(SERVICES.keys()), index=0)

# --- 3. Digital Twin Engine (Correction: Dynamic Data Generation) ---
def get_live_metrics(base_lat, load, is_6g=True):
    # 6G handles load with stable predictive isolation [cite: 61, 118]
    # Legacy 5G suffers from high jitter during dual-requests [cite: 60, 114, 167]
    if is_6g:
        noise = np.random.uniform(-0.02, 0.05) 
        return base_lat + (load * 0.001) + noise
    else:
        jitter = np.random.uniform(5, 50) if load > 50 else np.random.uniform(2, 10)
        return base_lat + (load * 0.5) + jitter

if st.sidebar.button("🚀 Execute AI Orchestration"):
    st.subheader("🔁 Dynamic Allocation & Comparison Log")
    
    p1 = SERVICES[s1]
    st.info(f"🟢 **Deploying {s1}:** Assigned to **{p1['slice']}**. Digital Twin synchronized.")

    if s2 != "None" and s2 != s1:
        p2 = SERVICES[s2]
        st.warning(f"🟡 **Deploying {s2}:** Analyzing resource overlap on **{p2['slice']}**...")
        
        st.divider()
        st.subheader("⚖️ Service vs. Service: Resource Differentiation")
        
        comp_col1, comp_col2 = st.columns(2)
        
        with comp_col1:
            # Comparison Table [cite: 37, 100, 133]
            comp_data = {
                "Metric": ["Target Latency", "Reliability", "Slice Type", "Priority Level", "Spectrum Band"],
                s1: [f"{p1['lat']} ms", f"{p1['rel']}%", p1['slice'], "CRITICAL (Highest)", "Sub-6GHz (Stable)"],
                s2: [f"{p2['lat']} ms", f"{p2['rel']}%", p2['slice'], "STANDARD (Adaptive)", "THz (High-Speed)"]
            }
            st.table(pd.DataFrame(comp_data))

        with comp_col2:
            st.write("### 🧠 XAI Reasoning")
            # Logic Correction: Dynamic Reasoning based on Slice Selection [cite: 39, 87, 135]
            if p1['slice'] == p2['slice']:
                reasoning = (f"Both services share **{p1['slice']}**. The AI has performed **Orthogonal Slicing**[cite: 87, 102]. "
                             f"High-priority packet headers added to **{s1}** to ensure a 0.2ms queue priority over **{s2}**.")
            else:
                reasoning = (f"AI has isolated **{p1['slice']}** (Hardware-Locked) and **{p2['slice']}** (Software-Defined)[cite: 144, 145]. "
                             f"Resource blocks split at Edge Cloud to maintain independent SLAs[cite: 40].")
            st.success(reasoning)

    # --- 4. Visual Outputs (Correction: Dynamic Charts) ---
    st.divider()
    col1, col2 = st.columns([1, 1.2])

    with col1:
        st.subheader("📊 Active Slice Resource Pool")
        display_list = [{"Service": s, "Slice ID": SERVICES[s]['slice'], 
                         "Resource Lock": "Hardware-Locked" if "Slice 1" in SERVICES[s]['slice'] else "Software-Defined"} 
                        for s in ([s1] + ([s2] if s2 != "None" and s2 != s1 else []))]
        st.table(pd.DataFrame(display_list))

    with col2:
        st.subheader("🧠 XAI: Global Decision Weights")
        features = ["Latency Priority", "Reliability Weight", "Bandwidth Gain", "Resource Guardrail"]
        # Correction: Weights now react to the Service Type 
        if "mURLLC" in p1['type']:
            weights = [0.98, 0.96, 0.20, 0.90]
        elif "feMBB" in p1['type']:
            weights = [0.40, 0.35, 0.99, 0.60]
        else:
            weights = [0.30, 0.85, 0.15, 0.95]
            
        fig = px.bar(x=weights, y=features, orientation='h', color=weights, color_continuous_scale="Viridis")
        st.plotly_chart(fig, use_container_width=True)

    # --- 5. Benchmarking Correction: Load-Responsive Graphs ---
    st.divider()
    st.subheader("📉 Benchmarking: Legacy 5G vs. AI-Native 6G (Digital Twin Data)")
    c1, c2 = st.columns(2)
    
    # Generate dynamic time-series data based on load
    t_steps = list(range(10))
    data_5g = [get_live_metrics(p1['lat'], network_load, is_6g=False) for _ in t_steps]
    data_6g = [get_live_metrics(p1['lat'], network_load, is_6g=True) for _ in t_steps]

    with c1:
        st.error("### 🛑 Legacy 5G (Static Slicing)")
        st.write(f"**Status:** Congestion Impacted ({network_load}%)")
        fig5g = go.Figure(go.Scatter(x=t_steps, y=data_5g, mode='lines+markers', name="5G Latency", line=dict(color='red')))
        fig5g.update_layout(yaxis_title="Latency (ms)", xaxis_title="Time Interval")
        st.plotly_chart(fig5g)

    with c2:
        st.success("### 🚀 Your 6G (AI-Native Digital Twin)")
        st.write("**Status:** Stable Predictive Isolation")
        fig6g = go.Figure(go.Scatter(x=t_steps, y=data_6g, mode='lines+markers', name="6G Latency", line=dict(color='green')))
        fig6g.update_layout(yaxis_title="Latency (ms)", xaxis_title="Time Interval")
        st.plotly_chart(fig6g)

else:
    st.info("👈 Select services and network load in the sidebar, then click 'Execute AI Orchestration' to start the Digital Twin simulation.")

```
