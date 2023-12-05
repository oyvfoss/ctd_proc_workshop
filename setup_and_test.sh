#!/bin/bash

# - Installs the ctdenv environment from *ctd_env.yml*
# - Activates the environment
# - Sets the environment to be the default kernel 
# - Opens a jupyter lab instance

# Create Conda environment
mamba env create -f setup/ctd_env.yml

# Activate Conda environment 
mamba activate ctdenv

# install Jupyter kernel
python -m ipykernel install --user --name=ctdenv

# Open jupyter lab
jupyter lab