# Docker job template

------

## Description

## Usage

Run the training job by executing this command with your chosen configuration:

```bash
docker run training-job-template
```

Execute this command for interactive run mode:
```bash
docker run -it --entrypoint=/bin/bash training-job-template
```


### Environment variables

The training job can be parametrized with environment variables. These can be defined by passing an [environment file](https://docs.docker.com/compose/compose-file/#env_file) via `--env-file=={env_file}` to `docker run`. To learn about available variables, click [here](#parameters).
#
### Configuration

#### Parameters

The training job can be configured with following environment variables:

Example variables:

<table>
    <tr>
        <th>Variable</th>
        <th>Description</th>
        <th>Default</th>
    </tr>
     <tr>
        <td>TRAIN_SET_URL</td>
        <td>url to training data</td>
        <td></td>
    </tr>
    <tr>
        <td>TEST_SET_URL</td>
        <td>url to test data</td>
        <td></td>
    </tr>
        <td>SEED</td>
        <td>Global seed used for random numbers.</td>
        <td>42</td>
    </tr>
        <td colspan="3">AWS config </td>
    </tr>
    <tr>
        <td>acces_key</td>
        <td>AWS access key</td>
        <td>(required)</td>
    </tr>
    <tr>
        <td>S3 bucket</td>
        <td>url to S3 bucket containing data</td>
        <td>(required)</td>
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

In order to pull and push docker containers, the <DOCKER REPOSITORY> needs to be configured:

```bash
docker login <docker repo>
```

and your user and password to login.
