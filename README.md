# Mini DevOps Monitoring System 🚀

![Python](https://img.shields.io/badge/Python-3.x-blue)
![DevOps](https://img.shields.io/badge/DevOps-Monitoring-green)
![Automation](https://img.shields.io/badge/Automation-Python-orange)

A **Python-based DevOps monitoring system** that performs basic infrastructure monitoring tasks such as:

* Server availability checks
* Disk usage monitoring
* Log file analysis
* Alert detection

This project demonstrates how Python can be used to automate **common DevOps monitoring tasks**.

---

# Features

* ✅ Server availability monitoring using ping
* ✅ Disk usage monitoring
* ✅ Log file error detection
* ✅ Configurable monitoring settings
* ✅ Simple automation workflow

---

# Project Structure

```id="g0nuzn"
mini-devops-monitor
│
├── monitor.py
├── config.py
└── server.log
```

---

# How It Works

The monitoring system performs three main checks:

### 1. Server Health Check

The script checks whether configured servers are reachable.

Example output:

```id="dmb83o"
[OK] google.com is reachable
[ALERT] server is DOWN
```

---

### 2. Disk Usage Monitoring

The script checks disk usage and alerts when usage exceeds a configured threshold.

Example:

```id="rc1quq"
Disk usage: 72.14%
WARNING: Disk usage above threshold
```

---

### 3. Log File Analysis

The script reads log files and detects **ERROR messages**.

Example:

```id="c9slrm"
[ERROR] ERROR Database connection failed
[ERROR] ERROR Timeout occurred
Total errors detected: 2
```

---

# Installation

Clone the repository:

```id="gw02ir"
git clone https://github.com/sebastiantnalu-crypto/mini-devops-monitoring-system.git
```

Navigate into the project:

```id="qfd0j4"
cd mini-devops-monitoring-system
```

Run the monitoring script:

```id="t5z8l0"
python3 monitor.py
```

---

# Configuration

Edit the **config.py** file to configure monitoring settings.

Example:

```id="r9nd4c"
servers = [
    "google.com",
    "github.com",
    "cloudflare.com"
]

disk_threshold = 80

log_file = "server.log"
```

---

# Technologies Used

* Python 3
* Linux system utilities
* DevOps automation concepts

---

# Future Improvements

Possible enhancements:

* Slack alert integration
* Email notifications
* Docker container monitoring
* Kubernetes pod health checks
* CI/CD integration

---

# Learning Purpose

This project demonstrates:

* Python automation for DevOps
* Basic infrastructure monitoring
* Log analysis techniques
* DevOps scripting workflows

---

# Author

**Sebastian Tomichan Naluthengumgal**

Aspiring DevOps / Cloud Engineer

LinkedIn
https://www.linkedin.com/in/sebastiantomichan/

GitHub
https://github.com/sebastiantnalu-crypto
