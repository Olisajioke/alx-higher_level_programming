#!/usr/bin/python3
"""Defines a funtion that reads text."""


def read_file(filename=""):
    """Read a text file (UTF8) and print its content to stdout"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
