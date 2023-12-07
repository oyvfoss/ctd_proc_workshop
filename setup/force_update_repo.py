import subprocess
import time

# Create Conda environment
print('## CTD WORKSHOP: Forcing update to the most recent remote version of the "ctd_proc_workshop" project folder..\n')
time.sleep(2)
subprocess.run('conda run -n ctdenv git fetch origin', shell=True, check=True)
subprocess.run("conda run -n ctdenv git reset --hard origin/master", shell=True, check=True)

