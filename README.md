# TOR over VPN Traffic Detector

This Python tool detects potential TOR traffic encapsulated within a VPN tunnel by analyzing network packets.

## Features

- Captures live packets from a specified network interface
- Flags packets that use ports commonly associated with TOR nodes
- Assumes VPN encapsulation over common TCP/UDP protocol

For this project, I ran the script on a Wi-Fi interface. Specifically, on Windows, I used the following command to capture packets over the Wi-Fi network:
python davaleba4.py -i Wi-Fi
This command specifies the Wi-Fi network interface to monitor. It is important to ensure that the Wi-Fi interface is active and properly configured to allow packet sniffing. If you're using a different network interface, make sure to replace Wi-Fi with the correct interface name for your system.
  

Limitations
 - Simplified detection: This script only checks for common TOR ports. It is not a comprehensive detection tool and will miss more sophisticated methods of TOR-over-VPN traffic obfuscation

