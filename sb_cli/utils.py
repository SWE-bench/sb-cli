import requests

def verify_response(response):
    if response.status_code != 200:
        try:
            payload = response.json()
        except ValueError:
            payload = None
        if isinstance(payload, dict):
            message = payload.get("message", "No message provided")
        else:
            message = response.reason or "No message provided"
        raise requests.RequestException(f"API request failed with status code {response.status_code}: {message}")
