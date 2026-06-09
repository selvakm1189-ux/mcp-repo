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

def sum_list(numbers):
    """
    Sum all numbers in a list and return the result.
    
    Args:
        numbers (list): List of integers or floats
    
    Returns:
        int or float: Sum of all numbers in the list
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list is empty
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if len(numbers) == 0:
        raise ValueError("List cannot be empty")
    return sum(numbers)

def main():
    print("Hello, World!")
    print("Welcome to mcp-repo!")
    
    # Test the sum_three_integers function
    result = sum_three_integers(5, 10, 15)
    print(f"Sum of 5 + 10 + 15 = {result}")
    
    # Test the sum_list function
    numbers = [1, 2, 3, 4, 5, 10]
    list_sum = sum_list(numbers)
    print(f"Sum of {numbers} = {list_sum}")

if __name__ == "__main__":
    main()
