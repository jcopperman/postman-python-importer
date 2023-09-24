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
    url = request_info['url']
    method = request_info['method']
    headers = request_info.get('header', {})
    body = request_info.get('body', {})
    
    # Convert dictionaries to strings
    url = str(url)
    method = str(method)
    headers = json.dumps(headers, indent=4)
    body = json.dumps(body, indent=4)
    
    # Substitute environment variables
    for variable in environment_variables:
        variable_name = variable['key']
        variable_value = variable['value']
        url = url.replace('{{' + variable_name + '}}', variable_value)
        headers = headers.replace('{{' + variable_name + '}}', variable_value)
        body = body.replace('{{' + variable_name + '}}', variable_value)

    # Create a Python script
    script = f"""
import requests

url = "{url}"
method = "{method}"
headers = {headers}
body = {body}

response = requests.request(method, url, headers=headers, json=body)

print(response.status_code)
print(response.text)
"""

    # Save the Python script to a file in the "requests" folder
    with open(f'requests/request_{index}.py', 'w') as script_file:
        script_file.write(script)

# Main function
def main():
    environment_variables = load_environment_variables()
    collection_data = load_postman_collection()

    if collection_data:
        # Process each request in the collection
        for index, request in enumerate(collection_data['item'], start=1):
            process_request(request['request'], environment_variables, index)

        print("Requests processed and Python scripts generated in the 'requests' folder.")

if __name__ == "__main__":
    main()
