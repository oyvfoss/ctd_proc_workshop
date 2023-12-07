import time
import subprocess

# Create Conda environment
print('## CTD WORKSHOP: Starting Jupyter Lab session. If prompted, select "ctdenv" as kernel..\n')
time.sleep(4)
subprocess.run("conda run -n ctdenv jupyter lab", shell=True, check=True)
