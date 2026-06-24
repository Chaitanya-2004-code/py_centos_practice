#!/usr/bin/env python3

def detect_injection(user_input):
    patterns = ["'", '"', "--", ";", " OR ", " AND ", "1=1", "DROP", "UNION", "SELECT"]
    for p in patterns:
        if p.lower() in user_input.lower():
            return "Potential Injection Detected"
    return "Input seems clean"

# Example
inp = input("Enter user input: ")
print(detect_injection(inp))
