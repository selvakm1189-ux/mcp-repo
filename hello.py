#!/usr/bin/env python3
"""
Hello World Program
A simple script to print hello to the console.
"""

def sum_three_integers(a, b, c):
    """
    Sum three integers and return the result.
    
    Args:
        a (int): First integer
        b (int): Second integer
        c (int): Third integer
    
    Returns:
        int: Sum of the three integers
    """
    return a + b + c

def main():
    print("Hello, World!")
    print("Welcome to mcp-repo!")
    
    # Test the sum function
    result = sum_three_integers(5, 10, 15)
    print(f"Sum of 5 + 10 + 15 = {result}")

if __name__ == "__main__":
    main()
