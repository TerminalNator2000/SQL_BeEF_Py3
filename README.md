
# Kali Exploit Tools - Python 3 Package

## Overview

Kali Exploit Tools is a Python 3 package that provides a set of network exploitation and scanning tools, including **Nmap** scans, **BeEF**-like payload delivery, and **SQLMap** for automated SQL injection testing. Each tool is modular and can be configured to target specific hosts or endpoints, making it easy to use for penetration testing and security research.

## Features

- **Nmap Scans**: Perform customizable Nmap scans on target hosts.
- **BeEF-like Exploits**: Deliver JavaScript payloads to specified URLs, simulating BeEF-like exploitation.
- **SQLMap Integration**: Automate SQLMap commands directly from Python for SQL injection exploitation.


## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)


## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/kali_exploit_tools.git
   cd kali_exploit_tools
   ```

2. **Install Dependencies**:
   Install all required Python packages using `pip`.
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   Add any sensitive data or API keys in `config/secrets.env`.


## Configuration

### Main Configuration File (`config/config.yaml`)

Customize your tool settings in `config/config.yaml`. This file defines default parameters for each tool.

Example `config.yaml`:

```yaml
nmap:
  targets: ["192.168.1.1", "192.168.1.2"]
  scan_type: "-sS -Pn"

beef:
  target_url: "http://example.com"
  payload: "alert('BeEF attack')"

sqlmap:
  target_url: "http://example.com/vulnerable"
  options: "--batch --dbs"


### Environment Variables (`config/secrets.env`)

Store any API keys, tokens, or secret information in `secrets.env`. This file is loaded at runtime for secure access to sensitive data.

Example `secrets.env`:

```plaintext
API_KEY=your_api_key_here
SECRET_KEY=your_secret_key_here
```


## Usage

To run the application, simply execute `main.py`. You’ll be presented with a menu to select which tool to use.

```bash
python main.py
```

### Interactive Menu Options

1. **Run Nmap Scan**: Executes an Nmap scan on the targets defined in `config.yaml`.
2. **Run BeEF Exploit**: Sends a JavaScript payload to a specified target URL.
3. **Run SQLMap**: Automates SQLMap commands for SQL injection testing.
4. **Exit**: Exit the application.

### Running Individual Tools

Each tool can also be run directly by executing its script in the `exploits` directory.

```bash
python exploits/nmap_scan.py   # Run Nmap scan
python exploits/beef.py        # Run BeEF exploit
python exploits/sqlmap_wrapper.py  # Run SQLMap
```



## Project Structure

```plaintext
kali_exploit_tools/
├── exploits/
│   ├── beef.py                # BeEF-like exploitation functionalities
│   ├── nmap_scan.py           # Nmap scanning functionalities
│   ├── sqlmap_wrapper.py      # SQLMap integration and automation
├── core/                      
│   ├── config.py              # Configuration management
│   ├── db_logger.py           # Logging and database interactions
│   ├── network_utils.py       # Utility functions for network tasks
├── config/                     
│   ├── config.yaml            # Configuration file for targets and options
│   ├── secrets.env            # Environment file for sensitive data
├── reports/                   # Folder for generated reports
├── main.py                    # Main script to run the tools interactively
├── requirements.txt           # Python dependencies
├── setup.py                   # Package setup file
└── README.md                  # Documentation
```

---

## Contributing

Contributions are welcome! Feel free to submit pull requests, report issues, or suggest features. When contributing, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request to the `main` branch with a description of your changes.







