# OpenFisca country package template

This repository is here to help you quickly bootstrap and use your own OpenFisca country package.


## Bootstrapping a country package


First, create a directory and set up a git repository: 

```sh
COUNTRY_NAME=france # for instance

mkdir openfisca-$COUNTRY_NAME
cd openfisca-$COUNTRY_NAME
git init
```

Then, download this template code:
```sh
git pull https://github.com/openfisca/country-template.git
```

Finally, remove all references to `openfisca_country_template` in the code base:

```sh
CAPITALIZED_COUNTRY_NAME=France # for instance

sed -i '' -e "s/country_template/$COUNTRY_NAME/g" "MANIFEST.in"
sed -i '' -e "s/country_template/$COUNTRY_NAME/g" "openfisca_country_template/base.py"
sed -i '' -e "s/country_template/$COUNTRY_NAME/g" "openfisca_country_template/model.py"
sed -i '' -e "s/Country-Template/$CAPITALIZED_COUNTRY_NAME/g" "setup.py"
mv openfisca_country_template openfisca_$COUNTRY_NAME
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

First, install the OpenFisca wep api:
```sh
pip install openfisca-web-api
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
