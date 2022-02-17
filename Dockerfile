FROM ubuntu:20.04
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

# Add source directory
COPY src/journals2data journals2data/src/journals2data
COPY logs journals2data/logs
COPY out journals2data/out

COPY cmd/install_gecko_docker.sh journals2data/cmd/install_gecko_docker.sh
COPY cmd/docker_image_setup.sh journals2data/cmd/docker_image_setup.sh

# Install dependencies and setup Conda environment
RUN bash journals2data/cmd/docker_image_setup.sh
SHELL ["conda", "run", "-n", "j2d", "/bin/bash", "-c"]

# Python Script
COPY src/scripts/docker_run.py journals2data/src/docker_run.py
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "j2d", "python", "/journals2data/src/docker_run.py"]
