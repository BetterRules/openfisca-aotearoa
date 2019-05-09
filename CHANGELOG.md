# Changelog

# 11.2.0 [176](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/176)
* Bug Fix
  - Rates Rebate algorithm formula incorrectly allowed negative excess income

# 11.1.3 [174](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/174)
* No functional changes.
  - Removing unnecessary family groups in tests
  - Better names for tests

# 11.1.2 [170](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/170)
* No functional changes.
  - Removing unnecessary family/titled_property groups in tests

# 11.1.1 [169](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/169)
* Rename duplicate tests (same name, different test)

# 11.1.0 [167](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/167)
* Adds values for Rates Rebates 2018 to 2019

# 11.0.0 [163](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/163)
* Upgrade to Open Fisca 29.x

# 10.2.1 [159](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/159)
* No functional changes.
  - Removed debug print statement

# 10.2.0 [153](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/153)
* Update to Openfisca Core 26.0

# 10.1.3 [148](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/148)
* Add Hamish to maintainers

# 10.1.2 [150](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/150)
* Automate git tagging of release

# 10.1.1 [122](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/122)
* Grammar fix up in variable labels

# 10.1.0 [142](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/142)
* Add formula for Primary Carer in Paid Parental Leave

# 10.0.0 [145](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/145)
* Upgrades to Open Fisca core 25.0
* Removed support for Python 2.7
* Updated all yaml tests to new format

# 9.2.0 - [141](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/141)
* add `immigration__entitled_to_indefinite_stay` for use in citizenship presence calculations

# 9.1.0 - [#139](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/139)
* Fix calculation of number of days present in NZ for Citizenship by Grant

# 9.0.1 - [#121](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/121)
* Added unit (years) to ages
* Added unit (NZD) to best_start__entitlement

# 9.0.0 - [#132](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/132)
* Removed duplicate parameter `general/age_of_superannuation`

# 8.0.1 - [#126](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/126)
* Changed Formula:
  - Removed `family_scheme__full_time_earner` from `family_scheme__qualifies_for_family_tax_credit`

# 8.0.0 - [#125](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/125)
* Renamed variables:
  - `family_scheme__in_work_tax_credit_is_full_time_earner` replaced with `family_scheme__full_time_earner`

# 7.0.0 - [#124](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/124)
* Renamed variables:
  - `social_security__eligible_for_childcare_subsidy` to `social_security_regulation__eligible_for_childcare_subsidy`
  - `sole_parent__family_has_child_under_age_limit` to `sole_parent_support__family_has_child_under_age_limit`
  - `family_has_resident_child_under_5_not_in_school` to `social_security_regulation__family_has_resident_child_under_5_not_in_school`
  - `family_has_resident_child_aged_5_who_will_be_enrolled_in_school` to `social_security_regulation__family_has_resident_child_aged_5_who_will_be_enrolled_in_school`
  - `family_has_child_eligible_for_disability_allowance_child_under_6` to `social_security_regulation__family_has_child_eligible_for_disability_allowance_child_under_6`
* New variables:
  - `family_scheme__full_time_earner`
  - `hours_per_week_employed`
  - `early_childcare_hours_participation_per_week`
  - `student_allowance__partner_or_person_receiving_certain_allowances`
* New parameters:
  - `entitlements.social_security.family_scheme.hours_per_week_threshold`
  - `entitlements.social_security.family_scheme.hours_per_week_threshold_with_partner`
  - `entitlements.social_security.childcare_subsidy.minimum_hours_in_childcare`
* Added `social_security_regulation` to structure.json

# 6.1.2 - [#117](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/117)
* Bug fix
  - no longer throws unhandled exception when working on leap days

# 6.1.1 - [#115](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/115)

* New variable
  - `citizenship__meets_preceeding_single_year_minimum_presence_requirement`

# 6.1.0 - [#101](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/101)

* Added Citizen-by-grant presence in NZ requirements algorithm
* Change `age` to be changing by `DAY`
* Uses `day` branch from Open Fisca
* New Variables
  - `citizenship__citizenship_by_grant_may_be_authorized`
  - `citizenship__meets_minimum_presence_requirements`
  - `days_present_in_new_zealand_in_preceeding_5_years`
  - `days_present_in_new_zealand_in_preceeding_year`
  - `present_in_new_zealand`
  - `is_of_full_capacity`
  - `immigration__holds_indefinite_stay_visa`
  - `citizenship__is_of_good_character`
  - `citizenship__has_sufficient_knowledge_of_the_responsibilities_and_privileges_attaching_to_nz_citizenship`
  - `citizenship__has_sufficient_knowledge_of_the_english_language`
  - `citizenship__intends_to_reside_in_nz`
  - `citizenship__intends_nz_employment`
  - `citizenship__intends_international_service`
  - `citizenship__intends_crown_service`


# 6.0.3 - [#104](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/104)
* Refactor to remove unused variables
  - Removed `acc__elected_for_weekly_compensation`
  - Removed `social_security__cash_assets`
  - Removed `family_scheme__proportion_as_principal_carer`
  - Removed `social_security__is_a_specified_beneficiary`
  - Removed `income_tax__tax_payer_filing_status`

# 6.0.2 - [#103](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/103)
* Tidyup metadata
    Adding yet more missing labels

# 6.0.1 - [#102](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/102)
* Tidyup metadata
    Adding missing labels, shortened long labels and improved language in descriptions

# 6.0.0 - [#98](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/98)
* Technical improvement.
    Upgrade to Python 3.7

# 5.1.4 - [#100](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/100)
* Technical improvement.
    Pin to version 24.3.0, to ensure we support legislation explorer
    the `/entities` route was added to the API in this version

# 5.1.3 - [#97](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/97)
* Refactored NZ Superannuation
  - Added `super__eligible_age`
  - Removed age requirement from `super__eligible`
  - Removed `super__living_alone` and `super__has_partner_in_long_term_care_or_rest_home`

# 5.1.2 - [#94](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/94)
* Added NZ Superannuation

# 5.1.1 - [#93](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/93)
* Bug fix.
  - adding residency requirements to entitlements

# 5.1.0 - [#92](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/92)
* Tax and benefit system evolution.
  - adding income test to Family Tax Credit
  - added variables `family_scheme__in_work_tax_credit_is_full_time_earner, family_scheme__in_work_tax_credit_income_under_threshold, family_scheme__family_tax_credit_income_under_threshold`

# 5.0.2 - [#88](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/88)
* Tax and benefit system evolution.
  - added formula for is_permanent_resident

# 5.0.1 - [#81](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/81)
Calculation improvement.
 * Added Home Help

# 5.0.0 - [#83](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/83)
* Tax and benefit system evolution. Major change.
* Impacted periods: income_tax
* Impacted areas: `tests/best_start, tests/family_scheme, tests/working_for_families, variables/entitlements/income_tax/best_start.py, variables/entitlements/income_tax/family_scheme.py, variables/entitlements/income_tax/working_for_families.py`
* Details:
  - renamed `income_tax__qualifies_for_entitlements_under_family_scheme` to `family_scheme__qualifies_for_entitlements` to better reflect law structure
  - renamed `income_tax__caregiver_age_qualifies_under_family_scheme` to `family_scheme__caregiver_age_qualifies` to better reflect law structure
  - renamed `income_tax__person_principal_carer_qualifies_under_family_scheme` to `family_scheme__qualifies_as_principal_carer` to better reflect law structure
  - renamed `income_tax__family_scheme_income` to `family_scheme__assessable_income` to better reflect law structure
  - renamed `income_tax__family_scheme_income_for_month` to `family_scheme__assessable_income_for_month` to better reflect law structure
  - renamed `income_tax__proportion_as_principal_carer` to `family_scheme__proportion_as_principal_carer` to better reflect law structure
  - renamed `income_tax__family_has_dependent_children` to `family_scheme__has_dependent_children` to better reflect law structure
  - renamed `income_tax__eligible_for_working_for_families` to `family_scheme__qualifies_for_working_for_families` to better reflect law structure
  - renamed `income_tax__caregiver_eligible_for_best_start_tax_credit` to `best_start__eligibility` to better reflect law structure
  - renamed `income_tax__entitlement_for_best_start_tax_credit` to `best_start__entitlement` to better reflect law structure
  - renamed `income_tax__family_has_children_eligible_for_best_start` to `best_start__family_has_children_eligible` to better reflect law structure
  - renamed `income_tax__best_start_tax_credit_per_child` to `best_start__tax_credit_per_child` to better reflect law structure
  - renamed `income_tax__person_is_best_start_child_as_year` to `best_start__year_of_child` to better reflect law structure
  - Added `family_scheme__base_qualifies` variable
  - Added `family_scheme__working_for_families_entitlement,` variables
  - Added `family_scheme__qualifies_for_child_tax_credit, family_scheme__child_tax_credit_entitlement` variables
  - Added `family_scheme__qualifies_for_in_work_tax_credit, family_scheme__in_work_tax_credit_entitlement` variables
  - Added `family_scheme__qualifies_for_parental_tax_credit, family_scheme__parental_tax_credit_entitlement` variables
  - Added `family_scheme__qualifies_for_minimum_family_tax_credit` variable
  - Added `family_scheme__qualifies_for_family_tax_credit, family_scheme__family_tax_credit_entitlement` variables
  - renamed parameter `entitlements.income_tax.best_start.full_year_abatement_threshold` to `entitlements.income_tax.family_scheme.best_start.full_year_abatement_threshold`
  - renamed parameter `entitlements.income_tax.best_start.full_year_abate` to `entitlements.income_tax.family_scheme.best_start.full_year_abate`
  - renamed parameter `entitlements.income_tax.best_start.prescribed_amount` to `entitlements.income_tax.family_scheme.best_start.prescribed_amount`
  - moved family scheme tests sub folder `income_tax/family_scheme folder`


# 4.2.6 - [#81](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/81)
Calculation improvement.
 * Added Home Help

# 4.2.5 - [#84](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/87)
Calculation improvement.
 * Added Childcare Subsidy

# 4.2.4 - [#77](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/86)
Calculation improvement.
 * Added Unsupported Child Benefit
 * Added Orphan's benefit

# 4.2.3 - [#77](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/77)
Technical improvement.
 * Remove dependency on OpenFisca-Web-API (now included in Core)
 * Update README.md with notes on updating OpenFisca-Core for existing developers

# 4.2.2 - [#78](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/78)
Calculation improvement.
 * Added Paid Parental Leave Regulations

# 4.2.1 - [#75](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/75)
Calculation improvement.
 * Added Student Allowance Regulations
 * Seperated Acts and Regulations
 * Adding Relationship status
 * Adding Superannuation age qualifications.

# 4.2.0
Hotfix
 * Mark source code as UTF8

# 4.1.6 - [#41](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/74)
Calculation improvement.
 * Added Young Parent Payment for single person

# 4.1.5 - [#72](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/72)
Calculation improvement.
  * Added Community Service Card

# 4.1.4 - [#41](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/55)
Calculation improvement.
 * Added Jobseeker Support for 18 and 19 year olds

# 4.1.3 - [#41](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/55)
Calculation improvement.
* addded Supported living payment
* Organising by numbered section of the act
* Moved Social Security Act disability definitions to that folder
* Move social security tests to folder with that name
* refactored to add 'is_citizen_or_resident' variable
* Renaming job seeker to Jobseeker Support
* Restructured Social Security Act variables

# 4.1.2 - [#41](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/55)
Calculation improvement.
* Added Sole Parent Support

# 4.1.1 - [#41](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/53)
Calculation improvement.
* Added Job Seeker Support

# 4.1.0 - [#41](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/51)
Calculation improvement.
* Added Child Disability Allowance
* Added "Others" role within a titled_property
* Added "Others" role within a family

# 4.0.2 - [#42](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/22)
Legislation improvement.
* Added Accommodation Supplement from the Social Security Act 1964

# 4.0.1 - [#42](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/42)
Technical improvement.
* Details:
  - Moving the version bump check to its own segment of the circle ci config, This means it appears as a separate check within a github PR, and so we can see quickly that the input/output tests pass - and it's only the version bump that's missing.

# 4.0.0 - [#22](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/22)

* Tax and benefit system evolution. Major change.
* Impacted periods: all
* Impacted areas: `entities.families, tests/best_start, tests/family_scheme, tests/working_for_families, variables/demographics, variables/rates_rebates, variables/entitlements/income_tax/best_start.py, variables/entitlements/income_tax/family_scheme.py, variables/entitlements/income_tax/working_for_families.py`
* Details:
  - removed extraneous rates_rebates variable file,
  - added `variables/demographics` section with variables (`date_of_birth, due_date_of_birth, age, age_of_youngest`)
  - added `variables/entitlements/income_tax/best_start.py` with variables (`income_tax__caregiver_eligible_for_best_start_tax_credit, income_tax__family_has_children_eligible_for_best_start, income_tax__best_start_tax_credit_per_child,  income_tax__entitlement_for_best_start_tax_credit, income_tax__person_is_best_start_child_as_year`)
  - added `variables/entitlements/income_tax/family_scheme.py` with variables (`income_tax__qualifies_for_entitlements_under_family_scheme, income_tax__caregiver_age_qualifies_under_family_scheme, income_tax__person_principal_carer_qualifies_under_family_scheme, income_tax__family_scheme_income, income_tax__proportion_as_principal_carer`)
  - added `variables/entitlements/income_tax/working_for_families.py` with variables (`social_security__received_income_tested_benefit, veterans_support__received_parents_allowance, veterans_support__received_childrens_pension, income_tax__resident, income_tax__family_has_dependent_children, income_tax__dependent_child`)

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
