#!/usr/bin/env python3
import requests
import json

def make_get_request(url):
    """Make a GET request and return the response"""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None

def main():
    # Test with httpbin
    print("=== Testing GET Request ===")
    url = "https://httpbin.org/get"
    data = make_get_request(url)
    
    if data:
        print("Request successful!")
        print(f"Origin IP: {data.get('origin', 'Unknown')}")
        print(f"User Agent: {data.get('headers', {}).get('User-Agent', 'Unknown')}")
    
    # Test with GitHub API
    print("\n=== Testing GitHub API ===")
    github_url = "https://api.github.com/users/octocat"
    github_data = make_get_request(github_url)
    
    if github_data:
        print(f"GitHub User: {github_data.get('login', 'Unknown')}")
        print(f"Public Repos: {github_data.get('public_repos', 'Unknown')}")
        print(f"Followers: {github_data.get('followers', 'Unknown')}")

if __name__ == "__main__":
    main()
