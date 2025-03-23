import os
import json
import requests
import boto3
from datetime import datetime

# AWS Configuration
SENDER_EMAIL = "murugudujaswanthi@gmail.com"  
RECIPIENT_EMAIL = "jaswanthi.murugudu04@gmail.com" 
S3_BUCKET = "your-weather-data-bucket"  

# OpenWeather API Configuration
WEATHER_API_KEY = "5a7324e7d0c8a05288f855abdc75d75f" 
LATITUDE = "12.9716"  # Bangalore
LONGITUDE = "77.5946"
WEATHER_API_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LATITUDE}&lon={LONGITUDE}&appid={WEATHER_API_KEY}&units=metric"

# AWS Clients
s3_client = boto3.client('s3')
ses_client = boto3.client("ses", region_name="us-east-1")  # ✅ Update AWS region if needed

def fetch_weather():
    """Fetches weather data from OpenWeather API"""
    response = requests.get(WEATHER_API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("❌ Error fetching weather data:", response.json())
        return None

def save_to_s3(data):
    """Saves weather data as JSON in S3"""
    file_name = f"weather_reports/weather_{datetime.now().strftime('%Y-%m-%d')}.json"
    s3_client.put_object(Bucket=S3_BUCKET, Key=file_name, Body=json.dumps(data))
    return file_name

def send_email(weather_data):
    """Formats weather data and sends an email via AWS SES"""
    subject = f"🌤 Daily Weather Report for {weather_data['name']}"
    body = f"""
    <html>
    <body>
        <h2>Weather Report for {weather_data['name']}</h2>
        <p><b>Temperature:</b> {weather_data['main']['temp']}°C</p>
        <p><b>Condition:</b> {weather_data['weather'][0]['description']}</p>
        <p>Have a great day! 😊</p>
    </body>
    </html>
    """
    
    response = ses_client.send_email(
        Source=SENDER_EMAIL,
        Destination={"ToAddresses": [RECIPIENT_EMAIL]},
        Message={
            "Subject": {"Data": subject},
            "Body": {"Html": {"Data": body}}
        }
    )
    return response

def lambda_handler(event, context):
    """AWS Lambda entry point"""
    weather_data = fetch_weather()
    if weather_data:
        file_name = save_to_s3(weather_data)
        send_email(weather_data)
        return {"status": "Success", "s3_file": file_name}
    else:
        return {"status": "Error fetching weather data"}
