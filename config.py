# core/config.py
import yaml
import os

def load_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

def load_env_vars():
    with open("config/secrets.env") as f:
        for line in f:
            if line.strip() and not line.startswith("#"):
                key, value = line.strip().split("=", 1)
                os.environ[key] = value
