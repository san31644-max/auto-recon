#!/bin/bash

echo "[*] Installing Python modules and tools..."
sudo apt update
sudo apt install -y nmap whois whatweb sublist3r theharvester nikto
pip3 install -r requirements.txt
echo "[+] Installation complete!"
