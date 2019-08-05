# Production

This is the space for production code: tested Python libs, jobs and services.


## Develop

### Requirements

- Python 3, Docker

### Docker Build

Execute this command in the project root folder to build this project and the respective docker container:

```bash
python build.py
```

This script compiles the project, assembles the various JAR artifacts (executable service, client, sources) and builds a docker container with the assembled executable jar. For additional script options:

```bash
python build.py --help
```

To only compile the Java artifacts (for development):

```bash
mvn clean package
```

### Deploy

Execute this command in the project root folder to deploy all assembled Java artifacts to the configured maven repository and push all docker containers to the configured docker registry:

```bash
python build.py --deploy --version={MAJOR.MINOR.PATCH-TAG}
```

For deployment, the version has to be provided. The version format should follow the [Semantic Versioning](https://semver.org/) standard (MAJOR.MINOR.PATCH). For additional script options:

```bash
python build.py --help
```

#### Configure Docker Repository

```bash
docker login docker-repository
```

### Dev Guidelines

#### Code Style

Our coding guideline for source code in the Java is based on the [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html). For any code-style related questions, please refer to the [linked guide](https://google.github.io/styleguide/javaguide.html).

We also have predefined code formatting settings for IntelliJ which can be downloaded [here](https://sap-my.sharepoint.com/personal/lukas_masuch_sap_com/_layouts/15/guestaccess.aspx?guestaccesstoken=X00sJxNAAJv9lTRnUX2zfJ2iDo7YGyoqmLAS%2bYS68W4%3d&docid=2_114ced53bd3d94684ab15521e206b4343&rev=1) (add .jar as extension as OneDrive doesn’t allow uploading jar files).

#### Git Workflow

Our git branching for all repositories is based on the [Git-Flow standard](https://datasift.github.io/gitflow/IntroducingGitFlow.html). Please go trough the [linked introduction](https://datasift.github.io/gitflow/IntroducingGitFlow.html), and visit [here](http://nvie.com/posts/a-successful-git-branching-model) and [here](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) for more information.

#### Build Versioning

Our build versioning for all projects is based on the [Semantic Versioning specification](https://semver.org/). For any versioning-related questions, please refer to the [linked guide](https://semver.org/). In additon to the MAJOR.MINOR.PATCH format, a `SNAPSHOT` tag will be attached to the version for all development builds (based on the [Maven versioning standard](https://docs.oracle.com/middleware/1212/core/MAVEN/maven_version.htm)). As define in  Git-Flow, the build version is also used as tag for releases on the master branch.
