# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class social_security__meets_young_parent_payment_single_persons_requirements(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Meets Young Parent Payment single person requirements from section 165"
    reference = """
        165 Young parent payment: single young persons
        (1) A young person is entitled to receive a young parent payment if—
            (a) section 164(2) applies to him or her; and
            (b) subsection (2) or subsection (3) or subsection (4) applies to him or her.
        (2) This subsection applies to a single young person if he or she—
            (a) is aged 16 or 17 years; and
            (b) is not living with a parent or guardian; and
            (c) is in exceptional circumstances (within the meaning of section 159).
        (3) This subsection applies to a single young person if—
            (a) he or she is aged 16 or 17 years; and
            (b) he or she is living with or being financially supported by a parent or guardian; and
            (c) the family scheme income (within the meaning of the Income Tax Act 2007) of the parent or guardian concerned and the spouse or partner (if any)
                of the parent or guardian concerned is less than the amount that would, in accordance with sections MD 1 and MD 13 of that Act, fully abate
                the amount of the parent or guardian concerned’s family tax credit entitlement under that Act.
        (4) This subsection applies to a single young person who is aged 18 years or 19 years.
        (5) For the purposes of the calculation required by subsection (3)﻿(c), if the parent or guardian with whom the young person concerned is living or by
            whom he or she is being supported has no family tax credit entitlement because that parent or guardian has no dependent children (within the
            meaning of section YA 1 of the Income Tax Act 2007), that parent or guardian’s family tax credit entitlement must be calculated as if the
            young person and his or her dependent child or children were dependent children (within the meaning of that section) of that parent or guardian.
        (6) Nothing in this section entitles a parent or guardian to whom subsection (5) applies to a family tax credit.
        """

    def formula(persons, period, parameters):
        sixteen_or_seventeen = (persons('age', period.start) >= 16) * (persons('age', period.start) < 18)
        eighteen_or_nineteen = (persons('age', period.start) >= 18) * (persons('age', period.start) < 20)

        living_with_parent_or_guardian = persons('living_with_parent_or_guardian', period)
        financially_supported_by_parent_or_guardian = persons('financially_supported_by_parent_or_guardian', period)

        family_income_under_threshold = persons('social_security__family_income_under_young_parent_payment_threshold', period)

        exceptional_circumstances = persons('social_security__single_young_person_in_exceptional_circumstances', period)

        section_2 = sixteen_or_seventeen * not_(living_with_parent_or_guardian) * exceptional_circumstances
        section_3 = sixteen_or_seventeen * (living_with_parent_or_guardian + financially_supported_by_parent_or_guardian) * family_income_under_threshold
        section_4 = eighteen_or_nineteen

        # is a parent?

        # TODO section_5

        return (section_2 + section_3 + section_4)


class social_security__family_income_under_young_parent_payment_threshold(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person's family income is under the young parent payment threshold"

    def formula(persons, period, parameters):
        yearly_income_threshold = 52 * parameters(period).entitlements.social_security.young_parent_payment.weekly_income_threshold
        yearly_family_income = persons('family_scheme__assessable_income_for_month', period) * 12
        return yearly_family_income < yearly_income_threshold
