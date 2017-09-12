# Changelog

## 1.2.7 - [#21](https://github.com/openfisca/country-template/pull/21)

* Minor change
  - Use the technical documentation new address

## 1.2.6 - [#20](https://github.com/openfisca/country-template/pull/20)

* Minor change
  - Document entities

## 1.2.5 - [#17](https://github.com/openfisca/country-template/pull/17)

* Technical improvement
* Details:
  - Adapt to version `17.0.0` of Openfisca-Core
  - Transform XML parameter files to YAML parameter files.

## 1.2.4 - [#16](https://github.com/openfisca/country-template/pull/16)

* Tax and benefit system evolution
* Details
  - Introduce `housing_occupancy_status`
  - Take the housing occupancy status into account in the housing tax

## 1.2.3 - [#9](https://github.com/openfisca/country-template/pull/9)

* Technical improvement: adapt to version `15.0.0` of Openfisca-Core
* Details:
  - Rename Variable attribute `url` to `reference`

## 1.2.2 - [#12](https://github.com/openfisca/country-template/pull/12)

* Tax and benefit system evolution
* Details
  - Allow to declare a yearly amount for `salary`.
  - The yearly amount will be spread over the months contained in the year

## 1.2.1 - [#11](https://github.com/openfisca/country-template/pull/11)

* Technical improvement
* Details:
  - Make `make test` command not ignore failing tests.

## 1.2.0 - [#10](https://github.com/openfisca/country-template/pull/10)

* Technical improvement
* Details:
  - Upgrade OpenFisca-Core
    - Update the way we define formulas start dates and variables stop dates.
    - Update the naming conventions for variable formulas.
    - See the [OpenFisca-Core Changelog](https://github.com/openfisca/openfisca-core/blob/master/CHANGELOG.md#1400---522).

## 1.1.0 - [#7](https://github.com/openfisca/country-template/pull/7)

* Tax and benefit system evolution
* Impacted periods: from 2013-01-01
* Impacted areas:
   - Reform: `modify_social_security_taxation`
* Details:
  - Add a reform modifying the brackets of a scale
      - Show how to add, modify and remove a bracket.
      - Add corresponding tests.

# 1.0.0 - [#4](https://github.com/openfisca/country-template/pull/4)

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas:
  - `benefits`
  - `demographics`
  - `housing`
  - `income`
  - `taxes`
* Details:
  - Build the skeleton of the tax and benefit system
