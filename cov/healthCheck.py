import requests


def checkScript():
    try:
        requests.post("https://hc-ping.com/a030d45c-d183-4dad-8448-c1d00b902b87")
    except requests.RequestException as e:
        # Log ping failure here...
        print("Ping failed: %s" % e)