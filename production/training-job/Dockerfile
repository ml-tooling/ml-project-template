# use "nvidia/cuda:10.0-cudnn7-devel-ubuntu16.04" for GPU runtime 
FROM ubuntu:16.04 

# Python version
ARG PYTHON_VERSION=3.7

# Generate and set locals
# https://stackoverflow.com/questions/28405902/how-to-set-the-locale-inside-a-debian-ubuntu-docker-container#38553499
RUN \
    apt-get update && \
    apt-get install locales --yes && \
    # install locales-all?
    sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8

ENV LC_ALL="en_US.UTF-8" \
    LANG="en_US.UTF-8" \
    LANGUAGE="en_US:en"

# Install basics
RUN \
    apt-get update && \
    apt-get install sudo --yes && \
    apt-get install --yes --no-install-recommends  \
    wget \
    curl && \
    chmod -R a+rwx /usr/local/bin/

# Add tini for init
RUN wget --quiet https://github.com/krallin/tini/releases/download/v0.18.0/tini -O /tini && \
    chmod +x /tini

# Install Miniconda + some basics
ARG MINICONDA_URL=https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN \
     curl -o ~/miniconda.sh -O $MINICONDA_URL && \
     chmod +x ~/miniconda.sh && \
     ~/miniconda.sh -b -p /opt/conda && \
     rm ~/miniconda.sh && \
     /opt/conda/bin/conda install -y python=$PYTHON_VERSION setuptools typing setuptools && \
     /opt/conda/bin/pip install --upgrade pip && \
     /opt/conda/bin/conda clean -ya

ENV PATH /opt/conda/bin:$PATH

# Install training requirements
COPY docker-res/requirements.txt "/tmp/"
RUN pip install -r "tmp/requirements.txt"


# Set *predefined* paths/variables
ENV TRAIN_SET_URL="" \
    TEST_SET_URL="" \
    RESOURCES_PATH="/resources" \ 
    DATA_PATH="/data" \ 
    LOG_PATH="/logs" 
        
RUN \
    mkdir -p $RESOURCES_PATH && \
    mkdir -p $DATA_PATH && \
    chmod -R a+rwx $DATA_PATH

# Set *configurable* variables
ENV N_EPOCHS="10" \ 
    SEED="1337" \
    NVIDIA_VISIBLE_DEVICES="all" \
    OMP_NUM_THREADS="8" 
    
# Copy resources
COPY docker-res/run.py "$RESOURCES_PATH/"

# Run run.py via tini
ENTRYPOINT ["/tini", "--", "python", "/resources/run.py"]