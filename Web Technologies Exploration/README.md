# 🌐 Web Technologies Exploration

## Objectives

By the end of this lab, students will be able to:

* Understand the fundamentals of HTTP requests and responses
* Use curl command-line tool to make GET and POST requests
* Explore and analyze API responses in JSON format
* Write Python scripts to interact with REST APIs
* Understand the difference between various HTTP methods
* Parse and manipulate API data using Python
* Implement basic error handling for web requests

---

# 📋 Prerequisites

Before starting this lab, students should have:

* Basic understanding of Linux command line operations
* Familiarity with text editors (nano, vim, or gedit)
* Basic knowledge of Python programming
* Understanding of JSON data format
* Basic networking concepts (IP addresses, ports, protocols)

---

# ☁️ Lab Environment Setup

Al Nafi provides Linux-based cloud machines for this lab.

### Pre-installed Tools

* curl
* Python 3
* requests library
* nano
* vim
* networking tools

---

# 🚀 Task 1: Understanding HTTP with curl

## Subtask 1.1: Basic GET Requests

### Test Internet Connectivity

```bash
ping -c 3 google.com
```

### First GET Request

```bash
curl https://httpbin.org/get
```

### Verbose Output

```bash
curl -v https://httpbin.org/get
```

### Save Response to File

```bash
curl https://httpbin.org/get -o response.json

cat response.json
```

---

## Subtask 1.2: GET Requests with Parameters

### Query Parameters

```bash
curl "https://httpbin.org/get?name=student&course=cybersecurity"
```

### Using curl Data Parameters

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

## Subtask 1.3: Understanding HTTP Headers

### View Response Headers

```bash
curl -I https://httpbin.org/get
```

### Custom Headers

```bash
curl -H "User-Agent: CyberSecurity-Student" \
-H "Accept: application/json" \
https://httpbin.org/headers
```

### Verify Custom Header

```bash
curl -H "Custom-Header: Lab7-Exercise" \
https://httpbin.org/headers | grep -A 10 "headers"
```

---

# 📡 Task 2: Making POST Requests

## Subtask 2.1: Basic POST Requests

### POST Form Data

```bash
curl -X POST https://httpbin.org/post \
-d "username=student&password=lab123"
```

### POST JSON Data

```bash
curl -X POST https://httpbin.org/post \
-H "Content-Type: application/json" \
-d '{"name":"John Doe","email":"john@example.com","course":"cybersecurity"}'
```

### Create JSON File

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

### POST JSON File

```bash
curl -X POST https://httpbin.org/post \
-H "Content-Type: application/json" \
-d @student_data.json
```

---

## Subtask 2.2: Other HTTP Methods

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

## Pretty Print JSON

```bash
curl https://api.github.com/repos/microsoft/vscode \
| python3 -m json.tool
```

---

## Extract Specific Fields

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

# 🐍 Task 4: Basic Python API Client

Create the following file:

## basic_api_client.py

```python
#!/usr/bin/env python3

import requests
import json

def make_get_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None

def main():
    print("=== Testing GET Request ===")

    url = "https://httpbin.org/get"
    data = make_get_request(url)

    if data:
        print("Request successful!")
        print(f"Origin IP: {data.get('origin','Unknown')}")
        print(f"User Agent: {data.get('headers',{}).get('User-Agent','Unknown')}")

    print("\n=== Testing GitHub API ===")

    github_url = "https://api.github.com/users/octocat"
    github_data = make_get_request(github_url)

    if github_data:
        print(f"GitHub User: {github_data.get('login','Unknown')}")
        print(f"Public Repos: {github_data.get('public_repos','Unknown')}")
        print(f"Followers: {github_data.get('followers','Unknown')}")

if __name__ == "__main__":
    main()
```

### Run Script

```bash
chmod +x basic_api_client.py

python3 basic_api_client.py
```

---

# 🐍 Task 5: Advanced Python API Client

## advanced_api_client.py

```python
#!/usr/bin/env python3

import requests

class APIClient:

    def __init__(self, base_url="https://httpbin.org"):
        self.base_url = base_url
        self.session = requests.Session()

        self.session.headers.update({
            "User-Agent":"CyberSecurity-Lab-Client/1.0"
        })

    def get(self, endpoint, params=None):

        url = f"{self.base_url}/{endpoint}"

        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"GET request failed: {e}")
            return None

    def post(self, endpoint, data=None, json_data=None):

        url = f"{self.base_url}/{endpoint}"

        try:
            if json_data:
                response = self.session.post(url, json=json_data)
            else:
                response = self.session.post(url, data=data)

            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"POST request failed: {e}")
            return None

client = APIClient()

params = {
    "student":"cybersec_learner",
    "lab":"web_technologies",
    "level":"basic"
}

print(client.get("get", params=params))

student_info = {
    "name":"Cybersecurity Student",
    "course":"Web Technologies Lab",
    "skills":["HTTP","APIs","Python"]
}

print(client.post("post", json_data=student_info))
```

### Run Script

```bash
chmod +x advanced_api_client.py

python3 advanced_api_client.py
```

---

# 🌦️ Task 6: Weather API Client

## weather_api_client.py

```python
#!/usr/bin/env python3

import requests

class WeatherAPIClient:

    def __init__(self):
        self.base_url = "https://api.open-meteo.com/v1"

    def get_weather_data(self, latitude, longitude):

        endpoint = f"{self.base_url}/forecast"

        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True,
            "timezone": "auto"
        }

        response = requests.get(endpoint, params=params)

        return response.json()

    def display_weather(self, data):

        current = data.get("current_weather", {})

        print(f"Temperature: {current.get('temperature')}°C")
        print(f"Wind Speed: {current.get('windspeed')} km/h")
        print(f"Wind Direction: {current.get('winddirection')}°")

client = WeatherAPIClient()

weather = client.get_weather_data(
    latitude=40.7128,
    longitude=-74.0060
)

client.display_weather(weather)
```

### Run Script

```bash
chmod +x weather_api_client.py

python3 weather_api_client.py
```

---

# 🛡️ Task 7: Robust API Client

## robust_api_client.py

```python
#!/usr/bin/env python3

import requests
import json
import time

class RobustAPIClient:

    def __init__(self, timeout=10, max_retries=3):

        self.timeout = timeout
        self.max_retries = max_retries
        self.session = requests.Session()

    def make_request(self, method, url, **kwargs):

        for attempt in range(self.max_retries):

            try:

                response = self.session.request(
                    method=method,
                    url=url,
                    timeout=self.timeout,
                    **kwargs
                )

                response.raise_for_status()

                return response.json()

            except requests.exceptions.Timeout:
                print("Timeout occurred")

            except requests.exceptions.ConnectionError:
                print("Connection error")

            except requests.exceptions.HTTPError as e:
                print(f"HTTP Error: {e}")

            time.sleep(2)

        return None

client = RobustAPIClient()

result = client.make_request(
    "GET",
    "https://httpbin.org/get"
)

print(result)
```

### Run Script

```bash
chmod +x robust_api_client.py

python3 robust_api_client.py
```

---

# ✅ Verification

### Test All Scripts

```bash
python3 basic_api_client.py

python3 advanced_api_client.py

python3 weather_api_client.py

python3 robust_api_client.py
```

### Test cURL

```bash
curl -s https://httpbin.org/get

curl -s -X POST https://httpbin.org/post \
-H "Content-Type: application/json" \
-d '{"test":"verification"}'
```

### Review Files

```bash
ls -la *.py *.json
```

---

# 🚨 Troubleshooting

## curl Not Installed

```bash
sudo apt update

sudo apt install curl -y
```

## requests Module Missing

```bash
pip3 install requests
```

or

```bash
sudo apt install python3-requests
```

## Connectivity Problems

```bash
ping -c 3 8.8.8.8

nslookup httpbin.org
```

## Permission Denied

```bash
chmod +x *.py
```

---

# 📚 HTTP Methods Summary

| Method | Purpose        |
| ------ | -------------- |
| GET    | Retrieve Data  |
| POST   | Create Data    |
| PUT    | Update Data    |
| PATCH  | Partial Update |
| DELETE | Delete Data    |

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

Understanding APIs and web technologies is essential for cybersecurity professionals because they are used for:

* Security Automation
* Threat Intelligence Collection
* Incident Response
* Security Monitoring
* API Security Testing
* Vulnerability Assessment
* Security Tool Integration

---

# 🏆 Lab Conclusion

Successfully completed **Web Technologies Exploration** on **Al Nafi Cloud Platform**.

### Skills Gained

* HTTP Fundamentals
* REST APIs
* cURL Operations
* JSON Parsing
* Python Requests Library
* API Automation
* Error Handling
* Web Security Concepts
* Real-World API Integration

These skills provide a strong foundation for advanced cybersecurity domains including:

* API Security Testing
* Web Application Security
* Threat Intelligence
* Security Automation
* Cloud Security
* Security Engineering

---

**🌐 End of Lab — Web Technologies Exploration**
