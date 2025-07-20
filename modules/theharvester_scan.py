import subprocess

def run(target, output_dir):
    output = subprocess.getoutput(f"theHarvester -d {target} -b all")
    with open(f"{output_dir}/theharvester.txt", "w") as f:
        f.write(output)
