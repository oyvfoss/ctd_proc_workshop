import subprocess

# Create Conda environment
print('## CTD WORKSHOP: Installing a mamba environment called "ctdenv" (this may take a minute or two)..\n')
subprocess.run("sleep 4", shell=True, check=True)
subprocess.run("mamba env create -f setup/ctd_env.yml", shell=True, check=True)

# Install Jupyter kernel
print('## CTD WORKSHOP: Installing jupyter kernel for running Jupyter Lab in the "ctdenv" environment.\n')
print('(disregard the debugger warning - it does not matter for our purposes).')
subprocess.run("sleep 4", shell=True, check=True)
subprocess.run("conda run -n ctdenv python -m ipykernel install --user --name=ctdenv", shell=True, check=True)

# Open Jupyter Lab
print('## CTD WORKSHOP: Success - hooray! Opening Jupyter Lab (a browser window should now pop up!)')
print('(To cancel the Jupyter instance, press CTRL+C)')
subprocess.run("conda run jupyter lab setup/Test_your_setup.ipynb", shell=True, check=True)