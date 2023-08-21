import requests

login_url = "http://127.0.0.1:5000/api/login"
secure_url = "http://127.0.0.1:5000/api/secure"

response = requests.post(login_url)

if response.status_code == 200:
    access_token = response.json().get("access_token")
    
    secure_headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(secure_url, headers=secure_headers)

    if response.status_code == 200:
        message = response.json().get("message")
        assert(message == "This is a safe endpoint")
        print("It worked!")
    else:
        message = response.json().get("msg")
        print(f"Response code {response.status_code}, message {message}")    
else:
    print(f"Login failed")