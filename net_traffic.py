from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import threading
import queue

# Set up a queue to store new requests
request_queue = queue.Queue()

def print_requests():
    while True:
        try:
            request = request_queue.get(timeout=1)
            if request.response:
                print(f"URL: {request.url}")
                print(f"Method: {request.method}")
                print(f"Status Code: {request.response.status_code}")
                print("---")
        except queue.Empty:
            continue
        except Exception as e:
            print(f"Error processing request: {e}")

def intercept(request):
    request_queue.put(request)

# Set up the Chrome WebDriver with selenium-wire
options = {
    'disable_encoding': True,  # To get the raw response body
    'suppress_connection_errors': True  # To avoid connection error logs
}
driver = webdriver.Chrome(seleniumwire_options=options)

# Add the request interceptor
driver.request_interceptor = intercept

# URL of the webpage you want to interact with
url = 'https://ec.toranoana.jp/tora_r/ec/cot/ranking/daily/all/'

# Start the request printing thread
print_thread = threading.Thread(target=print_requests, daemon=True)
print_thread.start()

try:
    # Navigate to the webpage
    driver.get(url)

    print("Capturing network traffic. Press Ctrl-C to stop.")

    # Keep the browser open and continue capturing traffic
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping traffic capture...")

finally:
    # Close the browser
    driver.quit()
    print("Browser closed. Exiting...")