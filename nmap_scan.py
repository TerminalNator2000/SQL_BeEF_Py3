# exploits/nmap_scan.py
import nmap
from core.config import load_config
import core.db_logger as db_logger

def run_scan():
    config = load_config()
    targets = config.get("nmap", {}).get("targets", [])
    scan_type = config.get("nmap", {}).get("scan_type", "-sS")

    nm = nmap.PortScanner()
    for target in targets:
        print(f"Running Nmap scan on {target} with options {scan_type}")
        scan_result = nm.scan(target, arguments=scan_type)
        db_logger.log_action("Nmap Scan", f"Scanned {target} - Results: {scan_result}")
        print(f"Results for {target}:\n", scan_result)
