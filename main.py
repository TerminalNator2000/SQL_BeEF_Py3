# main.py
from exploits import beef, nmap_scan, sqlmap_wrapper
from core import config, db_logger

def main_menu():
    print("\nSelect an action:")
    print("1. Run Nmap Scan")
    print("2. Run BeEF Exploit")
    print("3. Run SQLMap")
    print("4. Exit")

def run():
    config.load_env_vars()
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            nmap_scan.run_scan()
        elif choice == "2":
            beef.run_exploit()
        elif choice == "3":
            sqlmap_wrapper.run_sqlmap()
        elif choice == "4":
            print("Exiting the tool.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run()
