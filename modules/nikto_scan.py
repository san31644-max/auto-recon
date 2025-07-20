import subprocess

def run(target, output_dir):
    output = subprocess.getoutput(f"nikto -h {target}")
    with open(f"{output_dir}/nikto.txt", "w") as f:
        f.write(output)
