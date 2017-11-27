# Changelog

## 2.0.0 - [#24](https://github.com/openfisca/country-template/pull/24)

#### breaking change

* Details:
  - Upgrade to Core v21
  - Introduce the use of a string identifier to reference Enum items.
  - When setting an Enum (e.g. housing_occupancy_status), set the relevant string identifier (e.g. `free_lodger`). Indexes (e.g.`2`) and phrases (e.g. `Free Lodgers`) cannot be used anymore.
  - The default value is indicated for each Enum variable instead of being implicitly the first item of the enum.

#### Web API request/response

Before:

```
"persons": {
    "Bill": {}
},
"households": {
    "_": {
        "parent": ["Bill"]
        "housing_occupancy_status": "Free Lodger"
    }
}
```
Now:

```
"persons": {
    "Bill": {}
},
"households": {
    "_": {
        "parent": ["Bill"]
        housing_occupancy_status: "free_lodger"
    }
}
```

#### YAML testing
Before:

```
name: Household living in a 40 sq.meters accomodation while being free lodgers
  period: 2017
  input_variables:
    accomodation_size:
      2017-01: 40
    housing_occupancy_status:
      2017-01: 2
  output_variables:
    housing_tax: 0
```
Now:

```
name: Household living in a 40 sq.meters accomodation while being free lodgers
  period: 2017
  input_variables:
    accomodation_size:
      2017-01: 40
    housing_occupancy_status:
      2017-01: free_lodger
  output_variables:
    housing_tax: 0
```

#### Python API

When calculating an enum variable in Python, the output will be an array of Enum items.

> Each Enum item has:
> - a `name` property that contains its key (e.g. `tenant`)
> - a `value` property that contains its description (e.g. `"Tenant or lodger who pays a monthly rent"`)

## 1.4.0 - [#26](https://github.com/openfisca/country-template/pull/26)

* Technical improvement
* Details:
  - Upgrade to Core v20

### 1.3.2 - [#25](https://github.com/openfisca/country-template/pull/25)

* Declare package compatible with OpenFisca Core v19

### 1.3.1 - [#23](https://github.com/openfisca/country-template/pull/23)

* Technical improvement
* Details:
  - Declare package compatible with OpenFisca Core v18

## 1.3.0 - [#22](https://github.com/openfisca/country-template/pull/22)

* Tax and benefit system evolution
* Impacted periods: all
* Impacted areas: `stats`
* Details:
  - Introduce `total_benefits`
  - Introduce `total_taxes`

<!-- -->

* Minor change
* Details:
  - Introduce situation examples
    - These examples can be imported with: `from openfisca_country_template.situation_examples import single, couple`

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
