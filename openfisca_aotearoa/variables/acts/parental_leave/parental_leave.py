# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person, Family


class parental_leave__is_primary_carer(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Is primary carer, as per the Parental Leave Act 1987"
    reference = "http://www.legislation.govt.nz/act/public/1987/0129/latest/DLM120458.html"

    def formula_1987(persons, period, parameters):
        biological_mother = persons('parental_leave__is_the_biological_mother', period)
        her_spouse = persons('parental_leave__is_spouse_or_partner_of_the_biological_mother', period)
        other = persons('parental_leave__a_person_other_than_biological_mother_or_her_spouse', period)
        permanent = persons('parental_leave__taking_permanent_primary_responsibility_for_child', period)

        # Mark who is the principal caregiver, as there may be >1 eligible
        nominated = persons.has_role(Family.PRINCIPAL_CAREGIVER)

        return nominated * (biological_mother + her_spouse + (other * permanent))


class parental_leave__is_the_biological_mother(Variable):
    value_type = bool
    entity = Person
    definition_period = ETERNITY
    label = u"a female (the biological mother) who is pregnant or has given birth to a child"
    reference = "http://www.legislation.govt.nz/act/public/1987/0129/latest/DLM120458.html"


class parental_leave__is_spouse_or_partner_of_the_biological_mother(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"the spouse or partner of the biological mother"
    reference = "http://www.legislation.govt.nz/act/public/1987/0129/latest/DLM120458.html"

    def formula_1987(persons, period, parameters):
        is_principal = persons.has_role(Family.PRINCIPAL_CAREGIVER)

        biological_mother = persons.family.members('parental_leave__is_the_biological_mother', period)
        partner_is_biological_mother = persons.family.any(biological_mother, role=Family.PARTNER)

        return is_principal * partner_is_biological_mother


class parental_leave__a_person_other_than_biological_mother_or_her_spouse(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"a person, other than the biological mother or her spouse or partner"
    reference = "http://www.legislation.govt.nz/act/public/1987/0129/latest/DLM120458.html"


    def formula_1987(persons, period, parameters):
        biological_mother = persons.family.members('parental_leave__is_the_biological_mother', period)
        partner_is_biological_mother = persons.family.any(biological_mother, role=Family.PARTNER)

        return not_(biological_mother) * not_(partner_is_biological_mother)



class parental_leave__taking_permanent_primary_responsibility_for_child(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"taking permanent primary responsibility for the care, development, and upbringing of a child who is under the age of 6 years (and if there is more than 1 such person, the person nominated in accordance with subsection (2))."
    reference = "http://www.legislation.govt.nz/act/public/1987/0129/latest/DLM120458.html"


class parental_leave__applied_for_leave_or_stopped_working(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Has applied for/taken leave or stopped working immediately"
    reference = "http://www.legislation.govt.nz/act/public/1987/0129/latest/DLM121773.html"


class parental_leave__threshold_tests(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = u"satisfies Parental Leave Threshold Tests (tests are used to determine an employee's entitlements to parental leave)"
    reference = u"http://www.legislation.govt.nz/act/public/1987/0129/latest/DLM6810651.html"


class parental_leave__had_previous_parental_leave_in_last_six_months(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Had previous parental leave in last six months"
    reference = u"http://www.legislation.govt.nz/act/public/1987/0129/latest/DLM120450.html"


class parental_leave__eligible_employee(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u"Eligible employee"
    reference = u"http://www.legislation.govt.nz/act/public/1987/0129/latest/DLM121539.html"

    def formula(persons, period, parameters):
        is_citizen = persons('is_nz_citizen', period)

        return is_citizen * persons('parental_leave__is_primary_carer', period) * \
            persons('parental_leave__applied_for_leave_or_stopped_working', period) * \
            (persons('parental_leave__threshold_tests', period) >= 6) * \
            not_(persons('parental_leave__had_previous_parental_leave_in_last_six_months', period))
