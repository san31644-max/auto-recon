#!/usr/bin/env python3
from rich.console import Console
from utils.banner import show_banner
from modules import whois_scan, dns_lookup, nmap_scan, whatweb_scan, sublist3r_scan, theharvester_scan, nikto_scan
import os

console = Console()

def main():
    os.system("clear")
    show_banner()
    
    target = console.input("[bold cyan]Enter Target Domain or IP: [/bold cyan]").strip()
    if not target:
        console.print("[bold red]Error: Target cannot be empty! Exiting.[/bold red]")
        return

    output_dir = f"reports/{target}"
    os.makedirs(output_dir, exist_ok=True)

    console.print("\n[bold magenta]Choose Modules to Run:[/bold magenta]")
    console.print("[1] WHOIS")
    console.print("[2] DNS Lookup")
    console.print("[3] Nmap")
    console.print("[4] WhatWeb")
    console.print("[5] Sublist3r")
    console.print("[6] theHarvester")
    console.print("[7] Nikto")
    console.print("[8] All\n")

    choice = console.input("[bold green]Enter choice (comma-separated or '8' for All): [/bold green]")
    options = [opt.strip() for opt in choice.split(',')]

    try:
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
    except Exception as e:
        console.print(f"[bold red]Error during scanning: {e}[/bold red]")
        return

    console.print(f"\n[bold green]Recon Complete. Check 'reports/{target}' for outputs.[/bold green]")
    console.print("[bold yellow]Thank you for using AutoReconX! - Sandaru Dinusha[/bold yellow]")

if __name__ == "__main__":
    main()
