import subprocess
import os
import time

current_dir = os.path.dirname(os.path.abspath(__file__))

refresh_script = os.path.join(current_dir, "refresh_jsons.py")
generators_folder = os.path.join(current_dir, "Generators")

print("Running refresh_jsons.py...")
subprocess.run(["python3", refresh_script], check=True)
print("JSON refresh completed.")
time.sleep(1) 

print("Running generator scripts...")
for script in os.listdir(generators_folder):
    if script.endswith(".py"):
        script_path = os.path.join(generators_folder, script)
        print(f"Running {script}...")
        subprocess.run(["python3", script_path], check=True)
        time.sleep(0.5)  

print("All generator scripts have been executed.")
