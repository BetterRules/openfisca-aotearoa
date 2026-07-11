# Changelog

### Unreleased — income tax / ACC earners levy / KiwiSaver coverage (#199)

* Tax and benefit system evolution.
* Impacted periods: 2021-04 onwards (income tax); 2023-04 onwards (ACC earners levy); 2013-04 / 2026-04 / 2028-04 (KiwiSaver rates).
* Impacted areas:
  - `parameters/taxes/income_tax/individual_income_tax_rate.yaml`
  - `parameters/acc/earners_levy/`
  - `parameters/kiwisaver/`
  - `variables/acts/income_tax/individual.py`
  - `variables/acts/acc/earners_levy.py`
  - `variables/acts/kiwisaver/contributions.py`
* Added variables:
  - `income_tax__schedule_1_tax_before_credits`
  - `income_tax__income_tax_before_credits` (alias)
  - `acc__earnings_for_earners_levy`
  - `acc__earners_levy_including_gst`
  - `acc__earners_levy` (alias)
  - `kiwisaver__gross_salary_or_wages`
  - `kiwisaver__employee_minimum_contribution`
  - `kiwisaver__employer_minimum_contribution`
* Notes:
  - YEAR formulas look up 1 April parameters for the calendar year of the period (NZ tax/levy year convention).
  - Rates cited from IRD public pages; Schedule 1 progressive tax is before credits and excludes ACC levy.

### 22.0.0 - [69](https://github.com/digitalaotearoa/openfisca-aotearoa/pull/64)

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas:
  - `CONTRIBUTING.md`
  - `Makefile`
  - `variables/acts/social_security/childcare_assistance`
  - `variables/regulation/social_security_regulation`
  - `variables/demographics`
  - `parameters/social_security/childcare_assistance`

* Breaking changes:
 - `early_childcare_hours_participation_per_week` period changed from month to week
 - `attending_school` period changed from month to week

* Added variables:
 - `child_disability_allowance__payable`
 - `childcare_subsidy__eligible`
 - `childcare_subsidy__granted`
 - `childcare_subsidy__receiving`
 - `childcare_subsidy__hours_payable`
 - `childcare_subsidy__caregiver_approved_activity`
 - `childcare_subsidy__caregiver_approved_activity_hours`
 - `childcare_subsidy__caregiver_serious_disability`
 - `childcare_subsidy__caregiver_serious_disability_hours`
 - `childcare_subsidy__caregiver_other_hours`
 - `childcare_subsidy__caregiver_serious_disability_illness`
 - `childcare_subsidy__caregiver_serious_disability_illness_hours_needed`
 - `childcare_subsidy__no_other_caregiver`
 - `childcare_subsidy__other_child_in_hospital_or_disability_allowance`
 - `childcare_subsidy__other_caregiver_appproved_activity`
 - `childcare_subsidy__engaged_in_approved_activity`
 - `childcare_subsidy__shift_work`
 - `childcare_subsidy__family_has_resident_child_under_5_not_in_school`
 - `childcare_subsidy__resident_child_aged_5_intend_enrol_in_school`
 - `childcare_subsidy__family_with_disability_allowance_child_under_6`
 - `childcare_subsidy__child_under_5_not_in_school`
 - `childcare_subsidy__child_aged_5_intend_enrol_in_school`
 - `childcare_subsidy__child_meets_criteria_with_disability_allowance_under_6`
 - `childcare_subsidy__child_meets_criteria`
 - `childcare_subsidy__maximum`
 - `childcare_subsidy__rate`
 - `oscar_subsidy__granted`
 - `social_security_regulation__household_income`

* Renamed variables:
 - `will_be_enrolled_in_school` renamed to `intends_to_enroll_in_school`  period changed from month to eternity
 - `childcare_assistance__family_has_resident_child_under_5_not_in_school` renamed to `childcare_subsidy__family_has_resident_child_under_5_not_in_school`
 - `childcare_assistance__resident_child_aged_5_will_be_enrolled_in_school` renamed to `childcare_subsidy__resident_child_aged_5_intend_enrol_in_school`
 - `childcare_assistance__family_has_child_eligible_for_disability_allowance_child_under_6` renamed to `childcare_subsidy__family_with_disability_allowance_child_under_6`
 - `childcare_assistance__eligible_childcare_subsidy` renamed to `childcare_subsidy__eligible`

### 21.1.1 - [64](https://github.com/digitalaotearoa/openfisca-aotearoa/pull/64)

* Technical improvement.
* Details:
  - Updated Documentation
  - Updated OpenFisca Core dependency (to latest)
  - Updated python environment and version (3.11)
  - Updated docker related files
  - Updated github related files

### 21.0.1 - [58](https://github.com/digitalaotearoa/openfisca-aotearoa/pull/58)

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas:
  - `variables/acts/social_security`
  - `variables/acts/income_tax`
  - `variables/regulation/student_allowance`
  - `variables/regulation/social_security`
  - `variables/demographics`
  - `accommodation_supplement`
* Details:
  - Fix rate & rebate when accommodation type is lodging or boarding
  - Normally, a %62 rate is to be applied in this particular case
  - However, in reality %162 was being applied, which is incorrect
  - Resolve warnings present in Accomodation Supplement Tests
  - Resolved linting issues

* Breaking changes:
 - `student_allowance__married_or_partnered` period changed from month to day
 - `student_allowance__supported_child` period changed from month to day
 - `student_allowance__partner_has_a_supported_child` period changed from month to day
 - `student_allowance__person_has_spouse` period changed from month to day, formula updated

* Changes:
 - `age_of_partner` set_input_dispatch_by_period applied

### 21.0.0 - [60](https://github.com/digitalaotearoa/openfisca-aotearoa/pull/60)

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas:
  - `variables/acts/social_security`
  - `variables/acts/parental_leave`
  - `variables/acts/immigration`
  - `variables/demographics`
  - `variables/regulation/social_security/childcare_assistance`
  - `variables/regulation/student_allowance`
* Details:
  - Add calculation for child disability allowance

* Added variables:
 - `immigration__temporary_entry_class_visa`
 - `social_security__general_limitation`
 - `social_security__unlawfully_resident_or_present`
 - `social_security__compelled_to_remain`
 - `social_security__refugee_or_protected_person`
 - `social_security__awaiting_refugee`
 - `social_security__awaiting_protected_person`
 - `child_disability_allowance__payment`
 - `child_disability_allowance__payment_to`
 - `child_disability_allowance__child_with_serious_disability`
 - `child_disability_allowance__care_in_home`
 - `child_disability_allowance__approved_weekly_accomodation`
 - `child_disability_allowance__granted`
 - `social_security__temporary_ob_or_ucb_caregiver`
 - `social_security__care_and_control`
 - `has_disability`

* Breaking changes:
 - `immigration__recognised_refugee` period changed from month to day
 - `child_disability_allowance__eligible` formula and period changed
 - `child_disability_allowance__family_has_eligible_child` formula and period changed
 - `child_disability_allowance__allowance_criteria` formula and period changed
 - `child_disability_allowance__constant_care_exceeding_12_months`

* Renamed variables:
 - `income_tax__principal_caregiver` renamed to `social_security__principal_caregiver` this affects:
   - `orphans_benefit__entitled`
   - `supported_living_payment__entitled`
   - `unsupported_child__entitled`
   - `childcare_assistance__eligible_childcare_subsidy`
 - `social_security__disability_self_inflicted` renamed to `supported_living_payment__disability_self_inflicted`

Added new feature in folder `ōpenfisca_aotearoa/api_examples`. This is a space for example http calls to help illustrate how to call the API.
Added example calls for entities, parameters, variables and then `acts/social_security/child_disability_allowance` as per project structure


### 20.1.1 - [48](https://github.com/digitalaotearoa/openfisca-aotearoa/pull/48)

* Test case.
* Details:
  - Add Peta & Kai's stories.

## 20.1.0 - [57](https://github.com/digitalaotearoa/openfisca-aotearoa/pull/57)

* Technical improvement.
* Details:
  - Catch up from mainstream, both dependencies and code evolution (bumped Numpy to ~1.24 and Python to 39-311)
  - These upgrades are critical as the aforesaid versions are EOL and do not easily compile in modern workstations (specially ARM64).

### 20.0.3 - [51](https://github.com/digitalaotearoa/openfisca-aotearoa/pull/51)

* Fixes problem with importlib_metadata and idna upstream:
 - `setup.py`

### 20.0.2 - [49](https://github.com/govzeroaotearoa/openfisca-aotearoa/pull/49)

* Added dependency package importlib_metadata:
 - `setup.py`

### 20.0.1 - [49](https://github.com/govzeroaotearoa/openfisca-aotearoa/pull/49)

* Other Changes:
 - `tests/social_security/sole_parent_support/sole_parent_support__benefit.yaml figure fixed for 2022/23`

## 20.1.0 - [48](https://github.com/digitalaotearoa/openfisca-aotearoa/pull/48)

* Test case.
* Impacted periods: none.
* Impacted areas: `tests/accommodation_supplement`
* Details:
  - Add Peta's story
  - Add Kai's story

# 20.0.0 - [43](https://github.com/govzeroaotearoa/openfisca-aotearoa/pull/43)

* Added variables:
 - `sole_parent_support__requirement`
 - `sole_parent_support__dependent_child_requirement`
 - `sole_parent_support__spouse_or_partner_died`
 - `sole_parent_support__marriage_or_civil_union_dissolved`
 - `sole_parent_support__living_apart_and_lost_support`
 - `sole_parent_support__lost_regular_support`
 - `sole_parent_support__partner_imprisoned`
 - `sole_parent_support__partner_supervision`
 - `sole_parent_support__split_care`
 - `sole_parent_support__parents_living_apart`
 - `sole_parent_support__principal_caregiver_of_youngest`
 - `sole_parent_support__principal_caregiver_before_apart`
 - `sole_parent_support__entitled_without_split_care_requirement`
 - `sole_parent_support__both_primary_caregiver_by_order`
 - `sole_parent_support__receiving`
 - `social_security__principal_caregiver`
 - `sole_parent_support__benefit`
 - `sole_parent_support__base`
 - `sole_parent_support__reduction`
 - `sole_parent_support__weekly_childcare_cost`
* Other changes:
  - `social_security__residential_requirement` period changed from month to week
  - `social_security__ordinarily_resident_in_new_zealand` period changed from month to eternity
  - `sole_parent_support__entitled` period changed from month to week
  - `sole_parent_support__meets_relationship_qualification` period changed from month to week
  - `sole_parent_support__family_has_child_under_age_limit` period changed from month to week
  - `sole_parent_support__age_threshold` period changed from month to week
  - `sole_parent_support__years_in_nz_requirement` period changed from month to week
  - `sole_parent_support__below_income_threshold` period changed from month to week
  - `parent` role added to `family` entity
  - `Sole Parent Support Base Rate`
* Added parameters:
  - `parameters/social_security/schedule_5/asset_limits_1.yml`
  - `parameters/social_security/schedule_5/asset_limits_2.yml`
  - `parameters/social_security/schedule_5/asset_limits_3.yml`
  - `parameters/social_security/schedule_5/asset_limits_4.yml`
  - `parameters/social_security/schedule_5/income_limits_5.yml`
  - `parameters/social_security/schedule_5/income_limits_6.yml`
  - `parameters/social_security/schedule_5/income_limits_7.yml`
  - `parameters/social_security/schedule_5/income_limits_8.yml`
  - `parameters/social_security/schedule_5/income_limits_9.yml`
  - `parameters/social_security/sole_parent_support/child_age_threshold.yml`
  - `parameters/social_security/sole_parent_support/age_threshold.yml`
* Removed variables
  - `sole_parent_support__years_in_nz_requirement`

## 19.1.0 - [46](https://github.com/digitalaotearoa/openfisca-aotearoa/pull/46)

* Tax and benefit system evolution.
* Impacted periods: from 26/11/2018.
* Impacted areas: `regulations/accommodation_supplement/base.py`
* Details:
  - Add calculation for non-beneficiaries

### 19.0.1 - [45](https://github.com/digitalaotearoa/openfisca-aotearoa/pull/45)

* Calculation improvement.
* Impacted periods: 2018/11/26.
* Impacted areas: `accommodation_supplement`
* Details:
  - Use `social_security__dependent_children`

# 19.0.0 - [44](https://github.com/digitalaotearoa/openfisca-aotearoa/pull/44)

* Calculation improvement:
  - Incorporates all main benefits for accommodation base rate calculation

* Breaking changes
  - Several definition period and name changes

# 18.0.0 - [33](https://github.com/digitalaotearoa/openfisca-aotearoa/pull/33)

* New features:
  - Add first out of four cases of accommodation supplement

* Breaking changes
  - Several definition period and name changes

## 17.1.0 - [38](https://github.com/govzeroaotearoa/openfisca-aotearoa/pull/38)\\

* Other changes:
  - `social_security__residential_requirement` period changed from monthly to weekly
  - `social_security__ordinarily_resident_in_new_zealand` period changed from monthly to eternity

# 17.0.0 - [37](https://github.com/govzeroaotearoa/openfisca-aotearoa/pull/37)

* Added variables:
  - `social_security__receiving_main_benefit`
  - `emergency_benefit__receiving`
  - `sole_parent_support__receiving`
  - `supported_living_payment__receiving`
  - `young_parent_payment__receiving`
  - `youth_payment__receiving`
* Renamed variables:
  - `jobseeker_benefit__granted` to `jobseeker_support__granted`

### 16.0.2 - [36](https://github.com/govzeroaotearoa/openfisca-aotearoa/pull/35)
*
* Change to variable `person_has_partner` - time period switched from month to week

### 16.0.1 - [36](https://github.com/govzeroaotearoa/openfisca-aotearoa/pull/35)

* Change to variable `in_a_relationship` - time period switched from month to week

# 16.0.0 - [35](https://github.com/govzeroaotearoa/openfisca-aotearoa/pull/35)

* Change to contributing.md and coding patterns
* Updated spelling of dependant to dependent when used as an adjective
* Added section: `emergency_benefit`
* Added variables:
  - `in_a_relationship`
  - `social_security__been_married_or_civil_union_or_de_facto_relationship`
  - `social_security__age_youngest_dependant_child`
  - `jobseeker_support__transferred_15_july_2013`
  - `emergency_benefit__granted`
  - `social_security__granted_main_benefit`
  - `jobseeker_benefit__granted`
  - `sole_parent_support__granted`
  - `supported_living_payment__granted`
  - `young_parent_payment__granted`
  - `youth_payment__granted`
  - `income_tax__principal_caregiver` (to replace the previous dependancy on the role `principal_caregiver` which has been renamed to the more generic `principal`)
  - `oranga_tamariki__child` (not yet utilised by referred to in social_security__dependent_child)
  - `oranga_tamariki__parent` (not yet utilised by referred to in social_security__dependent_child)
  - `social_security__income`
  - `schedule_4__part1_1_a`
  - `schedule_4__part1_1_b`
  - `schedule_4__part1_1_c`
  - `schedule_4__part1_1_d`
  - `schedule_4__part1_1_e`
  - `schedule_4__part1_1_f`
  - `schedule_4__part1_1_g`
  - `schedule_4__part1_1_g_i`
  - `schedule_4__part1_1_g_ii`
  - `schedule_4__part1_1_h`
  - `schedule_4__part1_1_h_i`
  - `schedule_4__part1_1_h_ii`
  - `schedule_4__part1_1_i`
  - `schedule_4__part1_1_i_i`
  - `schedule_4__part1_1_i_ii`
  - `schedule_4__part1_1_j`
  - `schedule_4__part1_1_j_i`
  - `schedule_4__part1_1_j_ii`
* Added parameters
  - `social_security/income_test_1.yml`
  - `social_security/income_test_2.yml`
  - `social_security/income_test_3a.yml`
  - `social_security/income_test_3b.yml`
  - `social_security/income_test_4.yml`
* Breaking changes, Removed variables:
  - `jobseeker_support__net` (float) replaced with `jobseeker_support__benefit` (float)
  - `jobseeker_support__gross` (float) replaced with `jobseeker_support__base` (float)
  - `jobseeker_support__living_with_parent` (float) changed to `jobseeker_support__living_with_parent` (bool)
* Renamed variables:
  - `social_security__eligible_for_supported_living_payment` to `supported_living_payment__entitled`
  - `social_security__totally_blind` to `totally_blind`
  - `social_security__severely_restricted_capacity_for_work` to `supported_living_payment__restricted_work_capacity`
  - `social_security__required_to_give_fulltime_care` to `supported_living_payment__caring_for_another_person`
  - `person_is_parent` to `social_security__parent`
* Removed variables:
  - `married` (see marriage__married)
  - `civil_union` (see civil_union__civil_union)
  - `de_facto_relationship` (see property_relationships__de_facto_relationship)
  - `married_or_civil_union_or_de_facto_relationship` (see in_a_relationship)
* Entities and roles:
  - `principal_caregiver` to `principal`,
  - Removed the `parent` role as it wasn't utilised
* Other changes
  - Rewrote `young_parent_payment__relationship_requirements` formula
  - Removed `has_been_married_or_in_a_civil_union_or_de_facto_relationship`
  - Removed `social_security__child_in_family`
  - Improved `minimum_family_tax_credit` tests
  - Adapted `family_scheme__qualifies_as_principal_carer` to utilise `income_tax__principal_caregiver` instead of role `principal_caregiver`
  - Adapted `parental_leave__primary_carer` to utilise `income_tax__principal_caregiver` instead of role `principal_caregiver`
  - Adapted `child_disability_allowance__eligible` to utilise `income_tax__principal_caregiver` instead of role `principal_caregiver`
  - Adapted `orphans_benefit__entitled` to utilise `income_tax__principal_caregiver` instead of role `principal_caregiver`
  - Adapted `unsupported_child__entitled` to utilise `income_tax__principal_caregiver` instead of role `principal_caregiver`
  - Adapted `childcare_assistance__eligible_childcare_subsidy` to utilise `income_tax__principal_caregiver` instead of role `principal_caregiver`
  - Changed `social_security__dependent_children`, `social_security__child`, `social_security__dependent_child`, `social_security__financially_independent`, `in_a_relationship` from month to week period
  - Added formula to `social_security__dependent_child`
  - Added additional clauses to `jobseeker_support__base`
  - Improved `in_a_relationship` formula
  - Add section `schedule_4` to `structure.json`

# 15.0.0 - [34](https://github.com/govzeroaotearoa/openfisca-aotearoa/pull/34)

* Resolve issues with dependant child concepts within the Social Security Act
* Updated spelling of dependant to dependent when used as an adjective
* Breaking changes, Removed variables:
  - `dependent_child` utilise `social_security__dependent_child` instead
  - `social_security__person_has_dependant_child` (bool) replaced with `social_security__dependent_children` (float)
  - `person_has_dependent_child` (bool) replaced with `social_security__dependent_children` (float)
  - `person_has_dependent_child` also had a default value of `True` which affected one test in home_help
  - `openfisca_aotearoa/parameters/entitlements/social_security/jobseeker_support/age_threshold_without_dependant_child.yaml` renamed to `.../age_threshold_without_dependent_child.yaml`
  - removed the formula associated with `social_security__dependent_child`

# 14.0.0 - [31](https://github.com/govzeroaotearoa/openfisca-aotearoa/pull/31)

* Added support for Social Security Act 2018 residency requirements
* Added Job Seeker Support entitlement for Social Security Act 2018
* Breaking changes, Renamed variables:
  - `social_security__meets_residential_requirements_for_certain_benefits` to `social_security__residential_requirement`
  - `jobseeker_support` to `jobseeker_support__entitled`
  - `eligible_for_jobseeker` to `jobseeker_support__entitled`
  - `jobseeker_support__meets_age_threshold` to `jobseeker_support__age_requirement`
  - `jobseeker_support__below_income_threshold` to `jobseeker_support__minimum_income`
  - `jobseeker_support__prepared_for_employment` to `jobseeker_support__willing_and_able`
  - `jobseeker_support__age_requirement` to `jobseeker_support__age_requirement`
  - `social_security__residential_requirements` to `social_security__residential_requirement`
  - `social_security__resided_continuously_in_nz_for_at_least_2_years_at_any_one_time` to `social_security__resided_continuously_nz_2_years_citizen_or_resident`
  - `social_security__resided_continuously_in_nz_at_least_2_years_after_becoming_citizen_or_resident` to `social_security__resided_continuously_nz_2_years_citizen_or_resident`
* Breaking changes, variable calculation changed:
 - `social_security__residential_requirement`
 - `age` (added set_input_dispatch_by_period)
 - `social_security__financially_independent` (adjusted to allow for social_security__full_employment WEEK period)
 - `social_security__full_employment` (adjusted from month to week, added reference)
 - `social_security__person_has_dependant_child` (added set_input_dispatch_by_period and reference)
 - `social_security__residential_requirement` (added set_input_dispatch_by_period)
 - `social_security__ordinarily_resident_in_new_zealand` (added set_input_dispatch_by_period)
 - `jobseeker_support__entitled` extensively changed
 - `jobseeker_support__age_requirement`
 - `jobseeker_support__minimum_income` changed from `MONTH` to `WEEK`, default_value set to false (from true), set_input_dispatch_by_period added along with reference
* New variables added:
 - `social_security__employment`
 - `jobseeker_support__work_gap`
 - `jobseeker_support__available_for_work`
 - `jobseeker_support__losing_earnings`
 - `jobseeker_support__receiving`
 - `jobseeker_support__full_employment_temporary`
 - `jobseeker_support__income_52_week_period_less_than`
 - `jobseeker_support__taken_reasonable_steps`
 - `jobseeker_support__limited_in_capacity`
* Parameters renamed:
 - `age_threshold` to `age_threshold_without_dependant_child`
 - `age_threshold_with_dependant_child` to `age_threshold_other`

### 13.0.1 - [30](https://github.com/govzeroaotearoa/openfisca-aotearoa/pull/30)

* Restoration of Citizen and Immigration tests to utilise functionality added in OpenFisca core.

# 13.0.0 - [29](https://github.com/govzeroaotearoa/openfisca-aotearoa/pull/29)

* Large restructure and renaming exercise to lay groundwork for social security act work.
* Switch away from using act numbers for folders to using prefixes. New version of social security act forced this.
* Added documentation on coding, structuring project
* Currently dependant on Openfisca Core branch for weeks/days features
* Breaking changes, Renamed variables:
  - `is_nz_citizen` to `citizenship__citizen`
  - `is_citizen_or_resident` to `citizen_or_resident`
  - `is_resident` to `immigration__resident`
  - `is_permanent_resident` to `immigration__permanent_resident`
  - `is_dependent_child` to `dependent_child`
  - `has_a_partner` to `in_a_relationship`
  - `is_of_full_capacity` to `full_capacity`
  - `home_help__had_multiple_birth` to `home_help__multiple_birth`
  - `has_dependent_child` to `person_has_dependent_child`
  - `has_community_services_card` to `community_services_card`
  - `married_or_in_a_civil_union_or_de_facto_relationship` to `married_or_civil_union_or_de_facto_relationship`
  - `is_attending_school` to `attending_school`
  - `is_a_parent` to `person_is_parent`
  - `is_in_civil_union` to `civil_union`
  - `is_married` to `married`
  - `is_in_de_facto_relationship` to `de_facto_relationship`
  - `student_allowance__is_married_or_partnered` to `student_allowance__married_or_partnered`
  - `marriage__is_married` to `marriage__married`
  - `social_security__is_dependent_child` to `social_security__dependent_child`
  - `social_security__is_financially_independent` to `social_security__financially_independent`
  - `social_security__is_in_full_employment` to `social_security__full_employment`
  - `social_security__is_a_child` to `social_security__child`
  - `social_security__is_dependent_child` to `social_security__dependent_child`
  - `social_security__has_dependant_child` to `social_security__person_has_dependant_child`
  - `social_security__is_the_parent_of_dependent_child` to `social_security__parent_of_dependent_child`
  - `social_security__has_child_in_family` to `social_security__child_in_family`
  - `social_security__is_fulltime_student` to `social_security__fulltime_student`
  - `social_security__has_accomodation_costs` to `social_security__accomodation_costs`
  - `social_security__is_a_beneficiary` to `social_security__a_beneficiary`
  - `social_security__is_being_paid_jobseeker_benefit` to `social_security__paid_jobseeker_benefit`
  - `social_security__is_being_paid_sole_parent_support` to `social_security__paid_sole_parent_support`
  - `social_security__is_being_paid_a_supported_living_payment` to `social_security__paid_a_supported_living_payment`
  - `social_security__is_being_paid_a_youth_payment` to `social_security__paid_a_youth_payment`
  - `social_security__is_being_paid_a_young_parent_payment` to `social_security__paid_a_young_parent_payment`
  - `social_security__is_being_paid_an_emergency_benefit` to `social_security__paid_an_emergency_benefit`
  - `social_security__has_severely_restricted_capacity_for_work` to `social_security__severely_restricted_capacity_for_work`
  - `social_security__is_totally_blind` to `social_security__totally_blind`
  - `social_security__disability_was_self_inflicted` to `social_security__disability_self_inflicted`
  - `social_security__is_principal_carer_for_one_year_from_application_date` to `social_security__principal_carer_for_one_year_from_application_date`
  - `social_security__has_orphaned_child_in_family` to `social_security__orphaned_child_in_family`
  - `social_security__is_orphaned` to `social_security__orphaned`
  - `social_security__has_resided_continuously_in_nz_for_a_period_of_at_least_2_years_at_any_one_time` to `social_security__resided_continuously_nz_2_years_citizen_or_resident`
  - `social_security__is_ordinarily_resident_in_new_zealand` to `social_security__ordinarily_resident_in_new_zealand`
  - `social_security__eligible_for_child_disability_allowance` to `child_disability_allowance__eligible`
  - `disability_allowance__family_has_eligible_child` to `child_disability_allowance__family_has_eligible_child`
  - `social_security__child_meets_child_disability_allowance_criteria` to `child_disability_allowance__allowance_criteria`
  - `jobseeker_support__is_prepared_for_employment` to `jobseeker_support__willing_and_able`
  - `social_security__eligible_for_accommodation_supplement` to `accommodation_supplement__eligible`
  - `social_security__eligible_for_unsupported_childs_benefit` to `unsupported_child__entitled`
  - `social_security__has_unsupported_child_in_family` to `unsupported_child__unsupported_child_in_family`
  - `social_security__eligible_for_orphans_benefit` to `orphans_benefit__entitled`
  - `social_security__eligible_for_sole_parent_support` to `sole_parent_support__entitled`
  - `sole_parent_support__meets_age_threshold` to `sole_parent_support__age_threshold`
  - `sole_parent_support__meets_years_in_nz_requirement` to `sole_parent_support__years_in_nz_requirement`
  - `social_security__meets_young_parent_payment_in_relationship_requirements` to `young_parent_payment__relationship_requirements`
  - `social_security__meets_young_parent_payment_single_persons_requirements` to `young_parent_payment__single_young_persons`
  - `social_security__family_income_under_young_parent_payment_threshold` to `young_parent_payment__family_income_under_threshold`
  - `social_security__eligible_for_young_parent_payment` to `young_parent_payment__entitled`
  - `social_security__meets_young_parent_payment_basic_requirements` to `young_parent_payment__basic_requirements`
  - `social_security__income_under_young_parent_payment_threshold` to `young_parent_payment__income_under_threshold`
  - `social_security__is_ordinarily_resident_in_country_with_reciprocity_agreement` to `social_security__ordinarily_resident_in_country_with_reciprocity_agreement`
  - `family_scheme__has_dependent_children` to `family_scheme__dependent_children`
  - `immigration__is_recognised_refugee` to `immigration__recognised_refugee`
  - `immigration__is_protected_person` to `immigration__protected_person`
  - `parental_leave__is_primary_carer` to `parental_leave__primary_carer`
  - `parental_leave__is_the_biological_mother` to `parental_leave__biological_mother`
  - `parental_leave__is_spouse_or_partner_of_the_biological_mother` to `parental_leave__spouse_or_partner_of_biological_mother`
  - `civil_union__civil_union` to `civil_union__civil_union`
  - `acc__is_receiving_compensation` to `acc__receiving_compensation`
  - `veterans_support__is_entitled_to_be_paid_veterans_pension` to `veterans_support__entitled`
  - `property_relationships__is_in_de_facto_relationship` to `property_relationships__de_facto_relationship`
  - `student_allowance__is_tertiary_student` to `student_allowance__tertiary_student`
  - `student_allowance__is_enrolled_fulltime` to `student_allowance__enrolled_fulltime`
  - `student_allowance__is_secondary_student` to `student_allowance__secondary_student`
  - `super__is_being_paid_nz_superannuation` to `super__being_paid_nz_superannuation`
  - `social_security__is_required_to_give_fulltime_care` to `supported_living_payment__caring_for_another_person`
  - `student_allowance__is_childless` to `student_allowance__childless`
  - `student_allowance__is_a_dependent_student` to `student_allowance__dependent_student`
  - `student_allowance__is_living_with_a_parent` to `student_allowance__living_with_a_parent`
  - `student_allowance__is_a_student` to `student_allowance__student`
  - `student_allowance__has_a_supported_child` to `student_allowance__supported_child`
  - `veterans_support__is_being_paid_a_veterans_pension` to `veterans_support__being_paid_a_veterans_pension`
  - `acc__has_cover` to `acc__cover`
  - `acc__part_3__has_lodged_claim` to `acc_part_3__lodged_claim`
  - `acc__part_2__suffered_personal_injury` to `acc_part_2__suffered_personal_injury`
  - `acc__has_a_covered_injury` to `acc__person_has_covered_injury`
  - `acc__sched_1__engaged_fulltime_study_or_training` to `acc_sched_1__engaged_fulltime_study_or_training`
  - `acc__sched_1__incapacitated_for_6_months` to `acc_sched_1__incapacitated_for_6_months`
  - `acc__sched_1__weekly_earnings` to `acc_sched_1__weekly_earnings`
  - `acc__sched_1__lope_eligible` to `acc_sched_1__lope_eligible`
  - `acc__sched_1__minimum_weekly_earnings` to `acc_sched_1__minimum_weekly_earnings`
  - `acc__sched_1__lope_weekly_compensation` to `acc_sched_1__lope_weekly_compensation`
  - `acc__lope__incapacity_for_employment__by_covered_injury` to `incapacity_for_employment__caused_covered_injury`
  - `acc__sched_1__loe_more_than_lope` to `acc_sched_1__loe_more_than_lope`
  - `student_allowance__has_a_spouse` to `student_allowance__person_has_spouse`
  - `parental_leave__has_spouse_who_transferred_her_entitlement` to `parental_leave__spouse_who_transferred_her_entitlement`
  - `social_security__single_young_person_in_exceptional_circumstances` to `youth_payment__single_young_person_exceptional_circumstances`
  - `citizenship__meets_minimum_presence_requirements` to `citizenship__minimum_presence_requirements`
  - `citizenship__meets_each_year_minimum_presence_requirements` to `citizenship__each_year_minimum_presence_requirements`
  - `citizenship__meets_preceeding_single_year_minimum_presence_requirement` to `citizenship__preceeding_single_year_minimum_presence_requirement`
  - `citizenship__meets_5_year_presence_requirement` to `citizenship__5_year_presence_requirement`
  - `super__eligibility` to `super__eligible`
  - `is_a_step_parent` to `person_is_step_parent`
  - `social_security_regulation__family_has_resident_child_under_5_not_in_school` to `childcare_assistance__family_has_resident_child_under_5_not_in_school`
  - `social_security_regulation__eligible_for_childcare_subsidy` to `childcare_assistance__eligible_childcare_subsidy`
  - `social_security_regulation__family_has_resident_child_aged_5_who_will_be_enrolled_in_school` to `childcare_assistance__resident_child_aged_5_will_be_enrolled_in_school`
  - `social_security_regulation__family_has_child_eligible_for_disability_allowance_child_under_6` to `childcare_assistance__family_has_child_eligible_for_disability_allowance_child_under_6`
  - `social_security_regulation__household_income_below_childcare_subsidy_threshold` to `childcare_assistance__household_income_below_childcare_subsidy_threshold`
* Removed excess variable `immigration__holds_permanent_resident_visa`
* Added `orphans_benefit`,`unsupported_child`,`child_disability_allowance`,`young_parent_payment` to structure.json

## 12.1.0 [16](https://github.com/govzeroaotearoa/openfisca-aotearoa/pull/16)

* Removal of some tests while underlying issue in openfisca core is resolved (see openfisca_core/holders/helpers.py and period days)
* Adjustments to some tests to account for above issue
* Breaking changes:
 - age_of_partner now returns the maximum age of partners rather than assuming one as this section was failing to run after upgrade

### 12.0.1 [13](https://github.com/govzeroaotearoa/openfisca-aotearoa/pull/13)

* Allows utilisation of the vscode .devcontainer development process. Requires container environment.

# 12.0.0 [183](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/183)

* Upgrade to Open Fisca Core 30.x
* Breaking changes:
 - no longer accepts MONTH period values for variables that are by DAY
 - age variables must be set for a DAY period, not MONTH or YEAR

### 11.3.2 [184](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/184)

* No functional changes.
  - Added regression test for age calculations

## 11.3.0 [178](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/178)

* Accident Compensation Act - Loss of Earnings and Loss of Potential Earnings

## 11.2.0 [176](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/176)

* Bug Fix
  - Rates Rebate algorithm formula incorrectly allowed negative excess income

### 11.1.3 [174](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/174)

* No functional changes.
  - Removing unnecessary family groups in tests
  - Better names for tests

### 11.1.2 [170](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/170)

* No functional changes.
  - Removing unnecessary family/titled_property groups in tests

### 11.1.1 [169](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/169)

* Rename duplicate tests (same name, different test)

## 11.1.0 [167](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/167)

* Adds values for Rates Rebates 2018 to 2019

# 11.0.0 [163](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/163)

* Upgrade to Open Fisca 29.x

### 10.2.1 [159](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/159)

* No functional changes.
  - Removed debug print statement

## 10.2.0 [153](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/153)

* Update to Openfisca Core 26.0

### 10.1.3 [148](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/148)

* Add Hamish to maintainers

### 10.1.2 [150](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/150)

* Automate git tagging of release

### 10.1.1 [122](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/122)

* Grammar fix up in variable labels

## 10.1.0 [142](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/142)

* Add formula for Primary Carer in Paid Parental Leave

# 10.0.0 [145](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/145)

* Upgrades to Open Fisca core 25.0
* Removed support for Python 2.7
* Updated all yaml tests to new format

## 9.2.0 - [141](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/141)

* add `immigration__entitled_to_indefinite_stay` for use in citizenship presence calculations

## 9.1.0 - [#139](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/139)

* Fix calculation of number of days present in NZ for Citizenship by Grant

### 9.0.1 - [#121](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/121)

* Added unit (years) to ages
* Added unit (NZD) to best_start__entitlement

# 9.0.0 - [#132](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/132)

* Removed duplicate parameter `general/age_of_superannuation`

### 8.0.1 - [#126](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/126)

* Changed Formula:
  - Removed `family_scheme__full_time_earner` from `family_scheme__qualifies_for_family_tax_credit`

# 8.0.0 - [#125](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/125)

* Renamed variables:
  - `family_scheme__in_work_tax_credit_is_full_time_earner` replaced with `family_scheme__full_time_earner`

# 7.0.0 - [#124](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/124)

* Renamed variables:
  - `social_security__eligible_for_childcare_subsidy` to `childcare_assistance__eligible_childcare_subsidy`
  - `sole_parent__family_has_child_under_age_limit` to `sole_parent_support__family_has_child_under_age_limit`
  - `family_has_resident_child_under_5_not_in_school` to `childcare_assistance__family_has_resident_child_under_5_not_in_school`
  - `family_has_resident_child_aged_5_who_will_be_enrolled_in_school` to `childcare_assistance__resident_child_aged_5_will_be_enrolled_in_school`
  - `family_has_child_eligible_for_disability_allowance_child_under_6` to `childcare_assistance__family_has_child_eligible_for_disability_allowance_child_under_6`
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

### 6.1.2 - [#117](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/117)

#### Bug fix

  - no longer throws unhandled exception when working on leap days

### 6.1.1 - [#115](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/115)

#### New variable

  - `citizenship__preceeding_single_year_minimum_presence_requirement`

## 6.1.0 - [#101](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/101)

* Added Citizen-by-grant presence in NZ requirements algorithm
* Change `age` to be changing by `DAY`
* Uses `day` branch from Open Fisca
* New Variables
  - `citizenship__citizenship_by_grant_may_be_authorized`
  - `citizenship__minimum_presence_requirements`
  - `days_present_in_new_zealand_in_preceeding_5_years`
  - `days_present_in_new_zealand_in_preceeding_year`
  - `present_in_new_zealand`
  - `full_capacity`
  - `immigration__holds_indefinite_stay_visa`
  - `citizenship__of_good_character`
  - `citizenship__sufficient_knowledge_responsibilities_and_privileges`
  - `citizenship__sufficient_knowledge_english_language`
  - `citizenship__intends_to_reside_in_nz`
  - `citizenship__intends_nz_employment`
  - `citizenship__intends_international_service`
  - `citizenship__intends_crown_service`


### 6.0.3 - [#104](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/104)

#### Refactor to remove unused variables

  - Removed `acc__elected_for_weekly_compensation`
  - Removed `social_security__cash_assets`
  - Removed `family_scheme__proportion_as_principal_carer`
  - Removed `social_security__is_a_specified_beneficiary`
  - Removed `income_tax__tax_payer_filing_status`

### 6.0.2 - [#103](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/103)

#### Tidyup metadata

* Adding yet more missing labels

### 6.0.1 - [#102](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/102)

#### Tidyup metadata

* Adding missing labels, shortened long labels and improved language in descriptions

# 6.0.0 - [#98](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/98)

#### Technical improvement

* Upgrade to Python 3.7

### 5.1.4 - [#100](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/100)

#### Technical improvement
    Pin to version 24.3.0, to ensure we support legislation explorer
    the `/entities` route was added to the API in this version

### 5.1.3 - [#97](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/97)

#### Refactored NZ Superannuatio
  - Added `super__eligible_age`
  - Removed age requirement from `super__eligible`
  - Removed `super__living_alone` and `super__has_partner_in_long_term_care_or_rest_home`

### 5.1.2 - [#94](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/94)

#### Added NZ Superannuatio

### 5.1.1 - [#93](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/93)

#### Bug fix
  - adding residency requirements to entitlements

## 5.1.0 - [#92](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/92)

#### Tax and benefit system evolution

  - adding income test to Family Tax Credit
  - added variables `family_scheme__in_work_tax_credit_is_full_time_earner, family_scheme__in_work_tax_credit_income_under_threshold, family_scheme__family_tax_credit_income_under_threshold`

### 5.0.2 - [#88](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/88)

#### Tax and benefit system evolution

  - added formula for is_permanent_resident

### 5.0.1 - [#81](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/81)

#### Calculation improvement

 * Added Home Help

# 5.0.0 - [#83](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/83)

#### Tax and benefit system evolution. Major change.

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


### 4.2.6 - [#81](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/81)

#### Calculation improvement

 * Added Home Help

### 4.2.5 - [#84](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/87)

#### Calculation improvement

 * Added Childcare Subsidy

### 4.2.4 - [#77](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/86)

#### Calculation improvement

 * Added Unsupported Child Benefit
 * Added Orphan's benefit

### 4.2.3 - [#77](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/77)

#### Technical improvement

 * Remove dependency on OpenFisca-Web-API (now included in Core)
 * Update README.md with notes on updating OpenFisca-Core for existing developers

### 4.2.2 - [#78](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/78)

#### Calculation improvement

 * Added Paid Parental Leave Regulations

### 4.2.1 - [#75](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/75)

#### Calculation improvement

 * Added Student Allowance Regulations
 * Seperated Acts and Regulations
 * Adding Relationship status
 * Adding Superannuation age qualifications.

## 4.2.0

#### Hotfix

 * Mark source code as UTF8

### 4.1.6 - [#41](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/74)

#### Calculation improvement

 * Added Young Parent Payment for single person

### 4.1.5 - [#72](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/72)

#### Calculation improvement

  * Added Community Service Card

### 4.1.4 - [#41](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/55)

#### Calculation improvement

 * Added Jobseeker Support for 18 and 19 year olds

### 4.1.3 - [#41](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/55)

#### Calculation improvement

* addded Supported living payment
* Organising by numbered section of the act
* Moved Social Security Act disability definitions to that folder
* Move social security tests to folder with that name
* refactored to add "is_citizen_or_resident" variable
* Renaming job seeker to Jobseeker Support
* Restructured Social Security Act variables

### 4.1.2 - [#41](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/55)

#### Calculation improvement

* Added Sole Parent Support

### 4.1.1 - [#41](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/53)

#### Calculation improvement.

* Added Job Seeker Support

## 4.1.0 - [#41](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/51)

#### Calculation improvement

* Added Child Disability Allowance
* Added "Others" role within a titled_property
* Added "Others" role within a family

### 4.0.2 - [#42](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/22)

#### Legislation improvement

* Added Accommodation Supplement from the Social Security Act 1964

### 4.0.1 - [#42](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/42)

#### Technical improvement

* Details:
  - Moving the version bump check to its own segment of the circle ci config, This means it appears as a separate check within a github PR, and so we can see quickly that the input/output tests pass - and it's only the version bump that's missing.

# 4.0.0 - [#22](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/22)

#### Tax and benefit system evolution; Major change

* Impacted periods: all
* Impacted areas: `entities.families, tests/best_start, tests/family_scheme, tests/working_for_families, variables/demographics, variables/rates_rebates, variables/entitlements/income_tax/best_start.py, variables/entitlements/income_tax/family_scheme.py, variables/entitlements/income_tax/working_for_families.py`
* Details:
  - removed extraneous rates_rebates variable file,
  - added `variables/demographics` section with variables (`date_of_birth, due_date_of_birth, age, age_of_youngest`)
  - added `variables/entitlements/income_tax/best_start.py` with variables (`income_tax__caregiver_eligible_for_best_start_tax_credit, income_tax__family_has_children_eligible_for_best_start, income_tax__best_start_tax_credit_per_child,  income_tax__entitlement_for_best_start_tax_credit, income_tax__person_is_best_start_child_as_year`)
  - added `variables/entitlements/income_tax/family_scheme.py` with variables (`income_tax__qualifies_for_entitlements_under_family_scheme, income_tax__caregiver_age_qualifies_under_family_scheme, income_tax__person_principal_carer_qualifies_under_family_scheme, income_tax__family_scheme_income, income_tax__proportion_as_principal_carer`)
  - added `variables/entitlements/income_tax/working_for_families.py` with variables (`social_security__received_income_tested_benefit, veterans_support__received_parents_allowance, veterans_support__received_childrens_pension, income_tax__resident, income_tax__family_has_dependent_children, income_tax__dependent_child`)

# 3.0.0 - [#20](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/20)

#### Tax and benefit system evolution

* Impacted periods: all.
* Impacted areas:
  - Variables `income_tax__tax_payer_filing_status, income_tax__annual_gross_income, income_tax__annual_total_deduction, income_tax__net_income, income_tax__net_loss, income_tax__available_tax_loss, income_tax__taxable_income, rates_rebates__dependants, rates_rebates__rates_total, rates_rebates__combined_income, rates_rebates__rebate, rates_rebates__maximum_income_for_full_rebate, rates_rebates__minimum_income_for_no_rebate`
* Details:
  - Variable renaming, impacts the OpenFisca-Aotearoa public API (for instance renaming or removing a variable)

## 2.2.0 - [#19](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/19)

#### Tax and benefit system evolution

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

#### Tax and benefit system evolution

* Impacted periods: from 2000-04-01
* Impacted areas:
  - Variables `tax_payer_filing_status__income_tax, annual_gross_income__income_tax, annual_total_deduction__income_tax, net_income__income_tax, net_loss__income_tax, available_tax_loss__income_tax, taxable_income__income_tax`
  - Parameters `individual_income_tax_rate`
* Details:
  - Introducing some initial income_tax variables, laid out as per current best practice

# 2.0.0 - [#12](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/12)

#### Tax and benefit system evolution

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

#### Tax and benefit system evolution

* Impacted periods: from 1973-07
* Impacted areas:
  - Variables `rates_rebates`
* Details:
  - Addition of Math floor function to conform rates_rebates variable with existing infrastructure.


# 1.0.0 - [#6](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/6)

#### Tax and benefit system evolution

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

#### Tax and benefit system evolution

* Impacted periods: from 1898-01-01
* Impacted areas:
  - Parameters `general`
* Details:
  - Introduce new general legislation parameters
    - Introduce `general/age_of_majority` parameter
    - Introduce `general/age_of_superannuation` parameter
<!-- -->

#### Tax and benefit system evolution

* Impacted periods: from 2000-04-01
* Impacted areas:
  - Parameters `taxes`
* Details:
  - Introduce income tax parameters
    - Introduce `taxes/income_tax_rate` parameter
