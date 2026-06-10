# 🌐 Web Technologies Exploration

<div align="center">

![HTTP](https://img.shields.io/badge/HTTP-Protocol-blue?style=for-the-badge)
![cURL](https://img.shields.io/badge/cURL-Command%20Line-orange?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-API%20Development-green?style=for-the-badge)
![REST API](https://img.shields.io/badge/REST-API-red?style=for-the-badge)
![JSON](https://img.shields.io/badge/JSON-Data%20Format-black?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Cloud%20Lab-yellow?style=for-the-badge)

### 🚀 Hands-On Lab: Exploring HTTP, APIs, cURL, and Python Web Automation

</div>

---

# 📖 Overview

This lab provides practical experience with modern web technologies, HTTP communications, REST APIs, JSON processing, and Python automation. Using Linux command-line tools and Python scripting, students learn how web applications communicate and how cybersecurity professionals interact with APIs for automation, threat intelligence, monitoring, and security testing.

---

# 🎯 Learning Objectives

By completing this lab, I successfully learned how to:

✅ Understand HTTP requests and responses

✅ Use cURL to perform GET, POST, PUT, PATCH, and DELETE requests

✅ Analyze JSON API responses

✅ Interact with REST APIs using Python

✅ Parse and manipulate JSON data

✅ Handle API errors and exceptions

✅ Build reusable API clients

✅ Implement retry logic and timeout controls

✅ Work with real-world public APIs

---

# 🛠️ Technologies & Tools Used

| Tool             | Purpose                  |
| ---------------- | ------------------------ |
| cURL             | HTTP Request Testing     |
| Python 3         | API Automation           |
| Requests Library | REST API Communication   |
| JSON             | Data Exchange Format     |
| Linux Terminal   | Command-Line Operations  |
| HTTPBin          | API Testing Platform     |
| GitHub API       | Real-world API Testing   |
| Open-Meteo API   | Weather Data Integration |

---

# 🏗️ Lab Environment

### Al Nafi Cloud Machine

The lab environment included:

* Linux-Based Cloud Machine
* Python 3
* cURL
* Requests Library
* Nano/Vim Editors
* Networking Utilities

No additional setup or virtual machines were required.

---

# 📡 Task 1: Understanding HTTP with cURL

## 🔹 Basic GET Requests

### Test Internet Connectivity

```bash
ping -c 3 google.com
```

### Simple GET Request

```bash
curl https://httpbin.org/get
```

### Verbose HTTP Communication

```bash
curl -v https://httpbin.org/get
```

### Save Response to File

```bash
curl https://httpbin.org/get -o response.json

cat response.json
```

---

## 🔹 GET Requests with Parameters

### Query String Parameters

```bash
curl "https://httpbin.org/get?name=student&course=cybersecurity"
```

### Parameterized Request

```bash
curl -G https://httpbin.org/get \
-d "name=student" \
-d "course=cybersecurity"
```

### GitHub API Example

```bash
curl https://api.github.com/users/octocat
```

---

## 🔹 HTTP Headers

### View Headers Only

```bash
curl -I https://httpbin.org/get
```

### Send Custom Headers

```bash
curl -H "User-Agent: CyberSecurity-Student" \
-H "Accept: application/json" \
https://httpbin.org/headers
```

### Custom Header Verification

```bash
curl -H "Custom-Header: Lab7-Exercise" \
https://httpbin.org/headers
```

---

# 📨 Task 2: Working with HTTP Methods

## 🔹 POST Requests

### Form Data

```bash
curl -X POST https://httpbin.org/post \
-d "username=student&password=lab123"
```

### JSON Data

```bash
curl -X POST https://httpbin.org/post \
-H "Content-Type: application/json" \
-d '{
"name":"John Doe",
"email":"john@example.com",
"course":"cybersecurity"
}'
```

---

## 🔹 Create JSON File

```bash
cat > student_data.json << EOF
{
  "student_id": "CS001",
  "name": "Alice Smith",
  "course": "Cybersecurity Fundamentals",
  "semester": "Fall 2024"
}
EOF
```

### Send JSON File

```bash
curl -X POST https://httpbin.org/post \
-H "Content-Type: application/json" \
-d @student_data.json
```

---

## 🔹 Other HTTP Methods

### PUT Request

```bash
curl -X PUT https://httpbin.org/put \
-d "data=updated_information"
```

### DELETE Request

```bash
curl -X DELETE https://httpbin.org/delete
```

### PATCH Request

```bash
curl -X PATCH https://httpbin.org/patch \
-H "Content-Type: application/json" \
-d '{"field_to_update":"new_value"}'
```

---

# 🔍 Task 3: API Response Analysis

## Format JSON Output

```bash
curl https://api.github.com/repos/microsoft/vscode \
| python3 -m json.tool
```

---

## Extract Specific Information

```bash
curl -s https://api.github.com/repos/microsoft/vscode \
| grep -E '"name"|"description"|"language"'
```

---

## Check HTTP Status Codes

```bash
curl -w "%{http_code}\n" -s -o /dev/null https://httpbin.org/status/200

curl -w "%{http_code}\n" -s -o /dev/null https://httpbin.org/status/404

curl -w "%{http_code}\n" -s -o /dev/null https://httpbin.org/status/500
```

---

# 🐍 Task 4: Python API Development

## Basic API Client

### Features

* GET Requests
* JSON Parsing
* Error Handling
* GitHub API Integration

### Run Script

```bash
chmod +x basic_api_client.py

python3 basic_api_client.py
```

### Concepts Covered

* requests.get()
* JSON Parsing
* HTTP Status Validation
* Exception Handling

---

## Advanced API Client

### Features

* Object-Oriented Design
* Session Management
* GET Requests
* POST Requests
* Form Data Handling
* JSON Data Submission

### Run

```bash
chmod +x advanced_api_client.py

python3 advanced_api_client.py
```

---

# 🌦️ Task 5: Real-World API Integration

## Weather API Client

### API Used

Open-Meteo Weather API

### Capabilities

* Retrieve Live Weather Data
* Process JSON Responses
* Display Forecast Information
* Handle API Responses

### Run

```bash
chmod +x weather_api_client.py

python3 weather_api_client.py
```

---

### Information Retrieved

* Temperature
* Wind Speed
* Wind Direction
* Weather Code
* Time Zone

---

# 🛡️ Task 6: Robust API Error Handling

## Robust API Client Features

### Exception Handling

```python
try:
    response = requests.get(url)
except requests.exceptions.Timeout:
    pass
except requests.exceptions.ConnectionError:
    pass
```

### Retry Logic

```python
for attempt in range(max_retries):
```

### Exponential Backoff

```python
time.sleep(2 ** attempt)
```

### Timeout Protection

```python
requests.get(url, timeout=5)
```

---

## Run Script

```bash
chmod +x robust_api_client.py

python3 robust_api_client.py
```

---

# 📂 Project Files Created

```text
.
├── response.json
├── student_data.json
├── basic_api_client.py
├── advanced_api_client.py
├── weather_api_client.py
├── robust_api_client.py
└── README.md
```

---

# 🔬 Verification Commands

## Test Python Clients

```bash
python3 basic_api_client.py

python3 advanced_api_client.py

python3 weather_api_client.py
```

---

## Test cURL

```bash
curl -s https://httpbin.org/get

curl -s -X POST https://httpbin.org/post \
-H "Content-Type: application/json" \
-d '{"test":"verification"}'
```

---

## Review Files

```bash
ls -la *.py *.json
```

---

# 🚨 Troubleshooting

## cURL Missing

```bash
sudo apt update

sudo apt install curl -y
```

---

## Requests Library Missing

```bash
pip3 install requests
```

or

```bash
sudo apt install python3-requests
```

---

## Connectivity Problems

```bash
ping -c 3 8.8.8.8

nslookup httpbin.org
```

---

## Permission Errors

```bash
chmod +x *.py
```

---

# 📚 HTTP Methods Summary

| Method | Purpose          |
| ------ | ---------------- |
| GET    | Retrieve Data    |
| POST   | Create Resources |
| PUT    | Update Resources |
| PATCH  | Partial Updates  |
| DELETE | Remove Resources |

---

# 📊 Important HTTP Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | OK                    |
| 201  | Created               |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 404  | Not Found             |
| 500  | Internal Server Error |

---

# 🔐 Cybersecurity Relevance

Understanding APIs and web technologies is essential because security professionals use them for:

### Threat Intelligence

* Gathering threat feeds
* Consuming intelligence APIs

### Security Automation

* Automating incident response
* Integrating security tools

### Web Security Testing

* API Security Assessments
* Authentication Testing
* Authorization Testing

### Monitoring & Logging

* Security Dashboards
* SIEM Integrations
* Cloud Security Monitoring

---

# 🎓 Skills Acquired

✅ HTTP Fundamentals

✅ REST API Communication

✅ cURL Usage

✅ JSON Processing

✅ Python Requests Library

✅ Error Handling

✅ Retry Logic

✅ API Security Concepts

✅ Web Automation

✅ Real-World API Integration

---

# 🏆 Lab Completion Summary

Successfully completed the **Web Technologies Exploration Lab** on the **Al Nafi Cloud Platform**, gaining practical experience with modern web communications, REST APIs, Python automation, and HTTP protocol analysis.

These skills form a critical foundation for advanced cybersecurity domains including:

* Web Application Security
* API Security Testing
* Security Automation
* Threat Intelligence
* Cloud Security
* Security Engineering

---

<div align="center">

### 🌐 Learning Web Technologies for Cybersecurity Excellence

**Completed on Al Nafi Cloud Platform 🚀**

</div>
