FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN \
    apt-get update && \
    apt-get install sudo --yes && \
    apt-get install --yes --no-install-recommends git && \
    chmod -R a+rwx /usr/local/bin/ && \
     # Clean up
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /root/.cache/* && \
    rm -rf /tmp/*

# Configure git
RUN git config --global core.fileMode false && \
    git config --global http.sslVerify false

# Install utils
RUN \
      pip install --no-cache-dir --upgrade git+https://github.com/ml-tooling/ml-project-template#subdirectory=production/python-utils-lib

COPY ./model /model
COPY ./app /app
