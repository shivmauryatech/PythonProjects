# This file includes utility functions like loggings, helpers, decorators
# utils.py

from functools import wraps
from datetime import datetime
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # To supress warning

LOG_FILE = 'data/app.log'

def log_action(action):
    """
    Decorator to log actions performed in TaskManager.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"[{timestamp}] ACTION: {action} | FUNC: {func.__name__}\n"

            with open(LOG_FILE, 'a') as f:
                f.write(log_message)

            return result
        return wrapper
    return decorator





def get_motivational_quote():
    """Fetches a motivational quote from an API."""
    try:
        response = requests.get("https://api.quotable.io/random", timeout=5, verify=False) # verify=False to bypass ssl verification
        response.raise_for_status()  # Raises an error if response code is 4xx or 5xx

        data = response.json()
        quote = data.get("content", "No quote found.")
        author = data.get("author", "Unknown")

        print(f"\n💡 Quote of the moment:\n\"{quote}\"\n— {author}\n")

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Could not fetch quote. Reason: {e}")