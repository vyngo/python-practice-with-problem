import requests

url = "http://125.234.115.178:8000/judge/2/upload_file/"

files = {'file': ('ex1_cost_function.py', open('ex1_cost_function.py', 'rb'))}

response = requests.request("POST", url, files=files)

print('Ex1 Score: ' + response.text)

url = "http://125.234.115.178:8000/judge/3/upload_file/"

files = {'file': ('ex2_derivative_function.py', open('ex2_derivative_function.py', 'rb'))}

response = requests.request("POST", url, files=files)

print('Ex2 Score: ' + response.text)

url = "http://125.234.115.178:8000/judge/4/upload_file/"

files = {'file': ('ex3_update_value.py', open('ex3_update_value.py', 'rb'))}

response = requests.request("POST", url, files=files)

print('Ex3 Score: ' + response.text)
