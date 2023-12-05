import subprocess

# List of commands to execute
commands = [
    # Create Conda environment
    "mamba env create -f setup/ctd_env.yml",
    
    # Activate Conda environment
    "mamba activate ctdenv",
    
    # Install Jupyter kernel
    "python -m ipykernel install --user --name=ctdenv",
    
    # Open Jupyter Lab
    "jupyter lab",
]

# Function to run commands
def run_commands():
    for command in commands:
        subprocess.run(command, shell=True, check=True)

if __name__ == "__main__":
    run_commands()
