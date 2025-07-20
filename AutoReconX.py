#!/usr/bin/env python3
from rich.console import Console
from utils.banner import show_banner
from modules import whois_scan, nmap_scan, dns_lookup, whatweb_scan, sublist3r_scan, theharvester_scan, nikto_scan
import os

console = Console()

def main():
    os.system("clear")
    show_banner()
    target = console.input("[bold cyan]Enter Target Domain or IP: [/bold cyan]")

    output_dir = f"reports/{target}"
    os.makedirs(output_dir, exist_ok=True)

    console.print("\n[bold magenta]Choose Modules to Run:[/bold magenta]")
    print("[1] WHOIS\n[2] DNS Lookup\n[3] Nmap\n[4] WhatWeb\n[5] Sublist3r\n[6] theHarvester\n[7] Nikto\n[8] All\n")

    choice = input("Enter choice (comma-separated or '8' for All): ")
    options = choice.split(',')

    if "1" in options or "8" in options:
        whois_scan.run(target, output_dir)
    if "2" in options or "8" in options:
        dns_lookup.run(target, output_dir)
    if "3" in options or "8" in options:
        nmap_scan.run(target, output_dir)
    if "4" in options or "8" in options:
        whatweb_scan.run(target, output_dir)
    if "5" in options or "8" in options:
        sublist3r_scan.run(target, output_dir)
    if "6" in options or "8" in options:
        theharvester_scan.run(target, output_dir)
    if "7" in options or "8" in options:
        nikto_scan.run(target, output_dir)

    console.print(f"\n[bold green]Recon Complete. Check 'reports/{target}' for outputs.[/bold green]")

if __name__ == "__main__":
    main()
