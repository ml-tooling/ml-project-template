# Docker job template

------

## Input

## Pipeline

## Output

## Metrics

## Usage

Run the training job by executing this command with your chosen configuration:

```bash
docker run docker.wdf.sap.corp:51150/com.sap.sapai.ticketing/ticketing-training-job:latest
```

Note: for testing/debugging the job, make sure to set `DEBUG` to 1 (uses less data and smaller models).

### GPU training

Alternatively, the training can be accelerated using multiple GPUs (with IDs defined with `NVIDIA_VISIBLE_DEVICES`):

```bash
docker run --runtime=nvidia docker.wdf.sap.corp:51150/com.sap.sapai.ticketing/ticketing-training-job:latest
```

### Environment variables

The training job can be parametrized with environment variables. These can be defined by passing an [environment file](https://docs.docker.com/compose/compose-file/#env_file) via `--env-file=={env_file}` to `docker run`. To learn about available variables, click [here](#parameters).

Note, that you can also directly start the job with the Studio UI.

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
        <td>DATASET_KEY</td>
        <td>Key of the input dataset in CSV format.</td>
        <td>datasets/it_tickets.csv</td>
    </tr>
    <tr>
        <td>VECTORS_KEY</td>
        <td>Optional pretrained word vectors to used to improve training. See the above `Input` section for details. </td>
        <td>""</td>
    </tr>
    <tr>
        <td>PREPROCESSING</td>
        <td>Preprocessing level of input, one of {'fully', 'partly'}.</td>
        <td>fully</td>
    </tr>
    <tr>
        <td>SEP</td>
        <td>Separator character used for the input CSV file.</td>
        <td>;</td>
    </tr>
    <tr>
        <td>TEST_SIZE</td>
        <td>Relative size (percentage) of data used as a hold-out test set.</td>
        <td>0.05</td>
    </tr>
    <tr>
        <td>NUM_WORKERS</td>
        <td>Number of CPU cores used for processing.</td>
        <td>8</td>
    </tr>
    <tr>
        <td>OMP_NUM_THREADS</td>
        <td>Number of threads used by OpenMP (should equal to the no. of physical cores available).</td>
        <td>8</td>
    </tr>
    <tr>
        <td>NVIDIA_VISIBLE_DEVICES</td>
        <td>Cuda device IDs to use for PyTorch training (if available).</td>
        <td>all</td>
    <tr>
        <td>UPLOAD_EXPERIMENT</td>
        <td>Whether to upload the entire experiment folder to Studio (if connected).</td>
        <td>0</td>
    </tr>
    <tr>
        <td>DEPLOY_MODEL</td>
        <td>Whether to upload and deploy final model artifact (stacked ensemble, predicting categories in an end-to-end fashion).</td>
        <td>1</td>
    </tr>
    <tr>
        <td>SEED</td>
        <td>Global seed used for random numbers.</td>
        <td>42</td>
    </tr>
    <tr>
        <td>DEBUG</td>
        <td>Debug mode to test the entire pipeline with a subset of data and short trainings.</td>
        <td>0</td>
    </tr>
    <tr>
        <td colspan="3">Studio Configuration (will be automatically attached when started in Studio):</td>
    </tr>
    <tr>
        <td>STUDIO_ENDPOINT</td>
        <td>Endpoint URL of an ML Studio instance.</td>
        <td>(required)</td>
    </tr>
    <tr>
        <td>STUDIO_PROJECT</td>
        <td>Specified project of an ML Studio Instance.</td>
        <td>(required)</td>
    </tr>
    <tr>
        <td>STUDIO_API_TOKEN</td>
        <td>API Token to access the REST API of an ML Studio instance.</td>
        <td>(optional)</td>
    </tr>
    <tr>
        <td>EXPERIMENT_NAME</td>
        <td>Name of the experiment.</td>
        <td>Ticketing Model Training</td>
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
