# exploits/sqlmap_wrapper.py
import subprocess
from core.config import load_config
import core.db_logger as db_logger

def run_sqlmap():
    config = load_config()
    target_url = config.get("sqlmap", {}).get("target_url")
    options = config.get("sqlmap", {}).get("options", "")

    if not target_url:
        print("Error: Missing target URL in config for SQLMap.")
        return

    sqlmap_command = f"sqlmap -u {target_url} {options}"
    print(f"Running SQLMap command: {sqlmap_command}")
    process = subprocess.Popen(sqlmap_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        print("SQLMap Output:\n", stdout.decode())
        db_logger.log_action("SQLMap", stdout.decode())
    else:
        print("SQLMap Error:\n", stderr.decode())
        db_logger.log_action("SQLMap Error", stderr.decode())
