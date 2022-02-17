# Install Conda
apt-get update
apt-get install -y wget && rm -rf /var/lib/apt/lists/*
wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh

# Setup conda environment
conda env create -f journals2data/src/journals2data/docker_conda_config.yml
conda clean -a -y

# Install Firefox and Geckodriver
apt-get update
apt-get install -y firefox
bash journals2data/cmd/install_gecko_docker.sh

# Clean cache and unused dependencies to reduce the image size
rm -r /root/.cache/pip
apt-get remove -y wget
apt-get clean
apt-get autoclean
apt-get autoremove -y

