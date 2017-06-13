# OpenFisca Country-Template

This repository is here to help you quickly bootstrap and use your own OpenFisca country package.

## Bootstrapping a country package

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

## Writing the legislation

The country whose law is modelled here has a very simple tax and benefit system.

- It has a flat rate tax whose rates increase every year.
- On the first of December, 2015, it introduced a basic income for all its citizens of age who have no income.
- On the first of December, 2016, it removed the income condition, providing all its adult citizens with a basic income.

These elements are described in different folders. All the modelling happens within the `openfisca_country_template` folder.

- The rates are in the `parameters` folder.
- The formulas are in the `variables` folder.
- This country template comes also with *reforms* in the `reforms` folder. This is optional: your country may exist without defining any reform.
    - In this country, there is [a reform project](./openfisca_country_template/reforms/modify_social_security_taxation.py) aiming to modify the social security taxation, deleting the first bracket, raising the intermediary ones and adding a new bracket with a higher tax rate of `40 %` for people earning more than `40000`. This reform project would apply starting from `2017-01-01`.

The files that are outside from the `openfisca_country_template` folder are used to set up the development environment.


## Installing

> We recommend that you [use a virtualenv](https://doc.openfisca.fr/for_developers.html#create-a-virtualenv) to install OpenFisca. If you don't, you may need to add `--user` at the end of all commands starting by `pip`.

To install your country package, run:

```
pip install -e ".[test]"
```

You can make sure that everything is working by running the provided tests:

```sh
make test
```

> [Learn more about tests](https://doc.openfisca.fr/coding-the-legislation/writing_yaml_tests.html)

Your country package is now installed and ready!


## Serving your country package with the OpenFisca web API

If you are considering building a web application, you can plug the OpenFisca web api to your country package.

First, install the OpenFisca web API:
```sh
pip install -e '.[api]'
```

Then run:
```sh
openfisca-serve --port 2000
```

You can make sure that the api is working by requesting:

```sh
curl "http://localhost:2000/api/2/formula/income_tax?salary=4000"
```

> [Learn more about the API](https://doc.openfisca.fr/openfisca-web-api/index.html)
