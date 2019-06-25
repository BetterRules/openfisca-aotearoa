#!/bin/sh

set -e
if ! git rev-parse "$(python setup.py --version)" 2>/dev/null ; then
    git tag "$(python setup.py --version)"
    git push --tags  # update the repository version
    python setup.py bdist_wheel  # build this package in the dist directory
    twine upload dist/* --username "$PYPI_USERNAME" --password "$PYPI_PASSWORD"  # publish
else
    echo "Only non-functional elements were modified in this change, there is no need to deploy."
    echo
    echo "** No deployment was made **"
    echo
fi
