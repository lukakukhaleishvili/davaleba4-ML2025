# TOR over VPN Traffic Detector

This Python tool detects potential TOR traffic encapsulated within a VPN tunnel by analyzing network packets.

## Features

- Captures live packets from a specified network interface
- Flags packets that use ports commonly associated with TOR nodes
- Assumes VPN encapsulation over common TCP/UDP protocol

For this project, I ran the script on a Wi-Fi interface. Specifically, on Windows, I used the following command to capture packets over the Wi-Fi network:
python davaleba4.py -i Wi-Fi
This command specifies the Wi-Fi network interface to monitor. It is important to ensure that the Wi-Fi interface is active and properly configured to allow packet sniffing. If you're using a different network interface, make sure to replace Wi-Fi with the correct interface name for your system.
  
## is_tor_over_vpn Function
The is_tor_over_vpn function checks whether a captured packet could potentially be part of a TOR over VPN communication based on matching ports. If such traffic is detected, the function flags it as suspicious and returns True.

## sniff_packets Function
The sniff_packets function starts packet sniffing on the specified network interface and analyzes each packet using the is_tor_over_vpn function.

##  Main Script Execution
This block of code allows the user to run the script from the command line and specify the network interface on which to capture packets. Once the interface is selected, the packet sniffing process starts.


