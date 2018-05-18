# Changelog

# 2.0.0 - [#12](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/12)

* Tax and benefit system evolution
* Impacted periods: from 1973-07
* Impacted areas: 
  - Variables `rates_rebates`
  - Entities `Propertee`
* Details:
  - Renaming of rates_rebates variables and the Titled_Property entity (from Propertee)
  

# 1.0.1 - [#10](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/10)

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