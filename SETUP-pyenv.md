## Setup Aotearoa Open Fisca in pyenv

### Step 1: Install pyenv

```sh
curl https://pyenv.run | bash
```

### Step 2: Clone the repo

```sh
git clone https://github.com/ServiceInnovationLab/openfisca-aotearoa.git
cd openfisca-aotearoa
```

### Step 3: Install python using pyenv
We want to use the exact version of python we use on the official servers

```sh
 pyenv install < .python-verion
 python --version # You should have python 3.7 or better installed on your computer.
```

### If `ModuleNotFoundError: No module named '_ctypes'`
>
>     sudo apt-get update
>     sudo apt-get install libffi-dev
>
More problems? [Try the instructions here](https://stackoverflow.com/questions/27022373/python3-importerror-no-module-named-ctypes-when-using-value-from-module-mul#41310760)


#### Step 4: Install Dev dependencies

```sh
pip install -r requirements.txt
```

:tada: This OpenFisca Country Package is now installed and ready!

## Step 5: Running the tests

```sh
pip install -e ".[test]"
make test
```
> [Learn more about tests](https://openfisca.org/doc/coding-the-legislation/writing_yaml_tests.html)

:tada: This OpenFisca Aotearoa Package is now installed and ready!

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
