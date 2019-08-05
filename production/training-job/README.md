# Docker job template

## Description


## Usage 

Run the job by executing this command with your chosen configuration, exposing port 5000 to the outside world:

```bash
docker run -p 5000:5000 training-job-template
```

To enable the Nvidia Container Runtime for GPU-acceleration, execute:

```bash
docker run --runtime=nvidia training-job-template
```

Execute this command for interactive run mode:
```bash
docker run -it --entrypoint=/bin/bash training-job-template
```

More options:

* publish the container's port 5000 via to `host_port` usinng `-p {host_port}:5000`
* for testing purposes (fast execution), run with `--env-file==test.env`.
* run in detached mode usingn `-d`


### Environment variables

The training job can be parametrized with environment variables. These can be defined by passing an [environment file](https://docs.docker.com/compose/compose-file/#env_file) via `--env-file=={env_file}` to `docker run`. To learn about available variables, click [here](#parameters).

### Configuration

#### Parameters

The training job can be configured with following environment variables:


<table>
    <tr>
        <th>Variable</th>
        <th>Description</th>
        <th>Default</th>
    </tr>
    <tr>
        <td colspan="3"><b>Training Config:</d></td>
    </tr>
    <tr>
        <td>N_EPOCHS</td>
        <td>no. training epochs</td>
        <td>10</td>
    </tr>
    <tr>
        <td>SEED</td>
        <td>Global seed used for random numbers.</td>
        <td>42</td>
    </tr>
    <tr>
        <td colspan="3"><b>Computation Config:</d></td>
    </tr>
    <tr>
        <td>MAX_NUM_THREADS</td>
        <td>Controls which GPUs CUDA applications will see. By default, all GPUs from the host are used. You can either use all, none, or specify a comma-separated list of device IDs (e.g. 0,1). You can find out the list of available device IDs by running nvidia-smi on the host machine.</td>
        <td>auto</td>
    </tr>
    <tr>
        <td>NVIDIA_VISIBLE_DEVICES</td>
        <td>(GPU only) Controls which GPUs will be accessible by the job. By default, all GPUs from the host are used. You can either use all, none, or specify a comma-separated list of device IDs (e.g. 0,1). You can find out the list of available device IDs by running nvidia-smi on the host machine.</td>
        <td>all</td>
    </tr>
        <tr>
        <td>CUDA_VISIBLE_DEVICES</td>
        <td>(GPU only) Controls which GPUs will be accessible by the job. By default, all GPUs that the job has access to will be visible. To restrict the job, provide a comma-separated list of internal device IDs (e.g. 0,2) based on the available devices within the container job (run nvidia-smi). In comparison to NVIDIA_VISIBLE_DEVICES, the job user will still able to access other GPUs by overwriting this configuration from within the container.</td>
        <td>all</td>
    </tr>
    <tr>
        <td colspan="3"><b>Cloud Config:</d></td>
    </tr>
   
</table>

#### Proxy

If a proxy is required, you can pass it via the `http_proxy`and `no_proxy` environment varibales. For example: `--env http_proxy=<server>:<port>`

#### Docker Configuration

You can find more ways of configuration about [docker run](https://docs.docker.com/engine/reference/commandline/run) and [docker service create](https://docs.docker.com/engine/reference/commandline/service_create) in the official Docker documentation.

## Develop

### Requirements

- Python 3, Maven, Docker

### Build

Execute this command in the project root folder to build the docker container:

```bash
python build.py --version={MAJOR.MINOR.PATCH-TAG}
```

The version has to be provided. The version format should follow the [Semantic Versioning](https://semver.org/) standard (MAJOR.MINOR.PATCH). For additional script options:

```bash
python build.py --help
```

### Deploy

Execute this command in the project root folder to push the container to the configured docker registry:

```bash
python build.py --deploy --version={MAJOR.MINOR.PATCH-TAG}
```

The version has to be provided. The version format should follow the [Semantic Versioning](https://semver.org/) standard (MAJOR.MINOR.PATCH). For additional script options:

```bash
python build.py --help
```

#### Configure Docker Repository

In order to pull and push docker containers, a Docker registry  needs to be configured:

```bash
docker login <server>
```

and your user and password to login.
