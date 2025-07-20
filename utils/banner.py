# utils/banner.py
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def show_banner():
    banner = r"""
      ___        __         ______                                  
     /   | _____/ /_  ___  / ____/___  ____ ___  ____  ____  _____
    / /| |/ ___/ __ \/ _ \/ /   / __ \/ __ `__ \/ __ \/ __ \/ ___/
   / ___ / /__/ / / /  __/ /___/ /_/ / / / / / / /_/ / /_/ (__  ) 
  /_/  |_\___/_/ /_/\___/\____/\____/_/ /_/ /_/ .___/ .___/____/  
                                            /_/   /_/            
    """

    author = Text()
    author.append("\nAutoReconX - Automated Recon Tool\n", style="bold magenta")
    author.append("By: Sandaru Dinusha\n", style="bold cyan")
    author.append("GitHub: https://github.com/san31644-max\n", style="underline blue")
    author.append("\nScan smarter. Scan faster. Stay safe.\n", style="italic green")

    console.print(Panel.fit(banner, border_style="bright_blue"))
    console.print(Panel.fit(author, border_style="bright_magenta"))
