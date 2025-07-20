import subprocess

def run(target, output_dir):
    output = subprocess.getoutput(f"nslookup {target}")
    with open(f"{output_dir}/dns_lookup.txt", "w") as f:
        f.write(output)
