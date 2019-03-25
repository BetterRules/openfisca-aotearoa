## Setup OpenFisca Aotearoa to run in docker

## Run the application using Docker

- [Install Docker](https://www.docker.com/get-started).
- Build the docker image: `docker build -t openfisca-aotearoa`
- Run the image: `docker run -it -p 5000:5000 openfisca-aotearoa`

## Serve OpenFisca Aotearoa with the OpenFisca Web API

If you are considering building a web application, you can use the packaged OpenFisca Web API.

To serve the Openfisca Web API locally, run:

```sh
openfisca serve --port 5000
```

To read more about the `openfisca serve` command, check out its [documentation](https://openfisca.readthedocs.io/en/latest/openfisca_serve.html).

You can make sure that your instance of the API is working by requesting:

```sh
curl "http://localhost:5000/spec"
```

This endpoint returns the [Open API specification](https://www.openapis.org/) of your API.

:tada: OpenFisca Aotearoa is now served by the OpenFisca Web API! To learn more, go to the [OpenFisca Web API documentation](https://openfisca.org/doc/openfisca-web-api/index.html)
