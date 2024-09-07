import subprocess


def run_arp_command(command):
    try:
        result = subprocess.run(command)
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

def display_arp_cache():
    output = run_arp_command(["arp", "-a"])
    if output:
        print(output)

def add_arp_entry():
    ip = input("Enter IP address: ")
    mac = input("Enter MAC address: ")
    output = run_arp_command(["arp", "-s", ip, mac])
    if output is not None:
        print("ARP entry added successfully.")

def delete_arp_entry():
    ip = input("Enter IP address to delete: ")
    output = run_arp_command(["arp", "-d", ip])
    if output is not None:
        print("ARP entry deleted successfully.")

def main_menu():
    while True:
        print("\nARP Menu:")
        print("1. Display ARP Table")
        print("2. Add ARP entry")
        print("3. Delete ARP entry")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            display_arp_cache()
        elif choice == "2":
            add_arp_entry()
        elif choice == "3":
            delete_arp_entry()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
