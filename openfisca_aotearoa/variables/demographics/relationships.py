# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person, Family


# Re-usable variable for having a partner
class has_a_partner(Variable):
    value_type = bool
    entity = Person
    label = u"Is this person in a relationship?"
    definition_period = MONTH  # This variable cannot change over time.
    reference = u"TODO"

    def formula(persons, period, parameters):
        # has 1 or more partners
        number_of_partners = persons.family.nb_persons(role=Family.PARTNER)
        return number_of_partners >= 1


class is_adequately_supported_by_partner(Variable):
    value_type = bool
    entity = Person
    label = u"""Is adequately supported by their partner? (false if lost the regular support of
    their partner as their partner has been imprisoned or is subject to release or detention conditions that prevent employment)
    """
    definition_period = MONTH
    reference = u"https://www.workandincome.govt.nz/map/income-support/main-benefits/sole-parent-support/qualifications.html"
    default_value = True
