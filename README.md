# Secure Endpoint Example using Flask

This repository demonstrates how to create a secure API endpoint using the Flask framework in Python. The secure endpoint is protected using JWT (JSON Web Tokens) for authentication.

## Getting Started

### Prerequisites

Make sure you have Python and Flask installed on your system. You can install Flask using the following command:


### Installation

1. Clone this repository or download the ZIP file.

2. Navigate to the project directory in your terminal.

3. Run the Flask application:


## Usage

The `endpoint.py` file contains a Flask application with a secure endpoint. The endpoint is protected using JWT for authentication. To access the secure endpoint, you'll need to follow these steps:

1. **Login**: Make a POST request to `/api/login` (for demonstration purposes, this example uses a simple login process without actual authentication).

2. **Obtain Token**: The server will respond with a JSON object containing an access token. You'll need this token to access the secure endpoint.

3. **Access Secure Endpoint**: Make a GET request to `/api/secure` and include the access token in the headers using the format `Authorization: Bearer YOUR_ACCESS_TOKEN`.

```python
# Example Request
headers = {
 'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
}

response = requests.get('http://localhost:5000/api/secure', headers=headers)


