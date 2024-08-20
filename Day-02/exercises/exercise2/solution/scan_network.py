Python

import nmap

# Initialize the Nmap scanner
nm = nmap.PortScanner()

# Define the target network
target_network = '192.168.1.0/24'

# Scan the network
print(f"Scanning network: {target_network}")
nm.scan(hosts=target_network, arguments='-sP')

# Print the results
for host in nm.all_hosts():
    print(f"Host: {host} ({nm[host].hostname()})")
    print(f"State: {nm[host].state()}")
    if 'tcp' in nm[host]:
        for port in nm[host]['tcp']:
            print(f"Port: {port}\tState: {nm[host]['tcp'][port]['state']}")
