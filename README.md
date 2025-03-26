# AWS Lambda Weather Automation  

This project automates daily weather report emails using **AWS Lambda, S3, SES, Step Functions, and CloudWatch**.

## Features  
✅ Fetches real-time weather data from OpenWeather API 
✅ Saves weather data to AWS S3   
✅ Sends a weather report via AWS SES  
✅ Fully automated workflow using AWS Step Functions   
✅ CloudWatch triggers to run daily   

---

##  Project Structure  
This repository contains:  
- **`notebook_1_jaswanthi_murugudu_ipynb.py`** → Fetches weather data from OpenWeather API  and plots the graph
- **`notebook_2_jaswanthi_murugudu.py`** → Saves weather data to an AWS S3 bucket  and Sends an email with the weather report using AWS SES  
- **`notebook_3_jaswanthi_murugudu.py.py`** → Take the input and Sends an email with the weather report using AWS SES  
- **`step_function_definition.json`** → AWS Step Function to orchestrate execution  

---

##  Deployment Steps  

### **AWS Setup**  
1. **Create an S3 Bucket** → `your-weather-data-bucket`  
2. **Verify Email in AWS SES**  
3. **Create an IAM Role** → Attach policies:  
   - `AmazonS3FullAccess`  
   - `AmazonSESFullAccess`  
   - `AWSLambdaBasicExecutionRole`  

---

### ** Upload & Deploy Lambda Functions**  
1. **Zip each Lambda function**:  
   ```sh
   zip notebook_1_jaswanthi_murugudu_ipynb.py.zip notebook_1_jaswanthi_murugudu_ipynb.py.py
   zip notebook_2_jaswanthi_murugudu.py.zip notebook_2_jaswanthi_murugudu.py
   zip notebook_3_jaswanthi_murugudu.zip notebook_3_jaswanthi_murugudu.py
