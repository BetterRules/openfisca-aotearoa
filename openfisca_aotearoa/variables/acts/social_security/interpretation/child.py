# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person, Family


class social_security__has_dependant_child(Variable):
    value_type = bool
    entity = Person
    label = u"has a dependent child (or children)"
    definition_period = MONTH


class social_security__is_a_child(Variable):
    value_type = bool
    entity = Person
    label = u"""child means a single person under the age of 18 years, other than a person who is—
        (a) aged 16 years or 17 years; and
        (b) financially independent
        """
    definition_period = MONTH
    reference = u""

    def formula(persons, period, parameters):
        under_16 = persons('age', period.start) < 16
        under_18 = persons('age', period.start) < 18

        financially_independent = persons(
            'social_security__is_financially_independent', period)

        return under_16 + (under_18 * not_(financially_independent))


class is_dependent_child(Variable):
    value_type = bool
    entity = Person
    label = "Is a dependent child"
    reference = ""
    definition_period = MONTH


class social_security__is_dependent_child(Variable):
    value_type = bool
    entity = Person
    label = "Is a dependent child"
    reference = ""
    definition_period = MONTH
    #  dependent child, in relation to any person,—
    # (a) means a child—
    # (i) whose care is primarily the responsibility of the person; and
    # (ii) who is being maintained as a member of that person’s family; and
    # (iii) who is financially dependent on that person:
    # (b) does not include a child in respect of whom payments are being made under section 363 of the Oranga Tamariki Act 1989:
    # (c) despite paragraph (b), includes a child or a young person (as defined in section 2(1) of the Oranga Tamariki Act 1989)—
    # (i) of whom the person is a parent within the meaning of that Act; and
    # (ii) to whom section 361 of that Act applies; and
    # (iii) who, under section 362 of that Act, is placed in the charge of the person:
    # (d) for the purposes only of Schedules 3, 3A, 6, 9, 16, 17, 18, and 26, does not include a child in respect of whom an orphan’s benefit or an unsupported child’s benefit is being paid:
    # (e) does not include a child in respect of whom a young parent payment is being paid except in relation to that child’s parent or step-parent:
    # (f) for the purposes of clause 1(a) and (b) of Schedule 18A (rates of winter energy payment), has the meaning given to it by clause 2 of Schedule 18A

    def formula(persons, period, parameters):
        return persons('social_security__is_a_child', period) * persons('is_dependent_child', period)


class social_security__has_child_in_family(Variable):
    value_type = bool
    entity = Family
    definition_period = MONTH
    label = "Family has a child"

    def formula(families, period, parameters):
        children = families.members('social_security__is_a_child', period)
        return families.any(children, role=Family.CHILD)
