FROM ghcr.io/crocodile-cesm/crocogallery:latest
RUN python3 -m pip install --no-cache-dir notebook jupyterlab
ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}
ARG CACHE_BUST=1
# Clone CrocoGallery and move only the gallery/ folder
RUN git clone --depth=1 https://github.com/CROCODILE-CESM/CrocoGallery.git /tmp/cg && \
    python3 /tmp/cg/code/set_cesm_path.py /workspace/CESM && \
    python3 /tmp/cg/code/inject_paths.py && \
    mv /tmp/cg/gallery /workspace/gallery && \
    rm -rf /tmp/cg
# Make sure the contents of our repo are in ${HOME}
COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}

# ✅ Also fix ownership for /workspace/CESM
RUN chown -R ${NB_UID} /workspace/CESM
USER ${NB_USER}

# Register the conda environment as a Jupyter kernel
RUN conda run -n CrocoDash python -m ipykernel install --user --name CrocoDash --display-name "Python (CrocoDash)"