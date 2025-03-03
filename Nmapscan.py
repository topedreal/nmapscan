import subprocess

def nmap_scan(target=None, scan_type=None):
    """Perform an Nmap scan on a target using a selected scan type."""
    print("Welcome to the Scanner!\nNote: All scan types except -sT require sudo.")
    target = target or input("Enter target address: ").strip()
    
    scan_types = {"1": "-sS", "2": "-sT", "3": "-sU", "4": "-O"}
    
    if not scan_type:
        print("\nScan Types:")
        for key, value in scan_types.items():
            print(f"[{key}] {value}")
        while (choice := input("Select scan type (1-4): ").strip()) not in scan_types:
            print("Invalid choice! Enter a number between 1 and 4.")
        scan_type = scan_types[choice]
    
    print("\nScanning... Please wait.\n")
    result = subprocess.run(["nmap", scan_type, "-Pn", target], capture_output=True, text=True)
    if result.returncode:
        print("Error: Scan failed!\n", result.stderr)
        return
    
    filename = f"scan_results_{target.replace('.', '_')}.txt"
    with open(filename, "w") as file:
        file.write(result.stdout or "No output captured. Check Nmap installation and permissions.")
    
    print(f"Scan complete! Results saved to {filename}")

nmap_scan()
