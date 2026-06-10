#!/usr/bin/env python3
"""
A simple hello world program
"""

def main():
    print("Hello, Git World!")
    print("This is my first versioned program.")
    

def greet_user(name):
    """Greet a specific user"""
    print(f"Hello, {name}! Welcome to Git!")

# Add a new greeting
greet_user("Student")

def display_info():
    """Display project information"""
    print("=" * 30)
    print("Project: My First Git Project")
    print("Version: 1.0")
    print("Learning: Git version control")
    print("=" * 30)

# Display project info
display_info()
if __name__ == "__main__":
    main()
