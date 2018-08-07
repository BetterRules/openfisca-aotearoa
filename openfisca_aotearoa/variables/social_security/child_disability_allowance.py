from openfisca_aotearoa.entities import Person
from openfisca_core.model_api import *

# """
# Benefit: Part 1D Child with Serious Disability (eligible):

# If child.isDependent
#     and child.hasSeriousDisability
#     and child.requiresConstantCareAndAttention
#     and child.hasMedicalCertification
#     and applicapplicant_is_principal_carer
#     and applicant.isNZResident
#         then benefit.ChildDisabilityAllowance is PERMITTED
# """


class social_security__eligible_for_child_disability_allowance(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eligible for Child Disability Allowance"
