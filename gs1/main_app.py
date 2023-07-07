import requests

# Specific Record 
# URL = "http://127.0.0.1:8000/student_info/1"

# All record
URL = "http://127.0.0.1:8000/student_info/"

result = requests.get(url=URL)
print(result.json())