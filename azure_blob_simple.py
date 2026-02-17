import requests
from datetime import datetime

# Your Azure Blob Storage URL
BLOB_URL = "https://byggeboligblobstorage.blob.core.windows.net/"

try:
    # Make a GET request to the blob storage
    response = requests.get(BLOB_URL)
    
    # Get current UTC time
    utc_now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    # Print HTTP return code and UTC time
    print(f"HTTP Return Code: {response.status_code}")
    print(f"Date and Time (UTC): {utc_now}")
    
except Exception as e:
    utc_now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"Error: {str(e)}")
    print(f"Date and Time (UTC): {utc_now}")