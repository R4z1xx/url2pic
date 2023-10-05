import os
import sys
import requests
import base64

api_url = 'http://localhost:5000/capture'  # Replace with your actual API URL

if len(sys.argv) != 2:
    print("Usage: python url2pic.py <URL>")
    sys.exit(1)

input_url = sys.argv[1]

payload = {'url': input_url}

response = requests.post(api_url, json=payload)

if response.status_code == 200:
    try:
        screenshot_data = response.json()['screenshot']
        screenshot_bytes = base64.b64decode(screenshot_data)
        os.makedirs('screenshot', exist_ok=True)
        screenshot_path = os.path.join('screenshot', 'screenshot.png')
        with open(screenshot_path, 'wb') as file:
            file.write(screenshot_bytes)

        print(f'Screenshot saved as "{screenshot_path}"')
    except Exception as e:
        print(f'Error processing the response: {str(e)}')
else:
    print(f'Error: {response.status_code} - {response.text}')