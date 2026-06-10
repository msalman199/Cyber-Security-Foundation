#!/usr/bin/env python3
import requests
import json
import sys

class APIClient:
    def __init__(self, base_url="https://httpbin.org"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'CyberSecurity-Lab-Client/1.0'
        })
    
    def get(self, endpoint, params=None):
        """Make a GET request"""
        url = f"{self.base_url}/{endpoint}"
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"GET request failed: {e}")
            return None
    
    def post(self, endpoint, data=None, json_data=None):
        """Make a POST request"""
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
    
    def test_get_with_params(self):
        """Test GET request with parameters"""
        print("=== Testing GET with Parameters ===")
        params = {
            'student': 'cybersec_learner',
            'lab': 'web_technologies',
            'level': 'basic'
        }
        
        result = self.get('get', params=params)
        if result:
            print("Parameters sent successfully:")
            for key, value in result.get('args', {}).items():
                print(f"  {key}: {value}")
    
    def test_post_json(self):
        """Test POST request with JSON data"""
        print("\n=== Testing POST with JSON ===")
        student_info = {
            'name': 'Cybersecurity Student',
            'course': 'Web Technologies Lab',
            'skills': ['HTTP', 'APIs', 'Python'],
            'lab_number': 7
        }
        
        result = self.post('post', json_data=student_info)
        if result:
            print("JSON data sent successfully:")
            sent_data = result.get('json', {})
            print(f"  Name: {sent_data.get('name')}")
            print(f"  Course: {sent_data.get('course')}")
            print(f"  Skills: {sent_data.get('skills')}")
    
    def test_post_form_data(self):
        """Test POST request with form data"""
        print("\n=== Testing POST with Form Data ===")
        form_data = {
            'username': 'student123',
            'action': 'login',
            'timestamp': '2024-01-01T12:00:00Z'
        }
        
        result = self.post('post', data=form_data)
        if result:
            print("Form data sent successfully:")
            sent_data = result.get('form', {})
            for key, value in sent_data.items():
                print(f"  {key}: {value}")

def main():
    client = APIClient()
    
    # Run all tests
    client.test_get_with_params()
    client.test_post_json()
    client.test_post_form_data()
    
    print("\n=== API Client Testing Complete ===")

if __name__ == "__main__":
    main()
