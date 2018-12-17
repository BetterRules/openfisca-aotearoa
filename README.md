# OpenFisca Aotearoa

[![CircleCI](https://circleci.com/gh/ServiceInnovationLab/openfisca-aotearoa/tree/master.svg?style=svg)](https://circleci.com/gh/ServiceInnovationLab/openfisca-aotearoa/tree/master)
[![Waffle.io - Columns and their card count](https://badge.waffle.io/ServiceInnovationLab/openfisca-aotearoa.svg?columns=all)](https://waffle.io/ServiceInnovationLab/openfisca-aotearoa)


## Writing the Legislation

Aotearoa New Zealand's legislation as code utilising Open Fisca.
Early development phase.
Please also read [the wiki](https://github.com/ServiceInnovationLab/openfisca-aotearoa/wiki) as a way of introduction.

The files that are outside from the `openfisca_aotearoa` folder are used to set up the development environment.

## Deploy to your own platform-as-a-service

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Install Instructions for Users and Contributors

This package requires [Python 3](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/) .

Supported platforms:
- GNU/Linux distributions (in particular Debian and Ubuntu);
- Mac OS X;
- Microsoft Windows (we recommend using [ConEmu](https://conemu.github.io/) instead of the default console).

Other OS should work if they can execute Python and NumPy.

### Setting-up a Virtual Environment with Pew

We recommend using a [virtual environment](https://virtualenv.pypa.io/en/stable/) (abbreviated as "virtualenv") with a virtualenv manager such as [pew](https://github.com/berdario/pew).

- A [virtualenv](https://virtualenv.pypa.io/en/stable/) is a project specific environment created to suit the needs of the project you are working on.
- A virtualenv manager, such as [pew](https://github.com/berdario/pew), lets you easily create, remove and toggle between several virtualenvs.

To install pew, launch a terminal on your computer and follow these instructions:

```sh
python --version # You should have python 3.7 or better installed on your computer.
# If not, visit http://www.python.org to install it and install pip as well.
```

```sh
pip install --upgrade pip
pip install pew  # if asked, answer "Y" to the question about modifying your shell config file.
```
To set-up and create a new a virtualenv named **openfisca** running python3.7:

```sh
pew new openfisca --python=python3.7
```

The virtualenv you just created will be automatically activated. This means you will operate in the virtualenv immediately. You should see a prompt resembling this:
```sh
Installing setuptools, pip, wheel...done.
Launching subshell in virtual environment. Type 'exit' or 'Ctrl+D' to return.
```
Additional information:
- Exit the virtualenv with `exit` (or Ctrl-D).
- Re-enter with `pew workon openfisca`.

:tada: You are now ready to install this OpenFisca Country Package!

We offer 2 install procedures. Pick procedure A or B below depending on how you plan to use this Country Package.

### A. Minimal Installation (Pip Install)

Follow this installation if you wish to:
- run calculations on a large population;
- create tax & benefits simulations;
- write an extension to this legislation (e.g. city specific tax & benefits);
- serve your Country Package with the OpenFisca Web API.

For more advanced uses, head to the [Advanced Installation](#advanced-installation-git-clone).

#### Install this Country Package with Pip Install

Inside your virtualenv, check the prerequisites:

```sh
python --version  # should print "Python 3.xx".
#if not, make sure you pass the python version as an argument when creating your virtualenv
```

```sh
pip --version  # should print at least 9.0.
#if not, run "pip install --upgrade pip"
```
Install the Country Package:

```sh
pip install openfisca_aotearoa
```

:tada: This OpenFisca Country Package is now installed and ready!

#### Next Steps

- To learn how to use OpenFisca, follow our [tutorials](https://openfisca.org/doc/getting-started.html).
- To serve this Country Package, serve the [OpenFisca web API](#serve-your-country-package-with-the-openFisca-web-api).

Depending on what you want to do with OpenFisca, you may want to install yet other packages in your virtualenv:
- To install extensions or write on top of this Country Package, head to the [Extensions documentation](https://openfisca.org/doc/contribute/extensions.html).
- To plot simulation results, try [matplotlib](http://matplotlib.org/).
- To manage data, check out [pandas](http://pandas.pydata.org/).

### B. Advanced Installation (Git Clone)

Follow this tutorial if you wish to:
- create or change this Country Package's legislation;
- contribute to the source code.

#### Clone OpenFisca Aotearoa with Git

First of all, make sure [Git](https://www.git-scm.com/) is installed on your machine.

Set your working directory to the location where you want OpenFisca Aotearoa cloned.

Inside your virtualenv, check the prerequisites:

```sh
python --version  # should print "Python 3.7x".
#if not, make sure you pass the python version as an argument when creating your virtualenv
```

```sh
pip --version  # should print at least 18.0.
#if not, run "pip install --upgrade pip"
```
Clone OpenFisca Aotearoa on your machine:

```sh
git clone https://github.com/ServiceInnovationLab/openfisca-aotearoa.git
cd openfisca-aotearoa
pip install -e .
```

You can make sure that everything is working by running the provided tests:

```sh
pip install -e ".[test]"
openfisca test openfisca_aotearoa/tests
```
> [Learn more about tests](https://openfisca.org/doc/coding-the-legislation/writing_yaml_tests.html)

:tada: This OpenFisca Aotearoa Package is now installed and ready!

#### Next Steps

- To write new legislation, read [the wiki](https://github.com/ServiceInnovationLab/openfisca-aotearoa/wiki) along with the OpenFisca [Coding the legislation](https://openfisca.org/doc/coding-the-legislation/index.html) section.
- To contribute to the code, read our [contribution doc](https://github.com/ServiceInnovationLab/openfisca-aotearoa/blob/master/CONTRIBUTING.md).

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

## Ongoing setup updates.

If you update openfisca-aotearoa after some time of having it installed you may need to update the underlying dependant libraries.

In particular to update the underlying openfisca-core library if the openfisca-aotearoa dependancies have updated, run:

```sh
pip install OpenFisca-Core --upgrade --upgrade-strategy only-if-needed
```

:tada: You should now be up to date again and able to continue development.