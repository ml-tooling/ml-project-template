FROM ubuntu:16.04

# Install basics
RUN \
    apt-get update && \
    apt-get install sudo --yes && \
    apt-get install --yes --no-install-recommends  \
        wget \
        build-essential \
        cmake \
        ca-certificates \
        curl libcurl3 \
        zlibc zlib1g zlib1g-dev \
        # Fix problem with matplotlib using a GUI backend 
        libgl1-mesa-glx \ 
        software-properties-common \
        git \
        wget \
        locales \
        gcc \
        unzip && \
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen && \
    chmod -R a+rwx /usr/local/bin/ && \
    # Clean up
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /root/.cache/* && \
    rm -rf /tmp/*

# Configure git
RUN git config --global core.fileMode false && \
    git config --global http.sslVerify false

# Install Miniconda Python 3.6 & PyTorch cuda10
RUN curl -o ~/miniconda.sh -O  https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh  && \
     chmod +x ~/miniconda.sh && \
     ~/miniconda.sh -b -p /opt/conda && \
     rm ~/miniconda.sh && \
     /opt/conda/bin/conda install -y python=$PYTHON_VERSION cython typing && \
     /opt/conda/bin/conda clean -ya

ENV PATH /opt/conda/bin:$PATH

ENV LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    XDG_CACHE_HOME="/root/.cache/"

# Update python basics
RUN \
    conda install -y setuptools && \    
    pip install --upgrade pip && \
    pip install --upgrade Cython && \
    pip install --upgrade --no-cache-dir tqdm && \
    conda clean -ya


# # Set up paths & Install Studio library & other internal libs
ENV _RESOURCES_PATH="/resources"

RUN mkdir -p $_RESOURCES_PATH

# RUN \
#     mkdir -p $_RESOURCES_PATH && \
#     mkdir -p $DATA_ENVIRONMENT && \
#     chmod -R a+rwx $DATA_ENVIRONMENT


# Install Training Requirements
# RUN \
#     conda clean -ya

COPY docker-res/run.py "$_RESOURCES_PATH/"
CMD ["python", "/resources/run.py"]