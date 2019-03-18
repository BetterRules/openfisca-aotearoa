#!/bin/sh

set -ev
VERSION=`python setup.py --version`

if ! git rev-parse $VERSION 2>/dev/null ; then
  git tag $VERSION
  git push origin $VERSION
fi
