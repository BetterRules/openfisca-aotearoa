# Changelog

# 3.0.1 - [#21](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/21)

* Tax and benefit system evolution. Minor change.
* Impacted periods: none
* Impacted areas: `variables/rates_rebates`
* Details:
  - removed extraneous rates_rebates variable file
- - - -
These changes:
- Change non-functional parts of this repository


# 3.0.0 - [#20](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/20)

* Tax and benefit system evolution. 
* Impacted periods: all.
* Impacted areas: 
  - Variables `income_tax__tax_payer_filing_status, income_tax__annual_gross_income, income_tax__annual_total_deduction, income_tax__net_income, income_tax__net_loss, income_tax__available_tax_loss, income_tax__taxable_income, rates_rebates__dependants, rates_rebates__rates_total, rates_rebates__combined_income, rates_rebates__rebate, rates_rebates__maximum_income_for_full_rebate, rates_rebates__minimum_income_for_no_rebate`
* Details:
  - Variable renaming, impacts the OpenFisca-Aotearoa public API (for instance renaming or removing a variable)

## 2.2.0 - [#19](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/19)

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: Entities
* Details:
  - Add a `Family` entity.
<!-- -->
* Tax and benefit system evolution.
* Impacted periods: after 2017-04.
* Impacted areas: “Working for families” parameters
* Details:
  - Add the `principal_caregiver_minimum_exclusive_care_percentage`, `principal_caregiver_age_threshold`, `full_year_abatement_threshold`, `full_year_abatement_rate` and `dependent_children_minimum_threshold` parameters.

## 2.1.0 - [#18](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/18)

* Tax and benefit system evolution
* Impacted periods: from 2000-04-01
* Impacted areas:
  - Variables `tax_payer_filing_status__income_tax, annual_gross_income__income_tax, annual_total_deduction__income_tax, net_income__income_tax, net_loss__income_tax, available_tax_loss__income_tax, taxable_income__income_tax`
  - Parameters `individual_income_tax_rate`
* Details:
  - Introducing some initial income_tax variables, laid out as per current best practice

# 2.0.0 - [#12](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/12)

* Tax and benefit system evolution
* Impacted periods: from 1973-07
* Impacted areas:
  - Variables `rates_rebates`
  - Entities `Propertee`
* Details:
  - Renaming Titled_Property entity (from Propertee)
  - Renaming of combined_income_as_per_rates_rebates (from salary)
  - Renaming of dependants_as_per_rates_rebates (from dependants)
  - Renaming of rates_total_as_per_rates_rebates (from rates)


### 1.0.1 - [#10](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/10)

* Tax and benefit system evolution
* Impacted periods: from 1973-07
* Impacted areas:
  - Variables `rates_rebates`
* Details:
  - Addition of Math floor function to conform rates_rebates variable with existing infrastructure.


# 1.0.0 - [#6](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/6)

* Tax and benefit system evolution
* Impacted periods: from 1973-07
* Impacted areas:
  - Parameters `benefits/rates_rebates`
  - Variables `rates_rebates`
  - Entities
* Details:
  - Create calculations for rates rebates system, based on year
    - Introduce `Propertee` entity
    - Introduce `benefits/rates_rebates/additional_per_dependant` parameter
    - Introduce `benefits/rates_rebates/income_threshold` parameter
    - Introduce `benefits/rates_rebates/initial_contribution` parameter
    - Introduce `benefits/rates_rebates/maximum_allowable` parameter
    - Introduce `dependants` variable
    - Introduce `rates` variable
    - Introduce `rates_rebate` variable
    - Introduce `maximum_income_for_full_rebate` variable
    - Introduce `minimum_income_for_no_rebate` variable
<!-- -->
* Tax and benefit system evolution
* Impacted periods: from 1898-01-01
* Impacted areas:
  - Parameters `general`
* Details:
  - Introduce new general legislation parameters
    - Introduce `general/age_of_majority` parameter
    - Introduce `general/age_of_superannuation` parameter
<!-- -->
* Tax and benefit system evolution
* Impacted periods: from 2000-04-01
* Impacted areas:
  - Parameters `taxes`
* Details:
  - Introduce income tax parameters
    - Introduce `taxes/income_tax_rate` parameter
