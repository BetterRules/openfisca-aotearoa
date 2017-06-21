# OpenFisca Country-Template

This repository is here to help you quickly bootstrap and use your own OpenFisca country package.

## Bootstrapping your Country Package

This set of instructions will create your own copy of this boilerplate directory and customise it to the country you want to work on:

```sh
COUNTRY_NAME=France  # set the name of your country here; you should keep all capitals, and replace any spaces in the name by underscores
URL=https://github.com/openfisca/openfisca-france  # set here the URL of the repository where you will publish your code.

lowercase_country_name=$(echo $COUNTRY_NAME | tr '[:upper:]' '[:lower:]')

git clone https://github.com/openfisca/country-template.git  # download this template code

# remove all references to `openfisca_country_template` in the code base:
mv country-template openfisca-$lowercase_country_name
cd openfisca-$lowercase_country_name
git remote remove origin
sed -i '' '3,27d' README.md  # Remove these instructions lines
sed -i '' "s|country_template|$lowercase_country_name|g" README.md setup.py check-version-bump.sh Makefile `find openfisca_country_template -type f`
sed -i '' "s|Country-Template|$COUNTRY_NAME|g" README.md setup.py check-version-bump.sh .github/PULL_REQUEST_TEMPLATE.md CONTRIBUTING.md `find openfisca_country_template -type f`
sed -i '' "s|https://github.com/openfisca/openfisca-country-template|$URL|g" setup.py
mv openfisca_country_template openfisca_$lowercase_country_name
```

## Writing the Legislation

The country whose law is modelled here has a very simple tax and benefit system.

- It has a flat rate tax whose rates increase every year.
- On the first of December, 2015, it introduced a basic income for all its citizens of age who have no income.
- On the first of December, 2016, it removed the income condition, providing all its adult citizens with a basic income.

These elements are described in different folders. All the modelling happens within the `openfisca_country_template` folder.

- The rates are in the `parameters` folder.
- The formulas are in the `variables` folder.
- This country package comes also with *reforms* in the `reforms` folder. This is optional: your country may exist without defining any reform.
    - In this country, there is [a reform project](./openfisca_country_template/reforms/modify_social_security_taxation.py) aiming to modify the social security taxation, deleting the first bracket, raising the intermediary ones and adding a new bracket with a higher tax rate of `40 %` for people earning more than `40000`. This reform project would apply starting from `2017-01-01`.

The files that are outside from the `openfisca_country_template` folder are used to set up the development environment.

## Packaging your Country Package for Distribution

Country packages are python distributions. To distribute your package via `pip install`, follow the steps given by the [Python Packaging Authority](https://python-packaging-user-guide.readthedocs.io/distributing/).

## Install Instructions for Users and Contributors

This package requires [Python 2.7](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/) .

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
python -V # You should have python 2.7.9 or better installed on your computer.
# If not, visit http://www.python.org to install it and install pip as well.
```

```sh
pip install --upgrade pip
pip install pew  # if asked, answer "Y" to the question about modifying your shell config file.
```
To set-up and create a new a virtualenv named **openfisca** running python2.7:

```sh
pew new openfisca --python=python2.7
```

The virtualenv you just created will be automatically activated. This means you will operate in the virtualenv immediately. You should see a prompt resembling this :
```sh
Installing setuptools, pip, wheel...done.
Launching subshell in virtual environment. Type 'exit' or 'Ctrl+D' to return.
```
Additional information :
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
python --version  # should print "Python 2.7.xx".
#if not, make sure you pass the python version as an argument when creating your virtualenv
```

```sh
pip --version  # should print at least 9.0.
#if not, run "pip install --upgrade pip"
```
Install the Country Package:

```sh
pip install openfisca_country_template
```

:tada: This OpenFisca Country Package is now installed and ready!

#### Next Steps

- To learn how to use OpenFisca, follow our [tutorials](https://doc.openfisca.fr/getting-started.html).
- To serve this Country Package, serve the [OpenFisca web API](#serve-your-country-package-with-the-openFisca-web-api).

Depending on what you want to do with OpenFisca, you may want to install yet other packages in your virtualenv:
- To install extensions or write on top of this Country Package, head to the [Extensions documentation](https://doc.openfisca.fr/contribute/extensions.html).
- To plot simulation results, try [matplotlib](http://matplotlib.org/).
- To manage data, check out [pandas](http://pandas.pydata.org/).

### B. Advanced Installation (Git Clone)

Follow this tutorial if you wish to:
- create or change this Country Package's legislation;
- contribute to the source code.

#### Clone this Country Package with Git

First of all, make sure [Git](https://www.git-scm.com/) is installed on your machine.

Set your working directory to the location where you want this OpenFisca Country Package cloned.

Inside your virtualenv, check the prerequisites:

```sh
python --version  # should print "Python 2.7.xx".
#if not, make sure you pass the python version as an argument when creating your virtualenv
```

```sh
pip --version  # should print at least 9.0.
#if not, run "pip install --upgrade pip"
```
Clone this Country Package on your machine:

```sh
git clone https://github.com/openfisca/openfisca-country-template.git
cd openfisca-country-template
```

You can make sure that everything is working by running the provided tests:

```sh
pip install -e ".[test]"
make test
```
> [Learn more about tests](https://doc.openfisca.fr/coding-the-legislation/writing_yaml_tests.html)

:tada: This OpenFisca Country Package is now installed and ready!

#### Next Steps

- To write new legislation, read the [Coding the legislation](https://doc.openfisca.fr/coding-the-legislation/index.html) section to know how to write legislation.
- To contribute to the code, read our [Contribution Guidebook](https://doc.openfisca.fr/contribute/index.html).

## Serve this Country Package with the OpenFisca Web API

If you are considering building a web application, you can plug the OpenFisca Web API to your Country Package.

First, install the OpenFisca web API:
- if you completed the minimal install, run: 
    ```sh
    pip install openfisca-country-template[api]
    ```
- if you completed the advanced install, run:
    ```sh
    pip install -e '.[api]'
    ```

Then serve the Openfisca Web API locally:

```sh
openfisca-serve --port 2000
```

You can make sure that your instance of the API is working by requesting:

```sh
curl "http://localhost:2000/api/1/swagger"
```

:tada: This OpenFisca Country Package is now served by the OpenFisca Web API! To learn more, go to the [OpenFisca Web API documentation](https://doc.openfisca.fr/openfisca-web-api/index.html)
