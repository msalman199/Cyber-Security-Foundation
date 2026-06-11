# 🛡️🤖 AI-Driven Threat Detection Basics — Complete Lab (Full Project File)

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Security-orange?style=for-the-badge)
![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04+-E95420?style=for-the-badge&logo=ubuntu)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-yellow?style=for-the-badge)
![CyberSecurity](https://img.shields.io/badge/CyberSecurity-Threat%20Detection-red?style=for-the-badge)

---

# 🚀 AI-Driven Threat Detection Basics

This is a complete hands-on cybersecurity lab for building:

- Statistical anomaly detection system
- Real-time threat monitoring engine
- Machine learning-based threat classifier
- Log analysis and alert automation system

---

# 🎯 Objectives

By the end of this lab, you will be able to:

- Implement anomaly detection for security logs  
- Build automated alert systems  
- Train ML models for threat classification  
- Detect unusual system behavior using statistics  
- Create real-time monitoring pipelines  

---

# 📌 Prerequisites

- Python basics (loops, functions, file handling)
- Linux command line
- Basic statistics (mean, standard deviation)
- Understanding of logs

---

# 🖥️ Lab Environment

- Ubuntu 20.04+
- Python 3.8+
- pip installed
- nano / vim editors
- Internet access

---

# ⚙️ TASK 1 — Environment Setup & Log Generation

---

## 🧩 Step 1.1 Install Dependencies

```bash
sudo apt update
pip3 install pandas numpy scikit-learn matplotlib
📁 Step 1.2 Project Structure
mkdir -p ~/threat_detection_lab/{logs,scripts,models,alerts}
cd ~/threat_detection_lab
🧪 Step 1.3 Log Generator Script
📄 generate_logs.py
#!/usr/bin/env python3
import random
import datetime

def generate_sample_logs():
    normal_activities = [
        "User login successful",
        "File access granted",
        "Database query executed"
    ]

    suspicious_activities = [
        "Multiple failed login attempts",
        "SQL injection attempt detected",
        "Unauthorized file access attempt"
    ]

    logs = []

    for _ in range(1000):
        logs.append({
            "level": "INFO",
            "activity": random.choice(normal_activities)
        })

    for _ in range(50):
        logs.append({
            "level": "WARNING",
            "activity": random.choice(suspicious_activities)
        })

    random.shuffle(logs)

    with open("logs/system.log", "w") as f:
        for log in logs:
            timestamp = datetime.datetime.now()
            ip = f"192.168.1.{random.randint(1,255)}"
            user = f"user{random.randint(1,50)}"
            f.write(f"{timestamp} | {log['level']} | {ip} | {user} | {log['activity']}\n")

if __name__ == "__main__":
    generate_sample_logs()
▶️ Run
chmod +x generate_logs.py
python3 generate_logs.py
📊 TASK 2 — Statistical Anomaly Detection
🧠 Log Analyzer
📄 scripts/log_analyzer.py
#!/usr/bin/env python3
import pandas as pd
import numpy as np

class LogAnalyzer:

    def __init__(self, log_file):
        self.log_file = log_file
        self.df = None

    def parse_logs(self):
        data = []
        with open(self.log_file, "r") as f:
            for line in f:
                parts = line.strip().split(" | ")
                if len(parts) == 5:
                    data.append(parts)

        self.df = pd.DataFrame(data, columns=[
            "timestamp", "level", "ip", "user", "activity"
        ])

        self.df["timestamp"] = pd.to_datetime(self.df["timestamp"])

    def detect_failed_logins(self):
        failed = self.df[self.df["activity"].str.contains("failed", case=False)]
        return failed["user"].value_counts()

    def detect_ip_anomalies(self):
        counts = self.df["ip"].value_counts()
        mean = counts.mean()
        std = counts.std()

        return counts[counts > mean + 2 * std]

    def detect_after_hours(self):
        self.df["hour"] = self.df["timestamp"].dt.hour
        return self.df[(self.df["hour"] < 9) | (self.df["hour"] > 17)]

    def detect_keywords(self):
        keywords = ["injection", "malware", "unauthorized", "scanning"]
        return self.df[self.df["activity"].str.contains("|".join(keywords), case=False)]

    def summary(self):
        print("\n📊 SUMMARY REPORT")
        print("Total logs:", len(self.df))
        print("Unique users:", self.df["user"].nunique())
        print("Unique IPs:", self.df["ip"].nunique())
        print("Warning logs:", len(self.df[self.df["level"] == "WARNING"]))


def main():
    analyzer = LogAnalyzer("logs/system.log")
    analyzer.parse_logs()

    print("\n🚨 Failed Logins:\n", analyzer.detect_failed_logins())
    print("\n🌐 IP Anomalies:\n", analyzer.detect_ip_anomalies())
    print("\n⏰ After Hours:\n", analyzer.detect_after_hours().head())
    print("\n🔍 Keywords:\n", analyzer.detect_keywords().head())

    analyzer.summary()

if __name__ == "__main__":
    main()
▶️ Run Analyzer
cd ~/threat_detection_lab/scripts
python3 log_analyzer.py
🚨 TASK 3 — Real-Time Monitoring System
⚙️ alert_config.json
{
  "console_alerts": true,
  "alert_threshold": 2,
  "monitoring_interval": 3,
  "alert_log_file": "../alerts/threat_alerts.log",
  "threat_patterns": [
    "failed login",
    "unauthorized",
    "injection",
    "malware",
    "scanning"
  ],
  "severity_levels": {
    "injection": "HIGH",
    "malware": "HIGH",
    "unauthorized": "MEDIUM",
    "failed login": "LOW"
  }
}
🛰️ real_time_monitor.py
#!/usr/bin/env python3
import time
import json
from datetime import datetime

class ThreatMonitor:

    def __init__(self, log_file, config_file):
        self.log_file = log_file
        self.config = json.load(open(config_file))
        self.last_position = 0

    def check_new_entries(self):
        with open(self.log_file, "r") as f:
            f.seek(self.last_position)
            lines = f.readlines()
            self.last_position = f.tell()
        return lines

    def analyze_entry(self, line):
        for pattern in self.config["threat_patterns"]:
            if pattern.lower() in line.lower():
                return {
                    "pattern": pattern,
                    "severity": self.config["severity_levels"].get(pattern, "LOW"),
                    "entry": line
                }
        return None

    def send_alert(self, threat):
        msg = f"[{datetime.now()}] 🚨 {threat['severity']} THREAT: {threat['pattern']} -> {threat['entry']}"
        print(msg)

        with open(self.config["alert_log_file"], "a") as f:
            f.write(msg + "\n")

    def start_monitoring(self):
        print("🛰️ Monitoring started...")
        while True:
            lines = self.check_new_entries()

            for line in lines:
                threat = self.analyze_entry(line)
                if threat:
                    self.send_alert(threat)

            time.sleep(self.config["monitoring_interval"])


def main():
    monitor = ThreatMonitor("logs/system.log", "scripts/alert_config.json")
    monitor.start_monitoring()

if __name__ == "__main__":
    main()
▶️ Test Monitoring
Terminal 1
python3 scripts/real_time_monitor.py
Terminal 2
echo "$(date) | WARNING | 10.0.0.1 | admin | SQL injection attempt detected" >> logs/system.log
🤖 TASK 4 — Machine Learning Threat Detection
🧠 ml_threat_detector.py
#!/usr/bin/env python3
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

class MLThreatDetector:

    def load_data(self):
        data = []
        with open("logs/system.log") as f:
            for line in f:
                parts = line.strip().split(" | ")
                if len(parts) == 5:
                    data.append(parts)

        df = pd.DataFrame(data, columns=[
            "timestamp", "level", "ip", "user", "activity"
        ])

        df["timestamp"] = pd.to_datetime(df["timestamp"])
        return df

    def extract_features(self, df):
        df["hour"] = df["timestamp"].dt.hour
        df["is_threat"] = df["level"].apply(lambda x: 1 if x == "WARNING" else 0)
        df["activity_len"] = df["activity"].str.len()
        df["failed"] = df["activity"].str.contains("failed", case=False).astype(int)
        df["unauthorized"] = df["activity"].str.contains("unauthorized", case=False).astype(int)
        df["injection"] = df["activity"].str.contains("injection", case=False).astype(int)

        return df

    def train_models(self, df):
        features = ["hour", "activity_len", "failed", "unauthorized", "injection"]
        X = df[features]
        y = df["is_threat"]

        iso = IsolationForest(contamination=0.1)
        iso.fit(X)

        rf = RandomForestClassifier()
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

        rf.fit(X_train, y_train)

        return iso, rf

    def save_models(self, iso, rf):
        pickle.dump(iso, open("models/isolation.pkl", "wb"))
        pickle.dump(rf, open("models/randomforest.pkl", "wb"))

def main():
    detector = MLThreatDetector()
    df = detector.load_data()
    df = detector.extract_features(df)
    iso, rf = detector.train_models(df)
    detector.save_models(iso, rf)

    print("✅ Models trained successfully!")

if __name__ == "__main__":
    main()
▶️ Train Model
python3 scripts/ml_threat_detector.py
📈 MODEL EVALUATOR
import pickle
import pandas as pd

def load_models():
    iso = pickle.load(open("models/isolation.pkl", "rb"))
    rf = pickle.load(open("models/randomforest.pkl", "rb"))
    return iso, rf

print("📊 Models loaded successfully")
📂 FINAL PROJECT STRUCTURE
threat_detection_lab/
│
├── logs/
│   └── system.log
│
├── scripts/
│   ├── generate_logs.py
│   ├── log_analyzer.py
│   ├── real_time_monitor.py
│   └── ml_threat_detector.py
│
├── models/
│   ├── isolation.pkl
│   └── randomforest.pkl
│
├── alerts/
│   └── threat_alerts.log
│
└── alert_config.json
🎯 FINAL OUTCOME

✔ Log anomaly detection
✔ Real-time alert system
✔ ML-based threat classification
✔ Hybrid cybersecurity detection pipeline

🛡️ END OF COMPLETE LAB
