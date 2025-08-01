FROM continuumio/miniconda3:25.3.1-1

# Install system dependencies (add any you need)
RUN apt-get update && apt-get install -y git make curl build-essential && rm -rf /var/lib/apt/lists/*
ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER=${NB_USER}
ENV NB_UID=${NB_UID}
ENV HOME=/home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}
# Set environment variables (adapt as needed)
ENV CESMROOT=/home/jovyan/CESM
ENV HOME=/home/jovyan
WORKDIR /home/jovyan

# Clone the CESM repo and run git-fleximod
RUN git clone https://github.com/CROCODILE-CESM/CESM.git $CESMROOT && \
    cd $CESMROOT && \
    ./bin/git-fleximod update

# Clone CrocoDash and checkout s3_zarr branch on submodule
RUN git clone --recurse-submodules https://github.com/CROCODILE-CESM/CrocoDash.git && \
    cd CrocoDash/CrocoDash/rm6 && \
    git fetch origin && \
    git checkout -b s3_zarr origin/s3_zarr

# Clone CrocoGallery
RUN git clone https://github.com/CROCODILE-CESM/CrocoGallery.git

# Copy environment.yml from CrocoDash and create conda env
RUN conda env create -f CrocoDash/environment.yml

# Activate conda environment and install extra Python packages from CrocoGallery
SHELL ["conda", "run", "-n", "CrocoDash", "/bin/bash", "-c"]
RUN pip install -r CrocoGallery/requirements.txt



RUN python3 -m pip install --no-cache-dir notebook jupyterlab

# Make sure the contents of our repo are in ${HOME}
COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}

# Create the environment
RUN conda env create -f environment.yml

# Activate the env and make it default
RUN echo "conda activate CrocoDash" >> ~/.bashrc
