# -*- coding: utf-8 -*-

# This file defines the variables of our legislation.
# A variable is property of a person, or an entity (e.g. a property).
# See http://openfisca.org/doc/variables.html

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Propertee


# This variable is a pure input: it doesn't have a formula
class accomodation_size(Variable):
    value_type = float
    entity = Propertee
    definition_period = MONTH
    label = u"Size of the accomodation, in square metres"


# This variable is a pure input: it doesn't have a formula
class rent(Variable):
    value_type = float
    entity = Propertee
    definition_period = MONTH
    label = u"Rent paid by the property"


#  Possible values for the housing_occupancy_status variable, defined further down
class HousingOccupancyStatus(Enum):
    __order__ = "owner tenant free_lodger homeless"
    owner = u'Owner'
    tenant = u'Tenant'
    free_lodger = u'Free logder'
    homeless = u'Homeless'


class housing_occupancy_status(Variable):
    value_type = Enum
    possible_values = HousingOccupancyStatus
    default_value = HousingOccupancyStatus.tenant
    entity = Propertee
    definition_period = MONTH
    label = u"Legal housing situation of the property concerning their main residence"

# This file is from the OpenFisca default country template and as such can be removed
