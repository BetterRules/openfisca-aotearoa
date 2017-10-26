clean:
	rm -rf build dist
	find . -name '*.pyc' -exec rm \{\} \;

test:
	flake8
	openfisca-run-test --country-package openfisca_country_template openfisca_country_template/tests
