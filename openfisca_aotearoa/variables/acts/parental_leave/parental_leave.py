# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and entitlement system
from openfisca_aotearoa.entities import Person


class parental_leave__is_primary_carer(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = u"Is primary carer"
    reference = """
    http://www.legislation.govt.nz/act/public/1987/0129/latest/DLM120458.html?search=qs_act%40bill%40regulation%40deemedreg_parental+leave_resel_25_h&p=1#DLM120458
    Are you a primary carer that is:
    • an expectant mother (you are pregnant or have a baby under 1 year old)
    or
    • a primary carer who takes permanent primary responsibility for a child under 6 years old (such as
    adoptive parent, home for life parent, whāngai, grandparent with permanent full-time care and others
    with permanent care arrangements). Permanent primary responsibility does not include part-time or
    temporary responsibility such as foster care or childcare arrangements.
    Note: A primary carer does not include the spouse or partner of the expectant mother. The mother will
    need to apply (IR880) and transfer the entitlement (IR881).
    """


class parental_leave__passes_6_month_employment_test(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = u"Number of Persons classified as dependant for the purposes of rates rebates"
    reference = """
    http://www.legislation.govt.nz/act/public/1987/0129/latest/link.aspx?search=qs_act%40bill%40regulation%40deemedreg_parental+leave_resel_25_h&p=1&id=DLM6810651#DLM6810651

    In this Act, the following tests are used to determine an employee’s entitlements to parental leave:
    (a) an employee meets the 6-month employment test if the employee will have been employed by the same employer for at least an average of 10 hours a week in the 6 months immediately preceding the expected date of—
      (i) delivery of the child (in the case of a child to be born to the employee or to the employee’s spouse or partner); or
      (ii) assumption of responsibility for the care of the child (in any other case):
        (b) an employee meets the 12-month employment test if the employee will have been employed by the same employer for at least an average of 10 hours a week in the 12 months immediately preceding the expected date of—
          (i) delivery of the child (in the case of a child to be born to the employee or to the employee’s spouse or partner); or
          (ii) assumption of responsibility for the care of the child (in any other case).
    """


class parental_leave__passes_12_month_employment_test(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = u"Number of Persons classified as dependant for the purposes of rates rebates"
    reference = """
    http://www.legislation.govt.nz/act/public/1987/0129/latest/link.aspx?search=qs_act%40bill%40regulation%40deemedreg_parental+leave_resel_25_h&p=1&id=DLM6810651#DLM6810651

    In this Act, the following tests are used to determine an employee’s entitlements to parental leave:
    an employee meets the 12-month employment test if the employee will have been employed by the same employer for at least an average of 10 hours a week in the 12 months immediately preceding the expected date of—
    (i) delivery of the child (in the case of a child to be born to the employee or to the employee’s spouse or partner); or
    (ii) assumption of responsibility for the care of the child (in any other case).
    """


class parental_leave__applied_for_leave_or_stopped_working(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = u"Has applied for/taken leave or stopped working immediately"


class parental_leave__had_previous_parental_leave_in_last_six_months(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = u"Had previous parental leave in last six months"


class parental_leave__has_returned_to_work_except_KIT(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = u"Has returned to work (except for Keeping In Touch (KIT) hours)"


class parental_leave__is_employed(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = u"Has worked for one employer for the last 52 weeks up to the due date or the date the child came into their care"
    # if yes, employer declaration required
    # if no, check if they are a doctor rotating between different district health boards, or
    # a teacher who was employed by different boards of trustees in a state school or integrated school
    # if either yes, then employer declaration required

    # if either no,
    # Can just one employer verify that you have worked for them for at least an average of 10 hours
    # per week for any 26 of the last 52 weeks?
    # if yes, Can the same employer verify that you earned the income you have provided in this application?
    # if yes, employer declaration required
    # if no, Statutory declaration required


class parental_leave__is_self_employed(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = u"Is self-employed"
    # if yes, Chartered accountant and tax advisor declaration required
    # if no, Statutory declaration required