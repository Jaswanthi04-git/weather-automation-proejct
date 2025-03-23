# AWS Lambda Weather Automation

This project automates daily weather report emails using **AWS Lambda, SES, S3 & Step Functions**.

## Features
- Fetches weather data from OpenWeather API 
- Saves reports to S3 for reference
- Sends daily weather emails via AWS SES 
- Fully automated with AWS Step Functions 
- Uses CloudWatch for scheduling 

## Deployment Steps

### ** AWS Setup**
- **Create an S3 Bucket:** `your-weather-data-bucket`
- **Verify Email in AWS SES**
- **Create IAM Role:** Attach policies `AmazonS3FullAccess`, `AmazonSESFullAccess`, `AWSLambdaBasicExecutionRole`

### ** Deploy Lambda Using AWS CLI**
```sh
zip -r lambda_function.zip lambda_function.py
aws lambda update-function-code --function-name WeatherEmailLambda --zip-file fileb://lambda_function.zip
