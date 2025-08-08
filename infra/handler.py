# Create a Lambda function
# The Lambda will be a simple 'fetch my trading 212 data'
# We'll connnect this Lambda to API Gateway so that React can call it

# handler.py is the python file containing the Lambda function
# AWS Lambda will call a specific function inside this file every time its triggered
# By default, AWS Lambda will look for a function called 'lambda_handler'

import json # Provides a way to encode and decode JSON data, which is commonly used for data interchange in web applications
import os # Provides way of using operating system dependent functionality, such as accessing environment variables, working with file paths and performing file and directory operationsl
import requests # Allows you to send HTTP requests, which is useful for interacting with web services and APIs

# from dotenv import load_dotenv # Used to load environment variables from a .env file, which is useful for managing configuration settings in a secure way

# load_dotenv() # Used to load the environement variable from a .env file (ALWASY ADD .ENV TO .GITIGNORE!!!!!!!)

def lambda_handler(event, context):
    trading_212_api_key = os.environ.get('TRADING212_API_KEY')

    

    if not trading_212_api_key:
        return {
            'statusCode': 500,
            'body': 'API key not set!!!'
        }

    url = "https://demo.trading212.com/api/v0/equity/portfolio"
    headers = {"Authorization": f"{trading_212_api_key}"}
    print("API Key:", trading_212_api_key[:10])  # Just first few chars for safety
    print("URL:", url)
    print("Headers:", headers)
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        return {
            "statusCode": 200,
            "body": json.dumps(data)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

