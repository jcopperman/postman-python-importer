# Postman Collection to Python Script Converter

A Python script that converts Postman collections into Python scripts for making HTTP requests. This script automates the process of generating Python code from Postman collections, making it easier to transition from Postman to Python-based API testing and automation.

## Overview

This Python script allows you to import Postman environment variables and collections in JSON format and convert them into Python scripts. It automates the process of creating Python scripts for making HTTP requests, including handling environment variables and request parameters.

## Usage

### Prerequisites

Before using this script, ensure that you have the following prerequisites installed on your system:

- Python 3.x
- Pip (Python package manager)

### Installation

1. Clone the repository or download the script to your local machine:

### Where to Place Postman Files
Place your exported Postman environment variables and collections JSON files in the same directory as the Python script (postman_converter.py). Ensure that the JSON files have appropriate names, and be ready to provide their names when prompted by the script.

### Dependencies
The following Python libraries are required for this script:
`requests`: Used for making HTTP requests.