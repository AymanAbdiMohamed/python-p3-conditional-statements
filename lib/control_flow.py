#!/usr/bin/env python3

def admin_login(username, password):
    """
    Return 'Access granted' if username and password match the admin credentials,
    case-insensitive for username. Otherwise, return 'Access denied'.
    """
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"


def hows_the_weather(temperature):
    """
    Return a weather description based on temperature, matching test expectations.
    """
    if temperature < 0:
        return "It's freezing!"
    elif 0 <= temperature <= 33:
        return "It's brisk out there!"
    elif 34 <= temperature <= 65:
        return "It's a little chilly out there!"
    elif 66 <= temperature <= 85:
        return "It's perfect out there!"
    else:
        return "It's too dang hot out there!"


def fizzbuzz(num):
    """
    Return 'Fizz' for multiples of 3, 'Buzz' for multiples of 5,
    'FizzBuzz' for multiples of both 3 and 5, otherwise return the number.
    """
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


def calculator(operation, num1, num2):
    """
    Perform basic arithmetic operations: add, subtract, multiply, divide.
    Returns the result or prints "Invalid operation!" and returns None if operation is invalid.
    """
    if operation in ("add", "+"):
        return num1 + num2
    elif operation in ("subtract", "-"):
        return num1 - num2
    elif operation in ("multiply", "*"):
        return num1 * num2
    elif operation in ("divide", "/"):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        print("Invalid operation!")
        return None
