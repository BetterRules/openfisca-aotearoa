# OpenFisca country package template

This repository is here to help you quickly bootstrap and use your own OpenFisca country package.


## Bootstrapping a country package


This set of instructions will create your own copy of this boilerplate directory and customise it to the country you want to work on:

```sh
COUNTRY_NAME=France  # set the name of your country here; you should keep all capitals, and replace any spaces in the name by underscores

lowercase_country_name=$(echo $COUNTRY_NAME | tr '[:upper:]' '[:lower:]')

git clone https://github.com/openfisca/country-template.git  # download this template code

# remove all references to `openfisca_country_template` in the code base:
mv country-template openfisca-$lowercase_country_name
cd openfisca-$lowercase_country_name
git remote remove origin
sed -i '' "s/country_template/$lowercase_country_name/g" MANIFEST.in openfisca_country_template/base.py openfisca_country_template/model.py
sed -i '' "s/Country-Template/$COUNTRY_NAME/g" setup.py
mv openfisca_country_template openfisca_$lowercase_country_name
rm README.md
```

## Installation

> We recommend that you [use a virtualenv](https://doc.openfisca.fr/for_developers.html#create-a-virtualenv) to install OpenFisca. If you don't, you may need to add `--user` at the end of all commands starting by `pip`.

To install your country package, run:

```
pip install -e .
```

You can make sure that everything is working by running the provided test:

```sh
openfisca-run-test openfisca_$COUNTRY_NAME/test.yaml
```

> [Learn more about tests](https://doc.openfisca.fr/coding-the-legislation/writing_yaml_tests.html)

Your country package is now installed and ready!

## Serving your country package with the OpenFisca web API

If you are considering building a web application, you can plug the OpenFisca web api to your country package.

First, install the OpenFisca web API:
```sh
pip install -e '.[api]'
```

Then run : 
```sh
openfisca-serve --port 2000
```

You can make sure that the api is working by requesting:

```sh
curl "http://localhost:2000/api/2/formula/income_tax?salary=4000"
```

> [Learn more about the api](https://doc.openfisca.fr/openfisca-web-api/index.html)
