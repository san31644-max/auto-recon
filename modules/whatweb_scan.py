import subprocess

def run(target, output_dir):
    output = subprocess.getoutput(f"whatweb {target}")
    with open(f"{output_dir}/whatweb.txt", "w") as f:
        f.write(output)
