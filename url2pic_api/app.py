from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re

app = Flask(__name__)

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

def capture_screenshot(url):
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        total_height = driver.execute_script("return document.body.scrollHeight")
        driver.set_window_size(1920, total_height)

        screenshot = driver.get_screenshot_as_base64()
        driver.quit()
        return screenshot
    except Exception as e:
        print(f"Error capturing screenshot: {str(e)}")
        return None

@app.route('/capture', methods=['POST'])
def capture():
    if not request.is_json:
        return jsonify({'error': 'Invalid content-type. Use application/json'}), 400

    data = request.get_json()
    url = data.get('url')

    if not url or not re.match(r'^https?://', url):
        return jsonify({'error': 'Invalid URL'}), 400

    screenshot = capture_screenshot(url)

    if screenshot:
        return jsonify({'screenshot': screenshot})
    else:
        return jsonify({'error': 'Failed to capture screenshot'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)