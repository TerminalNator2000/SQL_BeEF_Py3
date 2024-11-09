# exploits/beef.py
import requests
from core.config import load_config
import core.db_logger as db_logger

def run_exploit():
    config = load_config()
    target_url = config.get("beef", {}).get("target_url")
    payload = config.get("beef", {}).get("payload")

    if not target_url or not payload:
        print("Error: Missing target URL or payload in config.")
        return

    print(f"Sending payload to {target_url}")
    response = requests.get(target_url, params={"payload": payload})
    db_logger.log_action("BeEF Exploit", f"Sent payload to {target_url} - Status Code: {response.status_code}")
    print(f"Exploit response status: {response.status_code}")
