#!/usr/bin/python3
import string
import random

def generate_filename():
    filename = ""
    for i in range(0, 4):
        filename += random.choice(string.ascii_letters)
    return filename
