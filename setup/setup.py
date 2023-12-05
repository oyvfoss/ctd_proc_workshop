# This script does the following:


#import os
#import subprocess

#subprocess.run(['mamba', 'env', 'create', '-f', 'ctd_env.yml'])
#subprocess.run(['conda', 'activate', 'your_environment_name'])
#subprocess.run(['python', '-m', 'ipykernel', 'install', '--user', '--name=your_environment_name'])


import subprocess

subprocess.run(['mamba', 'env', 'create', '-f', 'setup/ctd_env.yml'])

# Use `conda run` to activate the environment
subprocess.run(['conda', 'run', '--no-capture-output', 'python', '-m', 'ipykernel', 'install', '--user', '--name=ctdenv'])

# Use `conda run` to activate the environment
subprocess.run(['conda', 'activate', 'ctdenv'])