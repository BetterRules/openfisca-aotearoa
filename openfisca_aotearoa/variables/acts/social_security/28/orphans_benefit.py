from openfisca_aotearoa.entities import Person, Family
from openfisca_core.model_api import *


class social_security__eligible_for_orphans_benefit(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligible for Orphan's benefit"
    reference = "http://www.legislation.govt.nz/act/public/1964/0136/latest/whole.html#DLM361606"
    #  Orphans’ benefits

    # A person who is a principal caregiver in respect of a dependent child shall be entitled to receive an orphan’s benefit in respect of that child if—
    # (a) each of the child’s natural or adoptive parents is dead, or cannot be found, or suffers a serious long-term disablement which renders him or her unable to care for the child; and
    # (b) the applicant is likely to be the principal caregiver in respect of the child for at least 1 year from the date of application for the benefit; and
    # (c) the applicant is aged 18 years or over; and
    # (d) either—
    # (i) the child is both resident and present in New Zealand; or
    # (ii) the applicant has been both resident and present in New Zealand for a continuous period of 12 months at any time.

    def formula(persons, period, parameters):
      # todo
