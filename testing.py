import numpy as np
import pandas as pd
import requests
import json
from datetime import datetime, timedelta, timezone
import locale
from requests.auth import HTTPBasicAuth


def token_olish():

  url = "http://80.80.218.184:8080/users/login"

  payload = json.dumps({
    "username": "mdmdev",
    "password": "mdmdev"
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  return response.text

def upload_file(token):
    # url = 'http://test.app.akfa.onlinesavdo.com/goods'
    url = 'http://test.app.akfa.onlinesavdo.com/ajax-goods-excelUpload'
    # token = 'your_bearer_token'
    file_path ='D:\\Users\\Muzaffar.Tursunov\\Desktop\\test.xlsx'
    # Open the file you want to send in binary mode
    with open(file_path, 'rb') as file:
        # Create a dictionary to hold the file
        # files = {'file': file}
        
        # Set the headers for authentication
        # headers = {'Authorization': f'Bearer {token}'}
        sheet_name = 'Goods'

        files = {
        'file_upload': (file_path.split('/')[-1], file, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        }
        data = {
            'sheetname': sheet_name  # This should match the 'name' attribute of the sheet name input
        }
        
        # Send a POST request with the file and authentication
        response = requests.post(url, files=files, data=data)

    # Print the response from the server
    print(response.status_code)
    print(response)

