import subprocess

def run(target, output_dir):
    output = subprocess.getoutput(f"nmap -sC -sV -T4 {target}")
    with open(f"{output_dir}/nmap.txt", "w") as f:
        f.write(output)
