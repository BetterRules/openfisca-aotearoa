clean:
	rm -rf build dist
	find . -name '*.pyc' -exec rm \{\} \;

test:
	openfisca-run-test --country-package openfisca_aotearoa openfisca_aotearoa/tests
