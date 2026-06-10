#!/usr/bin/env python3
"""
Password Security Checker - Lab 3 Task 3
This script demonstrates functions, loops, and conditions for password validation
"""

import re
import string

def check_password_length(password, min_length=8):
    """
    Function to check if password meets minimum length requirement
    """
    return len(password) >= min_length

def check_password_complexity(password):
    """
    Function to check password complexity using conditions
    """
    checks = {
        'has_uppercase': bool(re.search(r'[A-Z]', password)),
        'has_lowercase': bool(re.search(r'[a-z]', password)),
        'has_numbers': bool(re.search(r'\d', password)),
        'has_special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }
    return checks

def calculate_password_strength(password):
    """
    Function to calculate overall password strength score
    """
    score = 0
    feedback = []
    
    # Length check
    if check_password_length(password, 8):
        score += 2
    else:
        feedback.append("Password should be at least 8 characters long")
    
    if len(password) >= 12:
        score += 1
        
    # Complexity checks
    complexity = check_password_complexity(password)
    
    for check, passed in complexity.items():
        if passed:
            score += 2
        else:
            if check == 'has_uppercase':
                feedback.append("Add uppercase letters (A-Z)")
            elif check == 'has_lowercase':
                feedback.append("Add lowercase letters (a-z)")
            elif check == 'has_numbers':
                feedback.append("Add numbers (0-9)")
            elif check == 'has_special':
                feedback.append("Add special characters (!@#$%^&*)")
    
    # Check for common patterns
    if password.lower() in ['password', '123456', 'qwerty', 'admin']:
        score -= 5
        feedback.append("Avoid common passwords")
    
    # Check for repeated characters
    if len(set(password)) < len(password) * 0.6:
        score -= 2
        feedback.append("Avoid too many repeated characters")
    
    return max(0, score), feedback

def get_strength_level(score):
    """
    Function to determine strength level based on score
    """
    if score >= 9:
        return "VERY STRONG", "🟢"
    elif score >= 7:
        return "STRONG", "🟡"
    elif score >= 5:
        return "MODERATE", "🟠"
    elif score >= 3:
        return "WEAK", "🔴"
    else:
        return "VERY WEAK", "⚫"

def test_multiple_passwords():
    """
    Function to test multiple passwords using loops
    """
    test_passwords = [
        "123456",
        "password",
        "Password1",
        "MyP@ssw0rd",
        "SuperSecure123!",
        "admin",
        "P@ssw0rd2024!",
        "weakpass",
        "StrongP@ssw0rd123!"
    ]
    
    print("🔐 TESTING MULTIPLE PASSWORDS")
    print("=" * 60)
    
    results = []
    
    # Loop through each password
    for i, password in enumerate(test_passwords, 1):
        print(f"\nTest {i}: '{password}'")
        print("-" * 30)
        
        score, feedback = calculate_password_strength(password)
        strength, emoji = get_strength_level(score)
        
        print(f"Strength: {emoji} {strength} (Score: {score}/11)")
        
        if feedback:
            print("Recommendations:")
            for suggestion in feedback:
                print(f"  • {suggestion}")
        else:
            print("✅ Excellent password!")
        
        results.append({
            'password': password,
            'score': score,
            'strength': strength,
            'feedback_count': len(feedback)
        })
    
    return results

def generate_password_report(results):
    """
    Function to generate a summary report of password tests
    """
    print("\n📊 PASSWORD SECURITY REPORT")
    print("=" * 60)
    
    # Count passwords by strength level
    strength_counts = {}
    total_passwords = len(results)
    
    for result in results:
        strength = result['strength']
        strength_counts[strength] = strength_counts.get(strength, 0) + 1
    
    print(f"Total passwords tested: {total_passwords}")
    print("\nStrength Distribution:")
    
    for strength, count in strength_counts.items():
        percentage = (count / total_passwords) * 100
        print(f"  {strength}: {count} ({percentage:.1f}%)")
    
    # Find best and worst passwords
    best_password = max(results, key=lambda x: x['score'])
    worst_password = min(results, key=lambda x: x['score'])
    
    print(f"\nBest Password: '{best_password['password']}' (Score: {best_password['score']})")
    print(f"Worst Password: '{worst_password['password']}' (Score: {worst_password['score']})")
    
    # Calculate average score
    avg_score = sum(result['score'] for result in results) / total_passwords
    print(f"Average Security Score: {avg_score:.1f}/11")

def interactive_password_checker():
    """
    Function for interactive password checking
    """
    print("\n🔍 INTERACTIVE PASSWORD CHECKER")
    print("=" * 40)
    print("Enter passwords to check (type 'quit' to exit)")
    
    while True:
        password = input("\nEnter password: ").strip()
        
        if password.lower() == 'quit':
            break
        
        if not password:
            print("Please enter a password")
            continue
        
        score, feedback = calculate_password_strength(password)
        strength, emoji = get_strength_level(score)
        
        print(f"\nPassword Strength: {emoji} {strength} (Score: {score}/11)")
        
        if feedback:
            print("Recommendations:")
            for suggestion in feedback:
                print(f"  • {suggestion}")
        else:
            print("✅ Excellent password!")

def main():
    """
    Main function to execute password security checking
    """
    print("🛡️  PASSWORD SECURITY CHECKER")
    print("=" * 50)
    
    # Test predefined passwords
    results = test_multiple_passwords()
    
    # Generate report
    generate_password_report(results)
    
    # Interactive checker
    interactive_password_checker()
    
    print("\n👋 Thank you for using the Password Security Checker!")

if __name__ == "__main__":
    main()
