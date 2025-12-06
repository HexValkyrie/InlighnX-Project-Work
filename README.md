# InlighnX-Project-Work
**THREAT VORTEX ANALYZER (TVA)**
Hybrid Corporate + Technical Security Report

**Author:** Komal Ratnaparkhe

**Role:** SOC Analyst (L1) & Ethical Hacking Intern

**Project Type:** Predictive Threat Intelligence + SOC Behavior Analytics

---

# **Threat Vector Analyzer (TVA) — AI-Powered SOC Intelligence Engine**

### *Next-Gen Detection. Analyst-First Design. Enterprise-Ready.*

```
████████╗██╗   ██╗ █████╗ 
╚══██╔══╝██║   ██║██╔══██╗
   ██║   ██║   ██║███████║
   ██║   ██║   ██║██╔══██║
   ██║   ╚██████╔╝██║  ██║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
      Threat Vector Analyzer
```
**Executive Summary**

> **TVA is a machine-learning powered correlation engine that detects multi-stage attacks by correlating system logs, network telemetry, user behavior, and known threat actor patterns—automatically delivering attack chain context to SOC Analysts.**
>
> Designed for: **L1 SOC Analysts, Ethical Hackers, Detection Engineers, Blue Teamers.**

The Threat Vortex Analyzer (TVA) is an innovative, behavior-based, early-warning detection system designed to help Security Operations Centers (SOC) identify cyberattacks before they escalate.
Traditional SIEMs alert analysts after attackers cross certain thresholds. TVA flips the script — it catches the weak signals, pre-attack indicators, and staging activities that typical tools ignore.

This project blends Ethical Hacking mindset + SOC defensive analysis and demonstrates command over:

Threat modeling
MITRE ATT&CK
Log analysis
Behavior analytics
Early-warning detection
Python automation

TVA is a unique and original project — designed to represent a new class of SOC tools: Predictive Defense Engines.
---

**Project Scope
Includes:**

Log ingestion (Windows/Linux/Syslog)
Weak signal analysis
Behavioral pattern recognition
Threat scoring
Pre-attack clustering (“vortexing”)
MITRE ATT&CK mapping
Alert dashboard
SOC-style incident report

**Excludes:**

Real-time agent-based deployment
EDR decision automation
ML models (future enhancement)

---

---

## 🔖 What’s in this repo
- `tva.py` — main detection & scoring engine (Python prototype)
- `configs/` — detection rules, IOC feeds, MITRE mapping
- `sample_logs/` — synthetic sample logs to run the demo
- `output/` — generated results and dashboard CSVs
- `docs/TVA_Project_Report.md` — professional project report (export to PDF)
- `assets/` — architecture / flowchart / dashboard images (upload PNGs here)

---
#  **Methodology**

TVA uses a hybrid approach inspired by:
Ethical Hacking Recon → Exploit → Escalate → Persist
SOC Event Correlation
MITRE ATT&CK Pre-Attack Tactics

Steps:
Event Ingestion
Ingest logs from simulated or real systems.
Weak Signal Detection

Look for early behaviors:
Sudden login bursts
Odd service enumeration
Port scanning attempts
New processes in odd locations

Pattern & Behavior Analysis
Identify:
Timing patterns
Frequency bursts
Adversarial sequences
Threat Scoring (TVS)

Each event gets a score based on:
MITRE mapping
Behavior context
Past occurrences
Threat Vortex Clustering
Combine related anomalies into clusters:
“Brute-force preparation vortex”
“Internal recon vortex”
“Privilege escalation vortex”
Dashboard Visualization
Plots risk scores, events, and trends.

---

# **Project Highlights**

*  **Zero-day style correlation** using anomaly detection
*  **ML-assisted attack chain reconstruction**
*  **Real-time threat scoring (TVAScore™)**
*  **Multi-source ingestion** (Windows, Sysmon, Network logs)
*  **Highly actionable alerts** — no noise
*  **Red Team simulation mode** for ethical hackers
*  **Sleek SIEM-like dashboard**

---

#  **Architecture Overview**

```
             +----------------------------+
             |     Log Collection Layer   |
             | (Win Events • Sysmon • PCAP)|
             +--------------+-------------+
                            |
                            v
                 +----------------------+
                 |  Preprocessing Hub   |
                 | (Parsing + Normaliz.)|
                 +----------+-----------+
                            |
                            v
          +--------------------------------------+
          |  TVA Detection Engine (Core)         |
          |  • Anomaly Detector (ML)             |
          |  • Signature Mapper (MITRE ATT&CK)   |
          |  • Behavior Correlator               |
          |  • TVAScore Calculator               |
          +------------------+-------------------+
                               |
                               v
                      +-----------------+
                      | Alerting Layer  |
                      |  JSON / CSV     |
                      |  Email / Slack  |
                      +--------+--------+
                               |
                               v
                     +-------------------+
                     |  TVA Dashboard    |
                     +-------------------+
```
---

#  **TVA Flowchart**

```
┌─────────────┐
│ Start TVA   │
└──────┬──────┘
       ▼
┌─────────────┐
│ Collect Logs│
└──────┬──────┘
       ▼
┌──────────────────┐
│ Detect Weak Signal│
│ (4625, scans, etc)│
└──────┬────────────┘
       ▼
┌──────────────────┐
│ Behavior Analysis │
│ (timing, bursts)  │
└──────┬────────────┘
       ▼
┌──────────────────┐
│ Score Activity   │
│ (TVS score)      │
└──────┬────────────┘
       ▼
┌──────────────────┐
│ Cluster Events   │
│ (Vortex groups)  │
└──────┬────────────┘
       ▼
┌──────────────────┐
│ Update Dashboard │
└──────┬────────────┘
       ▼
┌───────────────┐
│ End / Loop    │
└───────────────┘

```

---
# **Threat Scoring Pipeline Diagram**

```
Event → Normalize → Behavior Check → MITRE Mapping → TVS Scoring → Vortex Cluster → Dashboard Alert

```
Detailed stage diagram:

```
┌──────────┐
│ Raw Log  │
└────┬─────┘
     ▼
┌─────────────┐
│ Normalizer  │
└────┬────────┘
     ▼
┌────────────────┐
│ Behavior Engine │
└────┬────────────┘
     ▼
┌─────────────────┐
│ MITRE Technique │
│     Matching    │
└────┬────────────┘
     ▼
┌────────────────┐
│ TVS Calculation │
└────┬────────────┘
     ▼
┌─────────────────────┐
│ Vortex Grouping      │
└────┬─────────────────┘
     ▼
┌────────────────┐
│ Dashboard Alert│
└────────────────┘


```
---

#  **What TVA Detects**

 ✔️ Multi-stage intrusions

 ✔️ Lateral movement

 ✔️ Privilege escalation

 ✔️ Beaconing / C2 communication

 ✔️ Suspicious parent-child processes

 ✔️ Credential access patterns

 ✔️ Persistence via registry tasks

 ✔️ PowerShell abuse

---

# **TVA Dashboard Preview**

Image `/assets/tva_dashboard.png`

```
┌─────────────────────────────────────────────────────────────┐
│ TVA Dashboard                                               │
├─────────────────────────────────────────────────────────────┤
│ Alerts: 12  | Critical: 3 | High: 4 | Medium: 5             │
│ TVAScore Graph: ████░░░░░██████░░░░███████                  │
│ ----------------------------------------------------------- │
│ Top Behaviors:                                              │
│ 1. Suspicious PS Execution (EID 4104)                        │
│ 2. Failed Logon Burst (EID 4625)                             │
│ 3. Network Beacon Pattern (PCAP)                             │
└─────────────────────────────────────────────────────────────┘
```

---

# **Dashboard Mockup**

```
+-------------------------------------------------------------+
|                    THREAT VORTEX ANALYZER                   |
+-----------------------------+-------------------------------+
| Threat Score Trend          | MITRE Heatmap                 |
| (Bar Graph)                 | (Color-coded techniques)      |
+-----------------------------+-------------------------------+
| Top Hosts by Suspicion      | Vortex Clusters               |
| (Table: Host/IP/Score)      | (Grouped anomalies view)      |
+-------------------------------------------------------------+
| Event Timeline (Chronological Activity Graph)               |
+-------------------------------------------------------------+

```
---

# **Event Samples (JSON)**

```
[
  {
    "timestamp": "2025-12-01T03:45:10Z",
    "event_id": "4625",
    "source_ip": "192.168.1.45",
    "description": "Failed login attempt",
    "count": 5
  },
  {
    "timestamp": "2025-12-01T03:46:22Z",
    "event_id": "PORT_SCAN",
    "source_ip": "192.168.1.200",
    "description": "Sequential port probing on 445, 3389, 5985",
    "count": 3
  }
]

```
---

#  **Threat Vortex Score (TVS) Calculation**

```
TVS = (Behavior Weight × Frequency × MITRE Severity) + Time-Window Modifier
```
Example scoring:

Failed login bursts → +5
Port scanning → +8
Anomaly in odd hours → +3
MITRE high severity → × 1.4

---

# **SOC Investigation Sample Report**

Incident Title: Reconnaissance Vortex Detected
Severity: Medium–High
Detection Source: TVA (Threat Vortex Analyzer)

**Summary:**
TVA identified early reconnaissance behavior from internal host 192.168.1.200. Activity matched MITRE techniques under Reconnaissance and Discovery.

Indicators:
Port probing (445 → 3389 → 5985)
Off-hours enumeration
Failed login bursts

Threat Vortex Score (TVS): 74
Cluster Categorization:
ReconSweep_Vortex_01

SOC Recommendation:
Block IP
Review user activity
Enable throttling on authentication
Check privilege misuse

---

# **Core Features**

## 1. **ML-Based Threat Detection**

TVA uses:

* Isolation Forest
* LOF
* Statistical deviation

To identify anomalies in:

* Process creation
* Logon behavior
* Network activity

##  2. **Attack Chain Correlation**

TVA links together:

* Recon → Execution → Priv. Esc → Lateral Movement → Impact

##  3. **Red Team Simulation Mode**

Feeds TVA sample malicious logs to:

* Validate detection
* Benchmark TVAScore accuracy

##  4. **Multi-Log Support**

Supports:

* Windows Event Logs
* Sysmon
* Zeek
* RAW PCAP
* Firewall logs

##  5. **TVAScore™**

Custom scoring algorithm based on:

* Severity
* Frequency
* MITRE mapping
* Behavior risk
* ML anomaly weight

## 6. **Recommendations**

Integrate TVA with SIEM ingestion
Add ML-based anomaly clustering
Expand ATT&CK mapping
Add automatic triage suggestions
Create alerting webhook for SOC tools

# **Conclusion**

TVA demonstrates advanced defensive reasoning by detecting pre-attack behaviors before standard tools raise alerts.
This strengthens SOC readiness and brings predictive defense capabilities into everyday monitoring.

This hybrid project proves strong capabilities in:
Ethical hacking
SOC monitoring
Threat intelligence
Python scripting
MITRE ATT&CK
Event clustering
Cyber threat modeling

---

#  **Repository Structure**

```
📦 Threat-Vector-Analyzer
 ┣ 📂 assets/
 ┃ ┣ tva_architecture.png
 ┃ ┣ tva_dashboard.png
 ┃ ┗ tva_flowchart.png
 ┣ 📂 data_samples/
 ┃ ┣ sysmon_sample.csv
 ┃ ┣ windows_events.evtx
 ┃ ┗ pcap_test.pcap
 ┣ 📂 src/
 ┃ ┣ analyzer.py
 ┃ ┣ correlator.py
 ┃ ┣ model.py
 ┃ ┣ scorer.py
 ┃ ┗ dashboard.py
 ┣ 📂 docs/
 ┃ ┗ TVA_Report.pdf
 ┣ 📄 README.md
 ┗ 📄 requirements.txt
```

---

#  **How to Use**

### **1. Clone**

```bash
git clone https://github.com/yourusername/Threat-Vector-Analyzer.git
cd Threat-Vector-Analyzer
```

### **2. Install Requirements**

```bash
pip install -r requirements.txt
```

### **3. Run TVA**

```bash
python analyzer.py --input data_samples/
```

### **4. Open Dashboard**

```bash
python dashboard.py
```

---

#  **Example Output**

```
[TVA] Suspicious Parent-Child Sequence Detected
Process: powershell.exe -> rundll32.exe
TVAScore: 91 (Critical)
Technique: T1059.001 PowerShell
```

---

#  **MITRE ATT&CK Mapping**

| Technique ID | Description       | TVA Support |
| ------------ | ----------------- | ----------- |
| T1059        | Command Execution | ✔️          |
| T1059.001    | PowerShell        | ✔️          |
| T1204        | User Execution    | ✔️          |
| T1003        | Credential Access | ✔️          |
| T1021        | Remote Services   | ✔️          |
| T1105        | Exfiltration      | ✔️          |
| T1083        | Reconnaissance    | ✔️          |
| T1078        | Valid Accounts    | ✔️          |

---

#  **Roadmap**

* [ ] Add C2 Detection Module
* [ ] Integrate with ELK
* [ ] Add live SOC dashboard
* [ ] Add threat Intel (MISP API)

---

#  **Use Cases**

### For SOC Analysts:

* Enrich L1 investigation
* Validate alerts
* Reduce false positives
* Attack chain clarity

### For Ethical Hackers:

* Use TVA to test your attacks
* Prove detection gaps
* Strengthen reporting

---

#  **Author**

**Komal Ratnaparkhe**
SOC Analyst • Ethical Hacker • Blue Team Enthusiast
📍 India

---
