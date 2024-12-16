"""
the email sending part doesn't work

Less Secure Apps (Gmail): Gmail often blocks sign-ins from apps 
that it deems less secure (like Python's smtplib). 
"""

import smtplib
import requests
import time
import json

# Load credentials from the config.json file
def load_config():
    with open('config.json', 'r') as file:
        config = json.load(file)
    return config

# Website to monitor
# url = "https://example.com"  # Replace with the site URL you want to monitor
url = "https://www.coursera.org/learn/sql-data-science/home/module/6"

# Define the error codes to monitor (500, 403, 404)
error_codes = ['500', '403', '404']

# Load the email credentials from the config file
config = load_config()

# Email setup
"""
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'ricardo.filipe.saleiro.abreu@gmail.com'
sender_password = 'your_email_password'
receiver_email = 'ricardo.filipe.saleiro.abreu@gmail.com'
"""
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

# Function to check if the site is down
def is_site_down():
    try:
        response = requests.get(url)
        status_code = str(response.status_code)
        
        if status_code in error_codes:
            print(f"Error {status_code} detected.")
            return True  # Site is down (returns 500, 403, 404)
        else:
            print(f"Website is running fine with status code: {status_code}")
            return False  # Site is running fine
    except requests.RequestException as e:
        print(f"Error occurred: {e}")
        return True  # If request fails, consider the site as down

# Function to monitor the website and send email if down
def monitor_website():
    while True:
        if is_site_down():
            send_email(
                subject="Website is Down",
                message=f"The website {url} is currently down. Please check it!"
            )
        else:
            print("Website is up and running.")
        
        # Wait for 60 seconds before checking again
        time.sleep(60)

# Start monitoring
monitor_website()
