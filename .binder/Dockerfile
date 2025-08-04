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

# Clone CrocoGallery and move only the gallery/ folder
RUN git clone --depth=1 https://github.com/CROCODILE-CESM/CrocoGallery.git /tmp/cg && \
    mv /tmp/cg/gallery ${HOME}/gallery && \
    rm -rf /tmp/cg
# Make sure the contents of our repo are in ${HOME}
COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}