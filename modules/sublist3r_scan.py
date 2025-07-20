import subprocess

def run(target, output_dir):
    output = subprocess.getoutput(f"sublist3r -d {target}")
    with open(f"{output_dir}/sublist3r.txt", "w") as f:
        f.write(output)
