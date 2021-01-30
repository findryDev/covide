import requests
import os
from dotenv import load_dotenv
load_dotenv()


def checkScript():
    try:
        requests.post(f"{os.getenv('healthCheckKey')}")
    except requests.RequestException as e:
        # Log ping failure here...
        print("Ping failed: %s" % e)
