clean:
	rm -rf build dist
	find . -name '*.pyc' -exec rm \{\} \;

test:
	openfisca test --country-package openfisca_aotearoa openfisca_aotearoa/tests
