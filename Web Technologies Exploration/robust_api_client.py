#!/usr/bin/env python3
import requests
import json
import time
from typing import Optional, Dict, Any

class RobustAPIClient:
    def __init__(self, timeout=10, max_retries=3):
        self.timeout = timeout
        self.max_retries = max_retries
        self.session = requests.Session()
    
    def make_request(self, method: str, url: str, **kwargs) -> Optional[Dict[Any, Any]]:
        """Make HTTP request with error handling and retries"""
        
        for attempt in range(self.max_retries):
            try:
                print(f"Attempt {attempt + 1}: {method.upper()} {url}")
                
                response = self.session.request(
                    method=method,
                    url=url,
                    timeout=self.timeout,
                    **kwargs
                )
                
                # Check if request was successful
                response.raise_for_status()
                
                # Try to parse JSON
                try:
                    return response.json()
                except json.JSONDecodeError:
                    print("Warning: Response is not valid JSON")
                    return {"raw_content": response.text}
                
            except requests.exceptions.Timeout:
                print(f"Timeout error on attempt {attempt + 1}")
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)  # Exponential backoff
                    
            except requests.exceptions.ConnectionError:
                print(f"Connection error on attempt {attempt + 1}")
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)
                    
            except requests.exceptions.HTTPError as e:
                print(f"HTTP error: {e}")
                print(f"Status code: {e.response.status_code}")
                if e.response.status_code < 500:  # Don't retry client errors
                    break
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)
                    
            except requests.exceptions.RequestException as e:
                print(f"Request error: {e}")
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)
        
        print(f"All {self.max_retries} attempts failed")
        return None
    
    def test_various_scenarios(self):
        """Test different scenarios including error cases"""
        
        print("=== Testing Successful Request ===")
        success_data = self.make_request('GET', 'https://httpbin.org/get')
        if success_data:
            print("✓ Successful request completed")
        
        print("\n=== Testing 404 Error ===")
        not_found_data = self.make_request('GET', 'https://httpbin.org/status/404')
        if not not_found_data:
            print("✓ 404 error handled correctly")
        
        print("\n=== Testing Timeout (Simulated) ===")
        timeout_data = self.make_request('GET', 'https://httpbin.org/delay/15')
        if not timeout_data:
            print("✓ Timeout handled correctly")
        
        print("\n=== Testing POST with Data ===")
        post_data = {
            'test': 'robust_client',
            'timestamp': time.time(),
            'status': 'testing'
        }
        
        post_response = self.make_request(
            'POST', 
            'https://httpbin.org/post',
            json=post_data
        )
        
        if post_response:
            print("✓ POST request with JSON data successful")
            received_data = post_response.get('json', {})
            print(f"  Sent test value: {post_data['test']}")
            print(f"  Received test value: {received_data.get('test')}")

def main():
    print("=== Robust API Client Testing ===")
    client = RobustAPIClient(timeout=5, max_retries=2)
    client.test_various_scenarios()
    print("\n=== Testing Complete ===")

if __name__ == "__main__":
    main()
