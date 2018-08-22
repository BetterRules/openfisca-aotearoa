# -*- coding: utf-8 -*-
from openfisca_aotearoa.entities import Person
from openfisca_core.model_api import *


class social_security__meets_residential_requirements_for_certain_benefits(Variable):
    value_type = bool
    entity = Person
    label = u"Residential requirements for certain benefits"
    definition_period = MONTH

    reference = u"""
        74AA Residential requirements for certain benefits
            (1) A person who applies for a benefit of a kind stated in subsection (2) after 27 May 2007 is not eligible for it unless he or she
                (a) is a New Zealand citizen, or is a person who holds a residence class visa under the Immigration Act 2009; and
                (b) is ordinarily resident in New Zealand when he or she first applies for the benefit; and
                (c) except in the case of a person who is recognised as a refugee or a protected person in New Zealand under
                the Immigration Act 2009, has resided continuously in New Zealand for a period of at least 2 years at any one time,
            (i) if subsection (1A) applies to the person,
                (A) before he or she applies for the benefit; or
                (B) before a decision on his or her claim for the benefit is made under section 12; and
            (ii) in any other case, after the day on which paragraph (a) first applied to him or her.
        (1A) Subsection (1)﻿(a) and (b) do not apply to a person at a time when
        (a) there is in force under section 19(1) of the Social Welfare (Reciprocity Agreements,
                and New Zealand Artificial Limb Service) Act 1990 an order declaring that the provisions
                contained in an agreement or convention with the government of another country set out
                in a schedule to the order have force and effect so far as they relate to New Zealand; and
            (b) he or she is ordinarily resident in that country.
            (2) The benefits referred to in subsection (1) are a youth payment, a young parent payment,
                a supported living payment, jobseeker support, and sole parent support.
        """

    def formula(persons, period, parameters):
        # (a) is a New Zealand citizen, or is a person who holds a residence class visa under the Immigration Act 2009
        is_citizen_or_resident = persons('is_citizen_or_resident', period)

        # (b) is ordinarily resident in New Zealand when he or she first applies for the benefit; and
        normally_lives_in_nz = persons('social_security__is_ordinarily_resident_in_new_zealand', period)

        # (c) except in the case of a person who is recognised as a refugee or a protected person in New Zealand under
        # the Immigration Act 2009, has resided continuously in New Zealand for a period of at least 2 years at any one time,
        is_refugee_or_protected = persons('immigration__is_recognised_refugee', period) + persons('immigration__is_protected_person', period)

        enough_years_in_nz = persons('social_security__has_resided_continuously_in_nz_for_a_period_of_at_least_2_years_at_any_one_time', period)

        return (is_citizen_or_resident * normally_lives_in_nz) + (is_refugee_or_protected * enough_years_in_nz)


class social_security__is_ordinarily_resident_in_new_zealand(Variable):
    value_type = bool
    entity = Person
    label = u"74AA (b) is ordinarily resident in New Zealand when he or she first applies for the benefit"
    definition_period = MONTH

    def formula(persons, period, parameters):
        return persons('normally_lives_in_nz', period)


class social_security__has_resided_continuously_in_nz_for_a_period_of_at_least_2_years_at_any_one_time(Variable):
    value_type = bool
    entity = Person
    label = u"has resided continuously in New Zealand for a period of at least 2 years at any one time"
    definition_period = MONTH
