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
        software-properties-common \
        git \
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
     /opt/conda/bin/conda install -y python=$PYTHON_VERSION typing && \
     /opt/conda/bin/conda clean -ya

ENV PATH /opt/conda/bin:$PATH

ENV LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    XDG_CACHE_HOME="/root/.cache/"

# Update python basics
RUN \
    conda install -y setuptools && \    
    pip install --upgrade pip


# Install training and app requirements
COPY docker-res/requirements.txt "/tmp/"
RUN pip install -r "tmp/requirements.txt" && \
    conda clean -ya

# # Set up paths for resources and data
ENV RESOURCES_PATH="/resources" \ 
     DATA_PATH="/data"
     
RUN \
    mkdir -p $RESOURCES_PATH && \
    mkdir -p $DATA_PATH && \
    chmod -R a+rwx $DATA_PATH


# Copy resource and run job
COPY docker-res/run.py "$RESOURCES_PATH/"
CMD ["python", "/resources/run.py"]
