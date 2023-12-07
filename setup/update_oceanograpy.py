import subprocess
import time

# Create Conda environment
print('## CTD WORKSHOP: Updating the oceanograpy version in "ctdenv"..\n')
time.sleep(4)
subprocess.run('pip uninstall oceanograpy', shell=True, check=True)
subprocess.run("pip install --upgrade git+https://github.com/NPIOcean/oceanograpy.git", shell=True, check=True)

