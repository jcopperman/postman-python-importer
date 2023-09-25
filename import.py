import os
import json
import requests

# Create a folder for storing the generated Python scripts
if not os.path.exists("requests"):
    os.makedirs("requests")

# Load the Postman environment JSON
def load_environment_variables():
    environment_file = input("Do you want to import the environment variables? (y/n): ")
    if environment_file.lower() == 'y':
        environment_file_name = input("Enter the name of the environment JSON file (e.g., 'environment.json'): ")
        try:
            with open(environment_file_name, 'r') as file:
                environment_data = json.load(file)
                environment_variables = environment_data.get('values', [])
                return environment_variables
        except FileNotFoundError:
            print(f"File '{environment_file_name}' not found.")
    return []

# Load the Postman collection JSON
def load_postman_collection():
    collection_file = input("Do you want to import the Postman collection? (y/n): ")
    if collection_file.lower() == 'y':
        collection_file_name = input("Enter the name of the collection JSON file (e.g., 'collection.json'): ")
        try:
            with open(collection_file_name, 'r') as file:
                collection_data = json.load(file)
                return collection_data
        except FileNotFoundError:
            print(f"File '{collection_file_name}' not found.")
    return None

# Process a request and generate Python script
def process_request(request_info, environment_variables, index):
    request = request_info['request']
    url_data = request['url']
    method = request['method']
    headers = request.get('header', {})
    body = request.get('body', {})
    request_name = request_info['name']  # Extract request name

    # Extract the raw URL from the URL data
    raw_url = url_data.get('raw', '')

    # Substitute environment variables in the URL
    for variable in environment_variables:
        variable_name = variable['key']
        variable_value = variable['value']
        raw_url = raw_url.replace('{{' + variable_name + '}}', variable_value)

    # Create a Python script
    script = f"""
import requests

url = "{raw_url}"
method = "{method}"
headers = {headers}
body = {body}

response = requests.request(method, url, headers=headers, json=body)

print(response.status_code)
print(response.text)
"""

    # Save the Python script to a file with the request name-based name in the "requests" folder
    with open(f'requests/{request_name}.py', 'w') as script_file:
        script_file.write(script)

# Main function
def main():
    environment_variables = load_environment_variables()
    collection_data = load_postman_collection()

    if collection_data:
        # Process each request in the collection
        for index, request in enumerate(collection_data['item'], start=1):
            process_request(request, environment_variables, index)

        print("Requests processed and Python scripts generated in the 'requests' folder.")

if __name__ == "__main__":
    main()
