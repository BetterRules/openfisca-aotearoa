from openfisca_aotearoa.entities import Person, Family
from openfisca_core.model_api import *


class social_security__is_totally_blind(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligible for Supported Living Payment."


class social_security__has_severely_restricted_capacity_for_work(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Is incapable of regularly working 15 or more hours a week in open employment"
    reference = """
        http://legislation.govt.nz/act/public/1964/0136/latest/whole.html#DLM5468367
        40A Supported living payment: purpose
        (a) people who have, and are likely to have in the future, a severely restricted
            capacity to support themselves through open employment because of sickness, injury, or disability:
        40B (2) A person is permanently restricted in his or her capacity
              for work if the chief executive is satisfied that
        (a) the restricting sickness, injury, or disability is expected to
              continue for at least the period set out in regulations made
              under this Act for the purposes of this section; or
        (b) the person is not expected to live for the period set out in
              those regulations, because the person's sickness, injury, or
              disability is terminal.

        40B (3) A person is severely restricted in his or her capacity for work if
        the chief executive is satisfied that the person is incapable of regularly
        working 15 or more hours a week in open employment.
    """


class social_security__disability_was_self_inflicted(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = """The person's restricted capacity for work, or total blindness, was self-inflicted and brought about by
    the person with a view to qualifying for a benefit"""
    reference = """
        40B (5) A person must not be granted a supported living payment under this section if the chief
        executive is satisfied that the person's restricted capacity for work, or total blindness, was
        self-inflicted and brought about by the person with a view to qualifying for a benefit.
    """
