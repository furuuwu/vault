"""
the email sending part doesn't work

Error sending email: (535, b'5.7.8 Username and Password not accepted. 
For more information, go to\n5.7.8  https://support.google.com/mail/?p=BadCredentials 5b1f17b1804b1-43621546927sm116481815e9.1 - gsmtp')
"""

import smtplib
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Load credentials from the config.json file
def load_config():
    with open('config.json', 'r') as file:
        config = json.load(file)
    return config

# Email setup
config = load_config()

sender_email = config['email']
sender_password = config['password']
receiver_email = config['receiver_email']
smtp_server = config['smtp_server']
smtp_port = config['smtp_port']

# Function to send email
def send_email(subject, message):
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail(sender_email, receiver_email, email_message)
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

# Setup Selenium options
def setup_browser():
    options = Options()
    options.add_argument("--headless")  # Run browser in headless mode
    options.add_argument("--disable-gpu")  # Disable GPU acceleration for better performance
    options.add_argument("--window-size=1920x1080")  # Set window size
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Function to check the site for 500 errors
def check_for_500_error():
    try:
        # Initialize the browser
        driver = setup_browser()

        # Load the page
        url = "https://www.coursera.org/learn/sql-data-science/home/module/6"
        driver.get("url")

        # Wait for the page to load (you can add more complex waiting logic here)
        time.sleep(10)

        # Check the network logs for 500 errors
        logs = driver.get_log("browser")
        for entry in logs:
            if "500" in entry["message"]:
                print("500 Error detected in network request.")
                driver.quit()
                return True  # 500 error found

        print("No 500 errors detected.")
        driver.quit()
        return False  # No 500 error found

    except Exception as e:
        print(f"Error during site check: {e}")
        return True  # If there's any issue, assume the site is down

# Function to monitor the website
def monitor_website():
    while True:
        site_down = check_for_500_error()

        if site_down:
            subject = "500 Error Detected: Website Issues"
            message = f"The website is currently experiencing a 500 error. Please check the server logs and resolve the issue."
            send_email(subject, message)
        else:
            print("Website is functioning properly, no 500 errors detected.")
            subject = "Website is running well now!"
            message = f"The website is currently running well now! No 500 codes detected. Back tow work!"
            send_email(subject, message)

        # Wait for 60 seconds before checking again
        time.sleep(60)

# Start monitoring
monitor_website()
