import subprocess
import time

# Create Conda environment
print('## CTD WORKSHOP: Updating the oceanograpy version in "ctdenv"..\n')
time.sleep(4)
subprocess.run('conda run -n ctdenv pip uninstall -y oceanograpy', shell=True, check=True)
subprocess.run("conda run -n ctdenv pip install --upgrade git+https://github.com/NPIOcean/oceanograpy.git", shell=True, check=True)

