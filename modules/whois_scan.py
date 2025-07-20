import subprocess

def run(target, output_dir):
    output = subprocess.getoutput(f"whois {target}")
    with open(f"{output_dir}/whois.txt", "w") as f:
        f.write(output)
